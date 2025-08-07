import os
import re
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_question_txt(txt_file_path):
    """
    Extracts the question statement, solution, and tests from a Markdown-generated file.
    
    Args:
        txt_file_path (str): Path to the .txt file containing the question.
        
    Returns:
        dict: Dictionary containing 'enunciado' (statement), 'solucao' (solution), 
              and 'testes' (list of test cases with number, input, and output).
    """
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find all major sections
    section_pattern = re.compile(r"(####|###)\s*(Enunciado|Code Solução|Solução|Testes)", re.IGNORECASE)
    sections = list(section_pattern.finditer(content))
    
    enunciado, solucao, test_content = "", "", ""
    if not sections:
        # Fallback for files that might not have clear markdown headers
        if "```python" in content and "Entrada:" in content:
            parts = re.split(r'(```python|```)', content)
            enunciado = parts[0].strip()
            solucao = parts[2].strip() if len(parts) > 2 else ""
            test_content = content.split("#### Testes")[-1] if "#### Testes" in content else ""
    else:
        # Process sections found by regex
        for i, match in enumerate(sections):
            start_pos = match.end()
            end_pos = sections[i+1].start() if i + 1 < len(sections) else len(content)
            section_content = content[start_pos:end_pos].strip()
            header = match.group(2).lower()

            if "enunciado" in header:
                enunciado = section_content
            elif "solução" in header or "solucao" in header:
                solucao_match = re.search(r'```python(.*?)```', section_content, re.DOTALL)
                if solucao_match:
                    solucao = solucao_match.group(1).strip()
            elif "testes" in header:
                test_content = section_content

    # Extract tests from the test_content
    testes = []
    test_pattern = re.compile(
        r'\*\*Teste (\d+)\*\*\s*Entrada:\s*```(.*?)```\s*Saída:\s*```(.*?)```',
        re.DOTALL
    )
    for match in test_pattern.finditer(test_content):
        numero = match.group(1)
        entrada = match.group(2).strip().replace('\r', '').replace('\n', r'\n')
        saida = match.group(3).strip().replace('\r', '')
        testes.append({
            'numero': numero,
            'entrada': entrada,
            'saida': saida
        })

    return {
        'enunciado': enunciado,
        'solucao': solucao,
        'testes': testes
    }

def create_solution_file(enunciado, solucao, output_path):
    """
    Saves the solution to a .py file with appropriate formatting.
    
    Args:
        enunciado (str): The question statement to be included as a docstring.
        solucao (str): The Python code solution.
        output_path (str or Path): Path where the .py file will be saved.
        
    Raises:
        Exception: If there's an error while writing the file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        if enunciado:
            f.write(f'"""{enunciado}"""\n\n')
        f.write(solucao)
        if not solucao.endswith('\n'):
            f.write('\n')
    logger.info(f"Solution saved to: {output_path}")

def create_tests_file(testes, base_name, folder):
    """
    Saves the test cases to a formatted file.
    
    Args:
        testes (list): List of test dictionaries containing 'numero', 'entrada', and 'saida'.
        base_name (str): Base name for the test file.
        folder (Path): Directory where the test file will be saved.
        
    Raises:
        Exception: If there's an error while writing the file.
    """
    output_path = folder / f"{base_name}_test.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, test in enumerate(testes):
            f.write(f"Test {test['numero']}\n")
            f.write(f"Input: {test['entrada']}\n")
            f.write(f"Output:\n{test['saida']}")
            # Add a newline at the end of the file, but not between tests
            if i < len(testes) - 1:
                f.write("\n")

    logger.info(f"Tests saved to: {output_path}")

def create_test_script(base_name, output_path):
    """
    Generates a robust test runner shell script capable of handling multiline output.
    
    Args:
        base_name (str): Base name of the files (without extension).
        output_path (str or Path): Path where the shell script will be saved.
        
    Raises:
        Exception: If there's an error while writing or setting permissions on the file.
    """
    content_template = """#!/bin/bash

echo "Running tests for {base_name}.py"

PYTHON_FILE=\"{base_name}.py\"
TESTS_FILE=\"{base_name}_test.txt\"

if [ ! -f "$PYTHON_FILE" ] || [ ! -f "$TESTS_FILE" ]; then
  echo "❌ Required files not found!"
  exit 1
fi

total=0
passed=0

