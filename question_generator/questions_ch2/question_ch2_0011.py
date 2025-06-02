"""Crie um programa que solicite ao usuário a inserção de três notas (valores de ponto flutuante). O programa deve calcular a média aritmética dessas notas e, em seguida, classificar o desempenho do aluno com base na média, atribuindo uma letra de acordo com as seguintes regras:

*   **Média maior ou igual a 9.0:** Classificação "A"
*   **Média maior ou igual a 7.0 e menor que 9.0:** Classificação "B"
*   **Média maior ou igual a 5.0 e menor que 7.0:** Classificação "C"
*   **Média maior ou igual a 3.0 e menor que 5.0:** Classificação "D"
*   **Média menor que 3.0:** Classificação "F"

A saída deve exibir a média calculada (formatada com duas casas decimais) e a letra correspondente à classificação."""

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if media >= 9.0:
    classificacao = "A"
elif media >= 7.0:
    classificacao = "B"
elif media >= 5.0:
    classificacao = "C"
elif media >= 3.0:
    classificacao = "D"
else:
    classificacao = "F"

print(f"Média: {media:.2f}")
print(f"Classificação: {classificacao}")
