import subprocess
from pathlib import Path
import shutil

def main():
    questions_dir = Path("questions")
    passed_dir = questions_dir / "passed"
    passed_dir.mkdir(exist_ok=True)

    sh_files = list(questions_dir.glob("*.sh"))
    if not sh_files:
        print("❌ Nenhum script .sh encontrado na pasta 'questions'.")
        return

    print(f"🔍 Executando {len(sh_files)} scripts de teste...\n")

    for sh_file in sh_files:
        base = sh_file.stem  # ex: question_ch2_0001
        print(f"🚀 Testando: {sh_file.name}")

        try:
            result = subprocess.run(
                ["/bin/bash", sh_file.name],     # execução com bash
                cwd=questions_dir,               # executa dentro da pasta questions
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print(f"✅ TODOS os testes passaram para {base}.")

                # Arquivos a mover: .py, .txt, .sh, _test.txt
                for ext in [".py", ".txt", ".sh", "_test.txt"]:
                    file = questions_dir / f"{base}{ext}"
                    if file.exists():
                        shutil.move(str(file), passed_dir / file.name)

            else:
                print(f"❌ Testes FALHARAM para {base}.")
                print(result.stdout.strip())

        except Exception as e:
            print(f"❌ Erro ao executar {sh_file.name}: {e}")

    print("\n🏁 Processamento concluído.")
    print(f"🗂️ Arquivos aprovados foram movidos para: {passed_dir.resolve()}")

if __name__ == "__main__":
    main()
