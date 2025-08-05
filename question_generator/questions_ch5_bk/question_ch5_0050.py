"""Escreva uma função Python chamada `analisar_numeros` que receba uma lista de números (inteiros ou de ponto flutuante) como argumento.

Esta função deve calcular e retornar três valores:
1. O menor número presente na lista.
2. O maior número presente na lista.
3. A média aritmética de todos os números na lista.

No programa principal, solicite ao usuário que insira uma sequência de números separados por espaço. Converta essa sequência em uma lista de números de ponto flflutuante. Em seguida, chame a função `analisar_numeros` com a lista obtida e imprima os resultados (menor valor, maior valor e média) formatados com duas casas decimais para a média."""

def analisar_numeros(lista_de_numeros: list[float]) -> tuple[float, float, float]:
    """
    Calcula o menor, o maior e a média de uma lista de números.

    Args:
        lista_de_numeros (list[float]): Uma lista de números (inteiros ou de ponto flutuante).

    Returns:
        tuple[float, float, float]: Uma tupla contendo (menor_numero, maior_numero, media).
    """
    menor = min(lista_de_numeros)
    maior = max(lista_de_numeros)
    media = sum(lista_de_numeros) / len(lista_de_numeros)
    return menor, maior, media

# Programa principal
entrada_str = input()
numeros_str = entrada_str.split()
lista_de_numeros = [float(num) for num in numeros_str]

menor_valor, maior_valor, media_calculada = analisar_numeros(lista_de_numeros)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Média: {media_calculada:.2f}")
