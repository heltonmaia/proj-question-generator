"""Escreva duas funções em Python para analisar uma lista de números inteiros:

1.  **`contar_pares_impares(lista_numeros)`:** Esta função deve receber uma lista de números inteiros como argumento. Ela deve contar quantos números são pares e quantos são ímpares na lista e, em seguida, retornar esses dois valores (contagem de pares e contagem de ímpares) como uma tupla.
2.  **`contar_positivos_negativos(lista_numeros)`:** Esta função também deve receber a mesma lista de números inteiros como argumento. Ela deve contar quantos números são positivos e quantos são negativos na lista. O número zero não deve ser contado como positivo nem como negativo. A função deve retornar esses dois valores (contagem de positivos e contagem de negativos) como uma tupla.

Após a implementação das funções, o programa principal deve:
*   Ler uma única linha de entrada, que conterá uma série de números inteiros separados por vírgulas.
*   Converter esta entrada em uma lista de números inteiros.
*   Chamar as funções `contar_pares_impares` e `contar_positivos_negativos` com a lista criada.
*   Imprimir os resultados das contagens na saída padrão, cada um em uma linha separada, seguindo o formato especificado nos exemplos de teste."""

from typing import List, Tuple

def contar_pares_impares(lista_numeros: List[int]) -> Tuple[int, int]:
    """
    Conta a quantidade de números pares e ímpares em uma lista.

    Args:
        lista_numeros: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo (contagem_pares, contagem_impares).
    """
    pares = 0
    impares = 0
    for num in lista_numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def contar_positivos_negativos(lista_numeros: List[int]) -> Tuple[int, int]:
    """
    Conta a quantidade de números positivos e negativos em uma lista.
    O número zero não é considerado nem positivo nem negativo.

    Args:
        lista_numeros: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo (contagem_positivos, contagem_negativos).
    """
    positivos = 0
    negativos = 0
    for num in lista_numeros:
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
    return positivos, negativos

# Programa principal
# Lê a entrada como uma string de números separados por vírgulas e espaços,
# e converte para uma lista de inteiros.
numeros_str = input()
if not numeros_str.strip(): # Lida com entradas vazias ou apenas com espaços em branco
    lista_de_numeros = []
else:
    lista_de_numeros = [int(num.strip()) for num in numeros_str.split(',')]

# Chama as funções e exibe os resultados
pares, impares = contar_pares_impares(lista_de_numeros)
positivos, negativos = contar_positivos_negativos(lista_de_numeros)

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
