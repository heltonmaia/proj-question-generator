# Python Question Generator

This project generates, tests, and organizes Python programming questions based on online learning material. It uses the Gemini AI model and produces self-contained exercises, including problem statements, solutions, tests, and PDF lists.

---

## 📂 Project Structure Overview

```plaintext
.
├── prompt.md                    # Template for the LLM prompt
├── question_builder.py          # Reads content from a URL and generates question `.txt` files
├── question_solver.py           # Parses a question `.txt` file and produces .py, .sh, and test files
├── question_find_passed.py      # Executes all `.sh` scripts and moves passed questions to a subfolder 
├── create_pdf_all.py            # Builds a final PDF list of questions using ReportLab
├── questions/                   # Folder for generated questions
│   ├── question_ch5_0126.txt    # Example generated question
│   ├── question_ch5_0126.py     # Extracted solution file
│   ├── question_ch5_0126_test.txt # Input/output tests
│   └── question_ch5_0126.sh     # Auto test script
│   └── passed/                  # Auto test script
│       └── question_xxx         # Auto test script
└── config.yml                   # API key and Gemini model configuration

```

# 1. Generate question(s)
python question_builder.py

# 2. Extract and prepare test files
python question_solver.py

# 3. Run tests and filter passed questions
python question_find_passed.py

# 4. Compile passed questions into a PDF list
python create_pdf_all.py


flowchart TD
    A[🌐 Online Material URL] --> B[📄 prompt.md]
    B --> C[🤖 question_builder.py]
    C --> D[📁 questions/*.txt]
    D --> E[🛠️ question_solver.py]
    E --> F[.py, .sh, _test.txt files]
    F --> G[✅ question_find_passed.py]
    G --> H[📂 questions/passed/]
    H --> I[📘 create_pdf_all.py]
    I --> J[🧾 Final PDF]
