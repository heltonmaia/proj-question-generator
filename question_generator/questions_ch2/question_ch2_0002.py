"""Escreva um programa que solicita ao usuário uma nota numérica de um estudante. O programa deve então classificar esta nota de acordo com as seguintes categorias:

*   **A:** 90.0 ou superior
*   **B:** 80.0 a 89.9
*   **C:** 70.0 a 79.9
*   **D:** 60.0 a 69.9
*   **F:** Abaixo de 60.0

Ao final, o programa deve imprimir a nota informada e sua classificação correspondente."""

nota_str = input()
nota = float(nota_str)

classificacao = ""

if nota >= 90.0:
    classificacao = "A"
elif nota >= 80.0:
    classificacao = "B"
elif nota >= 70.0:
    classificacao = "C"
elif nota >= 60.0:
    classificacao = "D"
else:
    classificacao = "F"

print(f"Nota: {nota}")
print(f"Classificação: {classificacao}")
