"""Escreva uma função Python chamada `analisar_lista_numerica` que receba uma lista de números inteiros (`list[int]`) como entrada. A função deve calcular e retornar uma tupla contendo cinco valores, na seguinte ordem:

1.  A soma de todos os números na lista.
2.  A quantidade de números pares na lista.
3.  A quantidade de números ímpares na lista.
4.  O menor valor presente na lista.
5.  O maior valor presente na lista.

Considere que a lista de entrada sempre conterá pelo menos um número. Utilize type hints para os parâmetros e o retorno da função.

Seu programa principal deve ler uma linha de números inteiros separados por espaço, convertê-los em uma lista e, em seguida, usar a função `analisar_lista_numerica` para obter as informações solicitadas. Finalmente, imprima os resultados de forma clara, como demonstrado nos exemplos de saída."""

from typing import List, Tuple

def analisar_lista_numerica(numeros: List[int]) -> Tuple[int, int, int, int, int]:
    """
    Analisa uma lista de números inteiros, retornando sua soma,
    contagem de pares e ímpares, e os valores mínimo e máximo.

    Args:
        numeros (list[int]): Uma lista de números inteiros não vazia.

    Returns:
        tuple[int, int, int, int, int]: Uma tupla contendo:
            - A soma de todos os números.
            - A quantidade de números pares.
            - A quantidade de números ímpares.
            - O menor valor da lista.
            - O maior valor da lista.
    """
    soma_total = sum(numeros)
    pares = 0
    impares = 0
    
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    menor_valor = min(numeros)
    maior_valor = max(numeros)
            
    return soma_total, pares, impares, menor_valor, maior_valor

# Leitura da entrada: uma linha de números separados por espaço
entrada_str = input()
numeros_str = entrada_str.split()
numeros_int = [int(num) for num in numeros_str]

# Chamada da função e desempacotamento dos resultados
soma, pares, impares, menor, maior = analisar_lista_numerica(numeros_int)

# Impressão dos resultados
print(f"Soma da lista: {soma}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
