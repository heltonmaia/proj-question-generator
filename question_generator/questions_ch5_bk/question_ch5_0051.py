"""Desenvolva uma função em Python chamada `analisar_numeros` que receba uma lista de números inteiros como parâmetro. Esta função deve percorrer a lista e calcular três informações essenciais:
1.  A quantidade total de números pares presentes na lista.
2.  A quantidade total de números ímpares presentes na lista.
3.  A soma de todos os números contidos na lista.

A função `analisar_numeros` deve retornar esses três valores como uma tupla, seguindo a ordem específica: `(quantidade_pares, quantidade_impares, soma_total)`.

No programa principal, você deverá ler uma única linha de entrada que conterá números inteiros separados por espaço. Converta esses números lidos em uma lista de inteiros e então chame a função `analisar_numeros` com essa lista. Por fim, imprima os resultados obtidos pela função de forma clara e formatada, indicando a quantidade de números pares, a quantidade de números ímpares e a soma total."""

from typing import List, Tuple

def analisar_numeros(lista_de_numeros: List[int]) -> Tuple[int, int, int]:
    """
    Analisa uma lista de números inteiros para contar pares, ímpares e calcular a soma total.

    Args:
        lista_de_numeros (List[int]): Uma lista de números inteiros.

    Returns:
        Tuple[int, int, int]: Uma tupla contendo a quantidade de números pares,
                              a quantidade de números ímpares e a soma total dos números.
    """
    quantidade_pares = 0
    quantidade_impares = 0
    soma_total = 0

    for numero in lista_de_numeros:
        soma_total += numero
        if numero % 2 == 0:
            quantidade_pares += 1
        else:
            quantidade_impares += 1
            
    return quantidade_pares, quantidade_impares, soma_total

# Leitura da entrada: uma linha contendo números inteiros separados por espaço.
entrada_str = input()

# Verifica se a entrada não está vazia para evitar erro ao converter para int
if entrada_str.strip():
    numeros_str = entrada_str.split()
    lista_de_numeros = [int(num) for num in numeros_str]
else:
    lista_de_numeros = []

# Chamada da função e desempacotamento dos resultados
pares, impares, soma = analisar_numeros(lista_de_numeros)

# Impressão dos resultados
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Soma total: {soma}")
