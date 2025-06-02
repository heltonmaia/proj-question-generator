import os
import re
from pathlib import Path
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_question_txt(txt_file_path):
    """Extrai o enunciado, a solução e os testes de um arquivo gerado pelo gerador Markdown."""
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extrair Enunciado
    enunciado_match = re.search(r'#### Enunciado\s*(.*?)(?=\n####|$)', content, re.DOTALL)
    enunciado = enunciado_match.group(1).strip() if enunciado_match else ""

    # Extrair Solução
    solucao_match = re.search(r'#### Code Solução\s*```python(.*?)```', content, re.DOTALL)
    solucao = solucao_match.group(1).strip() if solucao_match else ""

    # Extrair Testes
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
    """Salva a solução em um arquivo .py com formatação adequada."""
    with open(output_path, 'w', encoding='utf-8') as f:
        if enunciado:
            f.write(f'"""{enunciado}"""\n\n')
        f.write(solucao)
        if not solucao.endswith('\n'):
            f.write('\n')
    logger.info(f"Solução salva em: {output_path}")

def create_tests_file(testes, output_path):
    """Salva os testes em um arquivo formatado."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for test in testes:
            f.write(f"Teste {test['numero']}:\n")
            f.write(f"Input: {test['entrada']}\n")
            f.write(f"Output: {test['saida']}\n")
            if test != testes[-1]:
                f.write("\n")
    logger.info(f"Testes salvos em: {output_path}")

def create_test_script(base_name, output_path):
    """Gera um script de teste automatizado robusto."""
    content = f"""#!/bin/bash

echo "Executando testes para {base_name}.py"

PYTHON_FILE="{base_name}.py"
TESTS_FILE="{base_name}_test.txt"

if [ ! -f "$PYTHON_FILE" ] || [ ! -f "$TESTS_FILE" ]; then
  echo "❌ Arquivos necessários não encontrados!"
  exit 1
fi

total=0
passed=0

while IFS= read -r line; do
  if [[ $line =~ ^Teste ]]; then
    test_name=$line
    IFS= read -r input_line
    input_data="${{input_line#Input: }}"
    IFS= read -r output_line
    expected_output="${{output_line#Output: }}"

    result=$(echo -e "$input_data" | python3 "$PYTHON_FILE" 2>&1)
    exit_code=$?

    if [ $exit_code -ne 0 ]; then
      echo "❌ $test_name: ERRO NA EXECUÇÃO (código $exit_code)"
      echo "   Saída do erro:"
      echo "   $result"
    else
      if [ "$result" == "$expected_output" ]; then
        echo "✅ $test_name: PASSOU"
        ((passed++))
      else
        echo "❌ $test_name: FALHOU"
        echo "   Esperado: '$expected_output'"
        echo "   Obtido:   '$result'"
      fi
    fi
    ((total++))
  fi
done < "$TESTS_FILE"

echo ""
echo "Resumo: $passed de $total testes passaram."

if [ $passed -eq $total ]; then
  exit 0
else
  exit 1
fi
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    os.chmod(output_path, 0o755)
    logger.info(f"Script de testes salvo em: {output_path}")

def process_question(txt_file_path):
    """Processa um único arquivo de questão .txt."""
    logger.info(f"Processando: {txt_file_path}")
    base = Path(txt_file_path).stem
    folder = Path(txt_file_path).parent

    question_data = parse_question_txt(txt_file_path)

    if not question_data['solucao']:
        raise ValueError("Nenhuma solução encontrada no arquivo TXT")
    if not question_data['testes']:
        raise ValueError("Nenhum caso de teste encontrado no arquivo TXT")

    solution_path = folder / f"{base}.py"
    tests_path = folder / f"{base}_test.txt"
    script_path = folder / f"{base}.sh"

    create_solution_file(question_data['enunciado'], question_data['solucao'], solution_path)
    create_tests_file(question_data['testes'], tests_path)
    create_test_script(base, script_path)

    print(f"\n✅ Arquivos gerados com sucesso:")
    print(f"   📄 Solução: {solution_path}")
    print(f"   🧪 Testes:  {tests_path}")
    print(f"   🚀 Script:  {script_path}")
    print(f"\nPara testar, execute:")
    print(f"  cd {folder}")
    print(f"  ./{script_path.name}")

def main():
    """Processa automaticamente todos os arquivos .txt na pasta 'questions'."""
    questions_dir = Path("questions")

    if not questions_dir.exists():
        questions_dir.mkdir()
        print(f"📁 Pasta criada: {questions_dir}")
        print("Por favor, coloque seus arquivos .txt na pasta 'questions' e execute novamente.")
        return

    txt_files = list(questions_dir.glob("*.txt"))
    if not txt_files:
        print("❌ Nenhum arquivo .txt encontrado na pasta 'questions'.")
        return

    print(f"🔍 Encontrados {len(txt_files)} arquivos para processar em '{questions_dir}':\n")
    for txt_file in txt_files:
        print(f"📄 Processando: {txt_file.name}")
        try:
            process_question(txt_file)
        except Exception as e:
            logger.error(f"Erro ao processar {txt_file.name}: {e}")
            print(f"❌ Erro em {txt_file.name}: {e}")

if __name__ == "__main__":
    main()
