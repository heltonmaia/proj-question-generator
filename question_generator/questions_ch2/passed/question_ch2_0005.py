"""Escreva um programa que solicita ao usuário que insira uma pontuação numérica (um número inteiro). O programa deve então classificar essa pontuação de acordo com as seguintes regras e imprimir a classificação correspondente:

*   Se a pontuação for menor que 0 ou maior que 100, a classificação é "Pontuação inválida.".
*   Se a pontuação for maior que 90 (e menor ou igual a 100), a classificação é "Excelente".
*   Se a pontuação for maior que 70 (e menor ou igual a 90), a classificação é "Bom".
*   Se a pontuação for maior que 50 (e menor ou igual a 70), a classificação é "Aprovado".
*   Se a pontuação for menor ou igual a 50 (e maior ou igual a 0), a classificação é "Reprovado".

Considere que a entrada do usuário será sempre um número inteiro."""

pontuacao_str = input()
pontuacao = int(pontuacao_str)

if pontuacao < 0 or pontuacao > 100:
    print("Pontuação inválida.")
elif pontuacao > 90:
    print("Excelente")
elif pontuacao > 70:
    print("Bom")
elif pontuacao > 50:
    print("Aprovado")
else:
    print("Reprovado")
