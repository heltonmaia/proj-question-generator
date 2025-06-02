"""Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma de trás para frente, ignorando maiúsculas e minúsculas.

Escreva um programa que solicita ao usuário que insira uma única palavra. O programa deve então:
1.  Converter a palavra para letras minúsculas para garantir que a comparação seja case-insensitive.
2.  Verificar se a palavra tratada é um palíndromo.
3.  Imprimir uma mensagem clara indicando se a palavra original é ou não um palíndromo."""

palavra_original = input()

# Converte a palavra para minúsculas para ignorar a capitalização
palavra_tratada = palavra_original.lower()

# Inverte a palavra tratada
palavra_invertida = palavra_tratada[::-1]

# Verifica se a palavra tratada é igual à sua versão invertida
if palavra_tratada == palavra_invertida:
    print(f"'{palavra_original}' é um palíndromo.")
else:
    print(f"'{palavra_original}' NÃO é um palíndromo.")
