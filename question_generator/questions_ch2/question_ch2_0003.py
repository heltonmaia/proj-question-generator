"""Crie um programa que solicita ao usuário duas palavras distintas. Em seguida, o programa deve realizar as seguintes operações e exibir os resultados:

1.  Converter a **primeira palavra** para letras maiúsculas.
2.  Converter a **segunda palavra** para letras minúsculas.
3.  Concatenar a primeira palavra (agora em maiúsculas) com a segunda palavra (agora em minúsculas).
4.  Verificar se o comprimento da string concatenada é **par ou ímpar** e exibir essa informação.
5.  Apresentar todos os resultados de forma clara."""

palavra1 = input()
palavra2 = input()

palavra1_maiusculas = palavra1.upper()
palavra2_minusculas = palavra2.lower()

concatenada = palavra1_maiusculas + palavra2_minusculas
comprimento_concatenada = len(concatenada)

paridade = "par" if comprimento_concatenada % 2 == 0 else "ímpar"

print(f"Primeira palavra em maiúsculas: {palavra1_maiusculas}")
print(f"Segunda palavra em minúsculas: {palavra2_minusculas}")
print(f"Strings concatenadas: {concatenada}")
print(f"Comprimento da string concatenada: {comprimento_concatenada} ({paridade})")
