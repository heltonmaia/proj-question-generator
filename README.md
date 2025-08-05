# Python Question Generator

This project generates, tests, and organizes Python programming questions based on online learning material. It uses the Gemini AI model and produces self-contained exercises, including problem statements, solutions, tests, and PDF lists.

## 🎯 Features

- **🤖 AI-Powered Generation**: Uses Google Gemini AI to create educational programming questions
- **📚 Educational Focus**: Generates questions for beginner to intermediate Python learners
- **🧪 Automated Testing**: Built-in test runner with comprehensive test cases
- **📊 Quality Control**: Filters questions that pass all tests automatically
- **📄 PDF Generation**: Creates professional PDF documentation of exercises
- **🌐 Web Scraping**: Extracts content from online learning materials
- **🔄 Batch Processing**: Generates multiple questions in sequence

## 🛠️ Requirements

- **Python 3.10+**
- **Google Gemini API Key**
- **Internet connection** (for web scraping and AI generation)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd proj-question-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key**
   
   **Option A: Interactive Setup (Recommended)**
   ```bash
   python app.py
   # Choose option 8: Setup configuration
   ```
   
   **Option B: Manual Setup**
   Create a `config.yml` file in the project root:
   ```yaml
   gemini:
     api_key: "your-gemini-api-key-here"
     model: "gemini-2.5-flash-preview-05-20"
   ```
   
   **Get your API key from:** https://makersuite.google.com/app/apikey

## 🚀 Quick Start

### Option 1: Interactive CLI (Recommended)
```bash
python app.py
```
This launches an interactive menu with all available options.

### Option 2: Command Line Arguments
```bash
# Generate a single question
python app.py --generate 5

# Generate questions in batch
python app.py --batch 1 10

# Process all question files
python app.py --process

# Run quality tests
python app.py --test

# Create PDF documentation
python app.py --pdf

# Run full pipeline
python app.py --pipeline

# Show project status
python app.py --status
```

### Option 3: Individual Scripts
1. **Generate question(s)**
   ```bash
   python question_generator/question_builder.py
   ```

2. **Extract and prepare test files**
   ```bash
   python question_generator/question_solver.py
   ```

3. **Run tests and filter passed questions**
   ```bash
   python question_generator/question_find_passed.py
   ```

4. **Compile passed questions into a PDF list**
   ```bash
   python question_generator/create_pdf_all.py
   ```

## 📂 Project Structure Overview

```plaintext
proj-question-generator/
├── README.md                           # Project documentation
├── pyproject.toml                      # Python project configuration
├── requirements.txt                    # Python dependencies
├── .gitignore                         # Git ignore patterns
├── app.py                             # CLI interface for all operations
├── question_generator/                 # Main package directory
│   ├── __init__.py                    # Package initialization
│   ├── prompt.md                      # Template for the LLM prompt
│   ├── question_builder.py            # Reads content from URL and generates question .txt files
│   ├── question_solver.py             # Parses question .txt files and produces .py, .sh, and test files
│   ├── question_find_passed.py        # Executes all .sh scripts and moves passed questions to subfolder
│   ├── create_pdf_all.py              # Builds final PDF list of questions using ReportLab
│   └── questions/                     # Default directory for generated questions
│       ├── passed/                    # Questions that passed all tests
│       │   ├── question_ch5_0001.py   # Solution file
│       │   ├── question_ch5_0001.sh   # Test runner script
│       │   ├── question_ch5_0001.txt  # Original question file
│       │   └── question_ch5_0001_test.txt # Test cases
│       ├── question_ch5_0126.py       # Example solution file
│       ├── question_ch5_0126.sh       # Example test runner
│       ├── question_ch5_0126.txt      # Example question file
│       └── question_ch5_0126_test.txt # Example test cases
└── config.yml                         # API key and Gemini model configuration (not in repo)
```

## 🔧 How It Works

### 1. Question Generation (`question_builder.py`)
- Fetches content from specified URL using BeautifulSoup
- Uses Gemini AI with structured prompt template
- Generates questions in Portuguese with educational focus
- Saves questions as structured `.txt` files

### 2. Question Processing (`question_solver.py`)
- Parses generated `.txt` files using regex patterns
- Extracts problem statement, solution code, and test cases
- Creates separate files for each component:
  - `.py` - Python solution code
  - `_test.txt` - Test cases (input/output pairs)
  - `.sh` - Automated test runner script

### 3. Quality Control (`question_find_passed.py`)
- Executes all test scripts using bash
- Validates solutions against test cases
- Moves passing questions to `passed/` subfolder
- Filters out questions with errors or incorrect solutions

### 4. Documentation (`create_pdf_all.py`)
- Compiles all passed questions into professional PDF
- Uses ReportLab for formatting and styling
- Creates comprehensive exercise list with proper formatting

## 📝 Question Format

Each generated question follows this structure:

```markdown
#### Enunciado
[Problem description in Portuguese]

#### Code Solução
```python
[Python solution code]
```

#### Testes
**Teste 1**
Entrada:
```
[Input data]
```
Saída:
```
[Expected output]
```
```

## 🧪 Testing System

- **Automated Test Runner**: Bash scripts execute Python solutions
- **Input/Output Validation**: Compares actual vs expected output
- **Error Handling**: Catches runtime errors and syntax issues
- **Multiple Test Cases**: Each question includes 3-4 test scenarios
- **Edge Case Testing**: Includes boundary conditions and error cases

## 📊 Current Status

- **Generated Questions**: 130+ questions for Chapter 5
- **Question Range**: `question_ch5_0001` to `question_ch5_0130`
- **Quality Control**: Automatic filtering of passing questions
- **Documentation**: PDF generation for approved exercises

## 🔑 Configuration

The system uses a `config.yml` file for configuration:

```yaml
gemini:
  api_key: "your-api-key-here"
  model: "gemini-2.5-flash-preview-05-20"
```

## 🛠️ Dependencies

Key dependencies include:
- `google-generativeai` - Gemini AI integration
- `beautifulsoup4` - Web scraping
- `reportlab` - PDF generation
- `pyyaml` - Configuration management
- `requests` - HTTP requests

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for question generation capabilities
- BeautifulSoup for web scraping functionality
- ReportLab for PDF generation features
