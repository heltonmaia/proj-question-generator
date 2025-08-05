#!/usr/bin/env python3
"""
Python Question Generator - CLI Interface

A command-line interface for the automated Python programming question generator.
This tool provides access to all main functions: generation, processing, testing, and PDF creation.
"""

import sys
import os
import argparse
from pathlib import Path
from typing import Optional

# Add the question_generator package to the path
sys.path.insert(0, str(Path(__file__).parent / "question_generator"))

try:
    from question_builder import generate_question_from_url
    from question_solver import process_question
    from question_find_passed import main as run_tests
    from create_pdf_all import main as create_pdf
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("Make sure you're running this from the project root directory.")
    sys.exit(1)


class QuestionGeneratorCLI:
    """Command-line interface for the Python Question Generator."""
    
    def __init__(self):
        self.questions_dir = Path("question_generator/questions")
        self.default_url = "https://heltonmaia.com/pythonbook/chapters/ch5/ch5.html"
        self.current_working_dir = self.questions_dir
        
        # Ensure default directory exists
        self.questions_dir.mkdir(parents=True, exist_ok=True)
    
    def print_banner(self):
        """Display the application banner."""
        print("=" * 60)
        print("🐍 Python Question Generator CLI")
        print("=" * 60)
        print("Automated generation, testing, and documentation of Python exercises")
        print("=" * 60)
        print(f"📁 Default questions directory: {self.questions_dir}")
        if not self.questions_dir.exists():
            print("⚠️  Default directory will be created when needed")
        print("=" * 60)
    
    def print_menu(self):
        """Display the main menu options."""
        print(f"\n📁 Current working directory: {self.current_working_dir}")
        print(f"📁 Default questions directory: {self.questions_dir}")
        print("\n📋 Available Options:")
        print("1.  Generate a single question")
        print("2.  Generate multiple questions (batch)")
        print("3.  Process all question files")
        print("4.  Run tests and filter passed questions")
        print("5.  Create PDF from passed questions")
        print("6.  Full pipeline (generate → process → test → PDF)")
        print("7.  Show project status")
        print("8.  Setup configuration")
        print("9.  Change working directory")
        print("10. Exit")
        print("-" * 60)
    
    def get_user_choice(self) -> str:
        """Get user input for menu selection."""
        while True:
            try:
                choice = input("Enter your choice (1-10): ").strip()
                if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                    return choice
                else:
                    print("❌ Invalid choice. Please enter a number between 1-10.")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
    
    def check_config(self):
        """Check if configuration file exists and is properly set up."""
        config_path = Path("config.yml")
        if not config_path.exists():
            print("❌ Configuration file 'config.yml' not found!")
            print("\n📝 Please create a config.yml file with your Gemini API key:")
            print("""
gemini:
  api_key: "your-actual-api-key-here"
  model: "gemini-2.5-flash-preview-05-20"
            """)
            print("🔑 Get your API key from: https://makersuite.google.com/app/apikey")
            return False
        
        # Check if API key is set
        try:
            import yaml
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            
            api_key = config.get('gemini', {}).get('api_key')
            if not api_key or api_key == "your-api-key-here":
                print("❌ Please set your actual Gemini API key in config.yml")
                print("🔑 Get your API key from: https://makersuite.google.com/app/apikey")
                return False
            
            return True
        except Exception as e:
            print(f"❌ Error reading config.yml: {e}")
            return False

    def select_directory(self) -> Path:
        """Let user select a directory for saving files."""
        print("\n📁 Directory Selection:")
        print(f"1. Use current directory: {Path.cwd()}")
        print(f"2. Use default questions directory: {self.questions_dir}")
        print("3. Enter custom path")
        
        while True:
            try:
                choice = input("Choose option (1-3): ").strip()
                if choice == '1':
                    return Path.cwd()
                elif choice == '2':
                    # Ensure default directory exists
                    self.questions_dir.mkdir(parents=True, exist_ok=True)
                    print(f"✅ Using default directory: {self.questions_dir}")
                    return self.questions_dir
                elif choice == '3':
                    custom_path = input("Enter custom directory path: ").strip()
                    path = Path(custom_path)
                    if not path.exists():
                        create = input(f"Directory '{path}' doesn't exist. Create it? (y/N): ").strip().lower()
                        if create == 'y':
                            path.mkdir(parents=True, exist_ok=True)
                            print(f"✅ Created directory: {path}")
                        else:
                            continue
                    return path
                else:
                    print("❌ Invalid choice. Please enter 1, 2, or 3.")
            except KeyboardInterrupt:
                return self.questions_dir

    def generate_single_question(self):
        """Generate a single question."""
        print("\n🎯 Generating a single question...")
        
        # Check configuration first
        if not self.check_config():
            return
        
        # Select directory
        target_dir = self.select_directory()
        print(f"📁 Files will be saved to: {target_dir}")
        
        # Get question number
        while True:
            try:
                question_num = input("Enter question number (e.g., 0131): ").strip()
                if question_num.isdigit() and len(question_num) <= 4:
                    question_num = question_num.zfill(4)
                    break
                else:
                    print("❌ Please enter a valid number (1-9999).")
            except KeyboardInterrupt:
                return
        
        output_filename = f"question_ch5_{question_num}"
        
        try:
            print(f"🔄 Generating question {question_num}...")
            
            # Temporarily change working directory for generation
            original_cwd = os.getcwd()
            os.chdir(target_dir)
            
            generate_question_from_url(self.default_url, output_file=output_filename)
            
            # Return to original directory
            os.chdir(original_cwd)
            
            print(f"✅ Question {question_num} generated successfully in {target_dir}!")
        except Exception as e:
            print(f"❌ Error generating question: {e}")
            # Ensure we return to original directory on error
            os.chdir(original_cwd)
    
    def generate_batch_questions(self, start_num: Optional[int] = None, end_num: Optional[int] = None):
        """Generate multiple questions in batch."""
        print("\n🔄 Batch question generation...")

        if not self.check_config():
            return

        target_dir = self.questions_dir
        print(f"📁 Files will be saved to: {target_dir}")

        if start_num is None or end_num is None:
            last_question_num = 0
            for f in target_dir.glob("question_ch5_*.txt"):
                try:
                    num = int(f.stem.split("_")[-1])
                    if num > last_question_num:
                        last_question_num = num
                except ValueError:
                    continue
            
            start_num = last_question_num + 1
            end_num = last_question_num + 10

        print(f"🚀 Generating questions {start_num} to {end_num}...")

        original_cwd = os.getcwd()
        os.chdir(target_dir)

        try:
            for i in range(start_num, end_num + 1):
                try:
                    output_filename = f"question_ch5_{i:04d}"
                    print(f"📝 Generating question {i}/{end_num}...")
                    generate_question_from_url(self.default_url, output_file=output_filename)
                    print(f"✅ Question {i} completed!")
                except Exception as e:
                    print(f"❌ Error generating question {i}: {e}")
                    continue
        finally:
            os.chdir(original_cwd)

    def process_questions(self, target_dir: Optional[Path] = None):
        """Process all question files."""
        print("\n🔧 Processing question files...")

        if target_dir is None:
            target_dir = self.questions_dir

        if not target_dir.exists():
            print(f"❌ Directory not found: {target_dir}")
            return

        txt_files = [f for f in target_dir.glob("*.txt") if "_test" not in f.name]
        if not txt_files:
            print(f"❌ No .txt files found in {target_dir}")
            return

        print(f"📁 Found {len(txt_files)} question files to process in {target_dir}...")

        original_cwd = os.getcwd()
        os.chdir(target_dir)

        try:
            for txt_file in txt_files:
                try:
                    print(f"🔄 Processing {txt_file.name}...")
                    process_question(txt_file.name)
                    print(f"✅ {txt_file.name} processed successfully!")
                except Exception as e:
                    print(f"❌ Error processing {txt_file.name}: {e}")
        finally:
            os.chdir(original_cwd)

    def run_quality_tests(self, target_dir: Optional[Path] = None):
        """Run tests and filter passed questions."""
        print("\n🧪 Running quality tests...")

        if target_dir is None:
            target_dir = self.questions_dir

        if not target_dir.exists():
            print(f"❌ Directory not found: {target_dir}")
            return

        sh_files = list(target_dir.glob("*.sh"))
        if not sh_files:
            print(f"❌ No .sh test files found in {target_dir}")
            print("Make sure to process questions first to generate test files.")
            return

        print(f"🧪 Found {len(sh_files)} test files to run in {target_dir}...")

        try:
            original_cwd = os.getcwd()
            os.chdir(target_dir)

            run_tests()

            os.chdir(original_cwd)
            print("✅ Quality tests completed!")
        except Exception as e:
            print(f"❌ Error running tests: {e}")
            os.chdir(original_cwd)

    def create_pdf_documentation(self):
        """Create PDF from passed questions."""
        print("\n📄 Creating PDF documentation...")

        passed_dir = self.questions_dir / "passed"
        if not passed_dir.exists() or not any(passed_dir.iterdir()):
            print("❌ No passed questions found. Run tests first.")
            return

        try:
            create_pdf()
            print("✅ PDF created successfully!")
        except Exception as e:
            print(f"❌ Error creating PDF: {e}")

    def run_full_pipeline(self):
        """Run the complete pipeline non-interactively."""
        print("\n🚀 Running full pipeline...")
        
        print("1. Generating questions...")
        self.generate_batch_questions()

        print("2. Processing questions...")
        self.process_questions(self.questions_dir)

        print("3. Running quality tests...")
        self.run_quality_tests(self.questions_dir)

        print("4. Creating PDF...")
        self.create_pdf_documentation()

        print("\n🎉 Full pipeline completed!")
    
    def show_project_status(self):
        """Show current project status."""
        print("\n📊 Project Status:")
        print("-" * 40)
        
        # Check configuration status
        config_status = "✅ Configured" if self.check_config() else "❌ Not configured"
        print(f"🔧 Configuration: {config_status}")
        
        # Show default directory status
        print(f"📁 Default questions directory: {self.questions_dir}")
        if self.questions_dir.exists():
            default_txt = len(list(self.questions_dir.glob("*.txt")))
            default_py = len(list(self.questions_dir.glob("*.py")))
            default_sh = len(list(self.questions_dir.glob("*.sh")))
            default_test = len(list(self.questions_dir.glob("*_test.txt")))
            
            passed_dir = self.questions_dir / "passed"
            if passed_dir.exists():
                default_passed = len(list(passed_dir.glob("*.txt")))
            else:
                default_passed = 0
            
            print(f"   📁 Total questions: {default_txt}")
            print(f"   🐍 Solution files: {default_py}")
            print(f"   🧪 Test runners: {default_sh}")
            print(f"   📋 Test files: {default_test}")
            print(f"   ✅ Passed questions: {default_passed}")
            
            if default_txt > 0:
                completion_rate = (default_py / default_txt) * 100
                print(f"   📈 Processing completion: {completion_rate:.1f}%")
            
            if default_py > 0:
                pass_rate = (default_passed / default_py) * 100
                print(f"   🎯 Quality pass rate: {pass_rate:.1f}%")
        else:
            print("   ❌ Default directory not found (will be created when needed)")
        
        # Show status for current working directory if different from default
        if self.current_working_dir != self.questions_dir:
            print(f"\n📁 Current working directory: {self.current_working_dir}")
            
            if not self.current_working_dir.exists():
                print("❌ Current working directory not found.")
                return
            
            # Count files by type in current working directory
            txt_files = len(list(self.current_working_dir.glob("*.txt")))
            py_files = len(list(self.current_working_dir.glob("*.py")))
            sh_files = len(list(self.current_working_dir.glob("*.sh")))
            test_files = len(list(self.current_working_dir.glob("*_test.txt")))
            
            passed_dir = self.current_working_dir / "passed"
            if passed_dir.exists():
                passed_files = len(list(passed_dir.glob("*.txt")))
            else:
                passed_files = 0
            
            print(f"   📁 Total questions: {txt_files}")
            print(f"   🐍 Solution files: {py_files}")
            print(f"   🧪 Test runners: {sh_files}")
            print(f"   📋 Test files: {test_files}")
            print(f"   ✅ Passed questions: {passed_files}")
            
            if txt_files > 0:
                completion_rate = (py_files / txt_files) * 100
                print(f"   📈 Processing completion: {completion_rate:.1f}%")
            
            if py_files > 0:
                pass_rate = (passed_files / py_files) * 100
                print(f"   🎯 Quality pass rate: {pass_rate:.1f}%")

    def setup_configuration(self):
        """Interactive configuration setup."""
        print("\n🔧 Configuration Setup")
        print("-" * 40)
        
        config_path = Path("config.yml")
        
        if config_path.exists():
            print("📁 Configuration file already exists.")
            overwrite = input("Do you want to overwrite it? (y/N): ").strip().lower()
            if overwrite != 'y':
                print("Configuration setup cancelled.")
                return
        
        print("\n🔑 You need a Gemini API key to generate questions.")
        print("Get your API key from: https://makersuite.google.com/app/apikey")
        print("\nEnter your Gemini API key:")
        
        api_key = input("API Key: ").strip()
        
        if not api_key:
            print("❌ API key cannot be empty.")
            return
        
        # Create config file
        config_content = f"""# Configuration file for Python Question Generator
# Generated by CLI setup

gemini:
  api_key: "{api_key}"
  model: "gemini-2.5-flash-preview-05-20"
"""
        
        try:
            with open(config_path, 'w') as f:
                f.write(config_content)
            print("✅ Configuration file created successfully!")
            print(f"📁 Location: {config_path.absolute()}")
        except Exception as e:
            print(f"❌ Error creating configuration file: {e}")

    def change_working_directory(self):
        """Change the current working directory for operations."""
        print("\n📁 Change Working Directory")
        print("-" * 40)
        
        new_dir = self.select_directory()
        self.current_working_dir = new_dir
        print(f"✅ Working directory changed to: {self.current_working_dir}")
    
    def run(self):
        """Main CLI loop."""
        self.print_banner()
        
        while True:
            self.print_menu()
            choice = self.get_user_choice()
            
            if choice == '1':
                self.generate_single_question()
            elif choice == '2':
                self.generate_batch_questions()
            elif choice == '3':
                self.process_questions()
            elif choice == '4':
                self.run_quality_tests()
            elif choice == '5':
                self.create_pdf_documentation()
            elif choice == '6':
                self.run_full_pipeline()
            elif choice == '7':
                self.show_project_status()
            elif choice == '8':
                self.setup_configuration()
            elif choice == '9':
                self.change_working_directory()
            elif choice == '10':
                print("\n👋 Thank you for using Python Question Generator!")
                break
            
            input("\nPress Enter to continue...")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Python Question Generator CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py                    # Interactive menu
  python app.py --generate 5       # Generate question #5
  python app.py --batch 1 10       # Generate questions 1-10
  python app.py --process          # Process all questions
  python app.py --test             # Run quality tests
  python app.py --pdf              # Create PDF
  python app.py --pipeline         # Run full pipeline
  python app.py --status           # Show project status
        """
    )
    
    parser.add_argument('--generate', type=int, help='Generate a single question by number')
    parser.add_argument('--batch', nargs=2, type=int, metavar=('START', 'END'), 
                       help='Generate questions in batch range')
    parser.add_argument('--process', action='store_true', help='Process all question files')
    parser.add_argument('--test', action='store_true', help='Run quality tests')
    parser.add_argument('--pdf', action='store_true', help='Create PDF documentation')
    parser.add_argument('--pipeline', action='store_true', help='Run full pipeline')
    parser.add_argument('--status', action='store_true', help='Show project status')
    
    args = parser.parse_args()
    
    cli = QuestionGeneratorCLI()
    
    # Handle command-line arguments
    if args.generate:
        cli.generate_single_question()
    elif args.batch:
        cli.generate_batch_questions()
    elif args.process:
        cli.process_questions()
    elif args.test:
        cli.run_quality_tests()
    elif args.pdf:
        cli.create_pdf_documentation()
    elif args.pipeline:
        cli.run_full_pipeline()
    elif args.status:
        cli.show_project_status()
    else:
        # No arguments provided, run interactive mode
        cli.run()


if __name__ == "__main__":
    main()
