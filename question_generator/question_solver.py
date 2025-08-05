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

    # Extract statement
    enunciado_match = re.search(r'#### Enunciado\s*(.*?)(?=\n####|$)', content, re.DOTALL)
    enunciado = enunciado_match.group(1).strip() if enunciado_match else ""

    # Extract solution
    solucao_match = re.search(r'#### Code Solução\s*```python(.*?)```', content, re.DOTALL)
    solucao = solucao_match.group(1).strip() if solucao_match else ""

    # Extract tests
    testes = []
    test_pattern = re.compile(
        r'\*\*Teste (\d+)\*\*\s*Entrada:\s*```(.*?)```\s*Saída:\s*```(.*?)```',
        re.DOTALL
    )
    for match in test_pattern.finditer(content):
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
        output_path (str or Path): Path where the test file will be saved.
        
    Raises:
        Exception: If there's an error while writing the file.
    """
    for test in testes:
        input_path = folder / f"{base_name}_test_{test['numero']}.in"
        output_path = folder / f"{base_name}_test_{test['numero']}.out"
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(test['entrada'].replace(r'\n', '\n'))
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(test['saida'])
    logger.info(f"Tests saved to: {folder}")

def create_test_script(base_name, output_path):
    """
    Generates a robust test runner shell script.
    
    Args:
        base_name (str): Base name of the files (without extension).
        output_path (str or Path): Path where the shell script will be saved.
        
    Raises:
        Exception: If there's an error while writing or setting permissions on the file.
    """
    content = f"""#!/bin/bash

echo "Running tests for {base_name}.py"

PYTHON_FILE="{base_name}.py"

if [ ! -f "$PYTHON_FILE" ]; then
  echo "❌ Required files not found!"
  exit 1
fi

total=0
passed=0

for test_in in {base_name}_test_*.in; do
  test_name="${{test_in%.in}}"
  test_out="{test_name}.out"

  result=$(python3 "$PYTHON_FILE" < "$test_in" 2>&1)
  exit_code=$?
  
  expected_output=$(cat "$test_out")

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
done

echo ""
echo "Summary: $passed out of $total tests passed."

if [ $passed -eq $total ]; then
  exit 0
else
  exit 1
fi
"""
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