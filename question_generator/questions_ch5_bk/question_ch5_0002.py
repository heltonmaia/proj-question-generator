"""Desenvolva um programa Python que realize uma análise estatística básica em uma lista de números fornecida. O programa deve conter uma função que receba uma lista de números de ponto flutuante (`float`) como argumento e retorne três valores: o menor valor da lista, o maior valor da lista e a média aritmética de todos os números na lista.

O programa principal deve ser responsável por:
1.  Ler uma única linha de entrada contendo números separados por espaços (ex: `10.5 2.0 8.0 15.0`).
2.  Converter esses números de strings para o tipo `float` e armazená-los em uma lista.
3.  Chamar a função de análise com a lista de números.
4.  Imprimir os resultados na tela, formatando a média aritmética para exibir exatamente duas casas decimais.

Considere que a lista de entrada nunca estará vazia para este exercício."""

def analisar_numeros(lista_numeros: list[float]) -> tuple[float, float, float]:
    """
    Analisa uma lista de números para encontrar o menor, o maior e a média.

    Args:
        lista_numeros (list[float]): Uma lista de números de ponto flutuante.

    Returns:
        tuple[float, float, float]: Uma tupla contendo (menor_valor, maior_valor, media_aritmetica).
    """
    menor = min(lista_numeros)
    maior = max(lista_numeros)
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    
    return menor, maior, media

# Leitura da linha de números e conversão para lista de floats
entrada_str = input()
numeros = [float(x) for x in entrada_str.split()]

# Chamada da função e desempacotamento dos resultados
menor_val, maior_val, media_val = analisar_numeros(numeros)

# Impressão dos resultados formatados
print(f"Menor valor: {menor_val}")
print(f"Maior valor: {maior_val}")
print(f"Média aritmética: {media_val:.2f}")
