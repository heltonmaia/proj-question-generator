"""Crie um programa que solicite ao usuário que digite uma palavra. O programa deve então determinar o comprimento dessa palavra e, com base nesse comprimento, classificá-la nas seguintes categorias:

*   Se o comprimento da palavra for menor que 5 caracteres, imprima 'A palavra é curta.'
*   Se o comprimento da palavra for entre 5 e 10 caracteres (inclusive), imprima 'A palavra é de tamanho médio.'
*   Se o comprimento da palavra for maior que 10 caracteres, imprima 'A palavra é longa.'

Utilize a função `len()` para obter o comprimento da string e estruturas condicionais (`if-elif-else`) para realizar a classificação."""

palavra = input()
comprimento = len(palavra)

if comprimento < 5:
    print("A palavra é curta.")
elif 5 <= comprimento <= 10:
    print("A palavra é de tamanho médio.")
else:
    print("A palavra é longa.")
