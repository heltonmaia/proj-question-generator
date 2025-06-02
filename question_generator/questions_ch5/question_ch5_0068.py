"""Desenvolva um programa Python que analise uma sequência de números inteiros fornecida pelo usuário. O programa deve utilizar uma função para processar essa sequência e retornar a contagem de números positivos, negativos, zeros, bem como a contagem de números pares e ímpares.

Sua tarefa é implementar a função `analisar_estatisticas_numericas` que receberá uma lista de números inteiros como argumento. Esta função deve calcular e retornar cinco valores inteiros (na forma de uma tupla), na seguinte ordem:
1.  Contagem de números positivos.
2.  Contagem de números negativos.
3.  Contagem de zeros.
4.  Contagem de números pares.
5.  Contagem de números ímpares.

No programa principal, você deve:
1.  Ler uma linha de entrada que conterá números inteiros separados por espaço (ex: `"1 2 0 -3 -4"`).
2.  Converter essa string de números em uma lista de inteiros.
3.  Chamar a função `analisar_estatisticas_numericas` com a lista criada.
4.  Imprimir os resultados das contagens, um por linha, com rótulos claros conforme o exemplo de saída."""

from typing import List, Tuple

def analisar_estatisticas_numericas(numeros: List[int]) -> Tuple[int, int, int, int, int]:
    """
    Analisa uma lista de números inteiros e retorna a contagem de positivos, negativos, zeros, pares e ímpares.

    Args:
        numeros: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo (count_positivos, count_negativos, count_zeros, count_pares, count_impares).
    """
    count_positivos = 0
    count_negativos = 0
    count_zeros = 0
    count_pares = 0
    count_impares = 0

    for num in numeros:
        if num > 0:
            count_positivos += 1
        elif num < 0:
            count_negativos += 1
        else: # num == 0
            count_zeros += 1

        if num % 2 == 0:
            count_pares += 1
        else:
            count_impares += 1
            
    return count_positivos, count_negativos, count_zeros, count_pares, count_impares

# Leitura da entrada
linha_entrada = input()
numeros_str = linha_entrada.split()
lista_de_numeros = [int(n) for n in numeros_str]

# Chamada da função e desempacotamento dos resultados
pos, neg, zeros, pares, impares = analisar_estatisticas_numericas(lista_de_numeros)

# Impressão dos resultados
print(f"Positivos: {pos}")
print(f"Negativos: {neg}")
print(f"Zeros: {zeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
