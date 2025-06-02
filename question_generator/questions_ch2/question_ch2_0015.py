"""Crie um programa que solicita ao usuário que digite uma palavra. O programa deve então analisar a palavra e classificá-la de acordo com as seguintes regras:

*   Se a palavra tiver menos de 3 caracteres, imprima: "Palavra muito curta."
*   Se a palavra tiver mais de 10 caracteres, imprima: "Palavra longa."
*   Se a palavra tiver entre 3 e 10 caracteres (inclusive) **E** o primeiro e o último caractere da palavra forem iguais (ignorando maiúsculas/minúsculas), imprima: "Palavra com início e fim iguais."
*   Caso contrário (palavra de 3 a 10 caracteres, mas com início e fim diferentes), imprima: "Palavra padrão.""""

palavra = input("Digite uma palavra: ")

if len(palavra) < 3:
    print("Palavra muito curta.")
elif len(palavra) > 10:
    print("Palavra longa.")
elif palavra[0].lower() == palavra[-1].lower():
    print("Palavra com início e fim iguais.")
else:
    print("Palavra padrão.")
