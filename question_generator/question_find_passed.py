import subprocess
from pathlib import Path
import shutil

def main():
    questions_dir = Path("questions_ch5")
    passed_dir = questions_dir / "passed"
    passed_dir.mkdir(exist_ok=True)

    sh_files = list(questions_dir.glob("*.sh"))
    if not sh_files:
        print("❌ No .sh scripts found in the 'questions' directory.")
        return

    print(f"🔍 Running {len(sh_files)} test scripts...\n")

    for sh_file in sh_files:
        base = sh_file.stem  # e.g., question_ch2_0001
        print(f"🚀 Testing: {sh_file.name}")

        try:
            result = subprocess.run(
                ["/bin/bash", sh_file.name],     # execute using bash
                cwd=questions_dir,               # run inside the questions directory
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print(f"✅ ALL tests passed for {base}.")

                # Files to move: .py, .txt, .sh, _test.txt
                for ext in [".py", ".txt", ".sh", "_test.txt"]:
                    file = questions_dir / f"{base}{ext}"
                    if file.exists():
                        shutil.move(str(file), passed_dir / file.name)

            else:
                print(f"❌ Tests FAILED for {base}.")
                print(result.stdout.strip())

        except Exception as e:
            print(f"❌ Error running {sh_file.name}: {e}")

    print("\n🏁 Processing completed.")
    print(f"🗂️ Approved files have been moved to: {passed_dir.resolve()}")

if __name__ == "__main__":
    main()