# Read the entire test file into a variable
mapfile -t test_lines < "$TESTS_FILE"

current_test_num=0

for i in "${!test_lines[@]}"; do
  line="${test_lines[$i]}"

  if [[ "$line" =~ ^Test ]]; then
    # Start of a new test case
    current_test_num=$((current_test_num + 1))
    test_name="$line"
    
    # The next line is the input
    input_line="${test_lines[$((i + 1))]}"
    input_data="${input_line#Input: }"
    
    # The rest of the lines until the next test are the expected output
    expected_output=""
    j=$((i + 3))  # Skip the "Output:" line
    while [ $j -lt ${#test_lines[@]} ]; do
      if [[ "${test_lines[$j]}" =~ ^Test ]]; then
        break
      fi
      expected_output+="${test_lines[$j]}"
      
      # Add newline if not the last line of output
      next_j=$((j + 1))
      if [ $next_j -lt ${#test_lines[@]} ] && ! [[ "${test_lines[$next_j]}" =~ ^Test ]]; then
        expected_output+=$'\n'
      fi
      j=$((j + 1))
    done

    result=$(echo -e "$input_data" | python3 "$PYTHON_FILE" 2>&1)
    exit_code=$?

    if [ $exit_code -ne 0 ]; then
      echo "❌ $test_name: RUNTIME ERROR (code $exit_code)"
      echo "   Error output:"
      echo "   $result"
    else
      if [ "$result" == "$expected_output" ]; then
        echo "✅ $test_name: PASSED"
        ((passed++))
      else
        echo "❌ $test_name: FAILED"
        echo "   Expected: '$expected_output'"
        echo "   Got:      '$result'"
      fi
    fi
    ((total++))
  fi
done

echo ""
echo "Summary: $passed out of $total tests passed."

if [ $passed -eq $total ] && [ $total -gt 0 ]; then
  exit 0
else
  exit 1
fi
"""
    content = content_template.replace("{base_name}", base_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    os.chmod(output_path, 0o755)
    logger.info(f"Test script saved to: {output_path}")

def process_question(txt_file_path):
    """
    Processes a single .txt question file and generates solution, test, and script files.
    
    Args:
        txt_file_path (str or Path): Path to the .txt file containing the question.
        
    Raises:
        ValueError: If no solution or test cases are found in the file.
        Exception: If there's an error during file processing or generation.
    """
    logger.info(f"Processing: {txt_file_path}")
    base = Path(txt_file_path).stem
    folder = Path(txt_file_path).parent

    question_data = parse_question_txt(txt_file_path)

    if not question_data['solucao']:
        raise ValueError("No solution found in the TXT file")
    if not question_data['testes']:
        raise ValueError("No test cases found in the TXT file")

    solution_path = folder / f"{base}.py"
    tests_path = folder / f"{base}_test.txt"
    script_path = folder / f"{base}.sh"

    create_solution_file(question_data['enunciado'], question_data['solucao'], solution_path)
    create_tests_file(question_data['testes'], base, folder)
    create_test_script(base, script_path)

    print(f"\n✅ Files generated successfully:")
    print(f"   📄 Solution: {solution_path}")
    print(f"   🧪 Tests:    {tests_path}")
    print(f"   🚀 Script:   {script_path}")
    print(f"\nTo test, run:")
    print(f"  cd {folder}")
    print(f"  ./{script_path.name}")

def main():
    """
    Automatically processes all .txt files in the 'questions' directory.
    Creates the directory if it doesn't exist and processes each found .txt file.
    
    Raises:
        Exception: If there's an error during directory creation or file processing.
    """
    questions_dir = Path("questions")
    
    # Ensure questions directory exists
    questions_dir.mkdir(exist_ok=True)

    txt_files = list(questions_dir.glob("*.txt"))
    if not txt_files:
        print(f"❌ No .txt files found in the '{questions_dir}' directory.")
        print(f"📁 Directory ready: {questions_dir}")
        return

    print(f"🔍 Found {len(txt_files)} files to process in '{questions_dir}':\n")
    for txt_file in txt_files:
        print(f"📄 Processing: {txt_file.name}")
        try:
            process_question(txt_file)
        except Exception as e:
            logger.error(f"Error while processing {txt_file.name}: {e}")
            print(f"❌ Error in {txt_file.name}: {e}")

if __name__ == "__main__":
    main()