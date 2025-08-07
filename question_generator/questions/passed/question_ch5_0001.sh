#!/bin/bash

echo "Running tests for question_ch5_0001.py"

PYTHON_FILE="question_ch5_0001.py"
TESTS_FILE="question_ch5_0001_test.txt"

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
        expected_output+=$'
'
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
