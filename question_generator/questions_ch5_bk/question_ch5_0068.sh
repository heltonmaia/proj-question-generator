#!/bin/bash

echo "Executando testes para question_ch5_0068.py"

PYTHON_FILE="question_ch5_0068.py"
TESTS_FILE="question_ch5_0068_test.txt"

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
    input_data="${input_line#Input: }"
    IFS= read -r output_line
    expected_output="${output_line#Output: }"

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
