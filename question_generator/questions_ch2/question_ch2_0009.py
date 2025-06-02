"""Escreva um programa que solicite ao usuário que insira uma palavra ou frase. Em seguida, o programa deve imprimir o comprimento da string, a primeira letra da string, a última letra da string e a string invertida."""

texto = input()

# Imprime o comprimento da string
print(len(texto))

# Imprime a primeira letra da string
print(texto[0])

# Imprime a última letra da string
print(texto[-1])

# Imprime a string invertida usando slicing
print(texto[::-1])
