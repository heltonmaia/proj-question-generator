"""Escreva duas funções em Python para analisar uma lista de números inteiros:

1.  **`contar_pares_impares(lista_numeros)`**: Esta função deve receber uma lista de números inteiros como argumento. Ela deve retornar uma tupla contendo duas variáveis: a contagem de números pares e a contagem de números ímpares na lista, nesta ordem.
2.  **`contar_positivos_negativos(lista_numeros)`**: Esta função também deve receber a mesma lista de números inteiros como argumento. Ela deve retornar uma tupla contendo duas variáveis: a contagem de números positivos e a contagem de números negativos na lista, nesta ordem. (Note que o número zero não deve ser contado como positivo nem como negativo).

O programa principal deve:
*   Ler uma linha de números inteiros, separados por vírgula, da entrada padrão.
*   Converter essa entrada em uma lista de números inteiros.
*   Chamar as funções `contar_pares_impares` e `contar_positivos_negativos` com a lista criada.
*   Imprimir os resultados obtidos de cada função, cada um em uma linha separada, seguindo o formato dos exemplos de saída."""

def contar_pares_impares(lista_numeros: list[int]) -> tuple[int, int]:
    """
    Conta a quantidade de números pares e ímpares em uma lista.

    Args:
        lista_numeros (list[int]): Uma lista de números inteiros.

    Returns:
        tuple[int, int]: Uma tupla contendo (quantidade_pares, quantidade_impares).
    """
    pares = 0
    impares = 0
    for num in lista_numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def contar_positivos_negativos(lista_numeros: list[int]) -> tuple[int, int]:
    """
    Conta a quantidade de números positivos e negativos em uma lista.

    Args:
        lista_numeros (list[int]): Uma lista de números inteiros.

    Returns:
        tuple[int, int]: Uma tupla contendo (quantidade_positivos, quantidade_negativos).
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
entrada_str = input()
lista_numeros = list(map(int, entrada_str.split(',')))

# Chama as funções e desempacota os resultados
pares, impares = contar_pares_impares(lista_numeros)
positivos, negativos = contar_positivos_negativos(lista_numeros)

# Imprime os resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
