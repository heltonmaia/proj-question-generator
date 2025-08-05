"""Desenvolva uma função Python que receba uma lista de números inteiros e retorne múltiplas informações sobre essa lista. A função deve calcular e retornar em uma tupla os seguintes valores, nesta ordem:

1.  A soma de todos os números na lista.
2.  A contagem de números pares.
3.  A contagem de números ímpares.
4.  A contagem de números positivos (excluindo o zero).
5.  A contagem de números negativos (excluindo o zero).

No programa principal, você deve solicitar ao usuário que insira uma série de números inteiros, separados por espaços, em uma única linha. Esses números serão então convertidos em uma lista. Em seguida, chame a função criada com essa lista e exiba todos os resultados de forma clara e formatada."""

def analisar_lista_numeros(lista: list[int]) -> tuple[int, int, int, int, int]:
    """
    Analisa uma lista de números inteiros e retorna a soma,
    a contagem de pares, ímpares, positivos e negativos.

    Args:
        lista (list[int]): Uma lista de números inteiros.

    Returns:
        tuple[int, int, int, int, int]: Uma tupla contendo:
            - A soma total dos números.
            - A contagem de números pares.
            - A contagem de números ímpares.
            - A contagem de números positivos (ignorando o zero).
            - A contagem de números negativos.
    """
    soma_total = 0
    contagem_pares = 0
    contagem_impares = 0
    contagem_positivos = 0
    contagem_negativos = 0

    for num in lista:
        soma_total += num

        if num % 2 == 0:
            contagem_pares += 1
        else:
            contagem_impares += 1

        if num > 0:
            contagem_positivos += 1
        elif num < 0:
            contagem_negativos += 1
            
    return soma_total, contagem_pares, contagem_impares, contagem_positivos, contagem_negativos

# Programa principal
entrada_str = input()
if entrada_str.strip(): # Verifica se a string de entrada não está vazia após remover espaços
    numeros = [int(x) for x in entrada_str.split()]
else:
    numeros = [] # Lista vazia se a entrada for vazia

soma, pares, impares, positivos, negativos = analisar_lista_numeros(numeros)

print(f"Soma total: {soma}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
