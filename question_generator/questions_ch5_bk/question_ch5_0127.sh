#!/bin/bash

echo "Running tests for question_ch5_0127.py"

PYTHON_FILE="question_ch5_0127.py"
TESTS_FILE="question_ch5_0127_test.txt"

if [ ! -f "$PYTHON_FILE" ] || [ ! -f "$TESTS_FILE" ]; then
  echo "❌ Required files not found!"
  exit 1
fi

total=0
passed=0

while IFS= read -r line; do
  if [[ $line =~ ^Test ]]; then
    test_name=$line
    IFS= read -r input_line
    input_data="${input_line#Input: }"
    IFS= read -r output_line
    expected_output="${output_line#Output: }"

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
done < "$TESTS_FILE"

echo ""
echo "Summary: $passed out of $total tests passed."

if [ $passed -eq $total ]; then
  exit 0
else
  exit 1
fi
