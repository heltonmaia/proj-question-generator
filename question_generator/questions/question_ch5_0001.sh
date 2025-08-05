#!/bin/bash

echo "Running tests for question_ch5_0001.py"

PYTHON_FILE="/home/hm/Work/github-projects/proj-question-generator/question_generator/questions/question_ch5_0001.py"
TESTS_FILE="/home/hm/Work/github-projects/proj-question-generator/question_generator/questions/question_ch5_0001_test.txt"

if [ ! -f "$PYTHON_FILE" ] || [ ! -f "$TESTS_FILE" ]; then
  echo "❌ Required files not found!"
  exit 1
fi

total=0
passed=0

while IFS= read -r line; do
  if [[ $line =~ ^Test ]]; then
    test_name=$line
    input_data=""
    while IFS= read -r input_line && [[ ! "$input_line" =~ ^Saída: ]]; do
      input_data+="${input_line#Entrada: }\n"
    done
    input_data=$(echo -e "${input_data%\\n}")

    expected_output=""
    while IFS= read -r output_line && [[ ! "$output_line" =~ ^Test ]]; do
      expected_output+="${output_line#Saída: }\n"
    done
    expected_output=$(echo -e "${expected_output%\\n}")

    result=$(echo -e "$input_data" | python3 "$PYTHON_FILE" 2>&1)
    exit_code=$?

    if [ $exit_code -ne 0 ]; then
      echo "❌ $test_name: RUNTIME ERROR (code $exit_code)"
      echo "   Error output:"
      echo "   $result"
    else
      if [[ "$result" == *"$expected_output"* ]]; then
        echo "✅ $test_name: PASSED"
        ((passed++))
      else
        echo "❌ $test_name: FAILED"
        echo "   Expected: '$expected_output'"
        echo "   Got:      '$result'"
      fi
    fi
    ((total++))
    if [[ "$output_line" =~ ^Test ]]; then
      line=$output_line
      continue
    fi
  fi
done < <(cat "$TESTS_FILE"; echo)

echo ""
echo "Summary: $passed out of $total tests passed."

if [ $passed -eq $total ]; then
  exit 0
else
  exit 1
fi
