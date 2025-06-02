"""Escreva um programa que solicita ao usuário a inserção de um número de ponto flutuante. Em seguida, o programa deve determinar se o número é positivo, negativo ou zero, e exibir a classificação correspondente na tela."""

numero = float(input())

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
