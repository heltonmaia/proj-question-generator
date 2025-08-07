"""Desenvolva um programa que analise uma lista de números inteiros fornecida pelo usuário. O programa deve conter uma única função chamada `analisar_caracteristicas_lista` que receba essa lista como argumento e retorne **quatro** valores:

1.  A contagem de números pares.
2.  A contagem de números ímpares.
3.  A contagem de números positivos (ignorando o zero, que não é positivo nem negativo).
4.  A contagem de números negativos (ignorando o zero).

O programa principal deve:
1.  Ler uma sequência de números inteiros separados por espaço do usuário e convertê-los em uma lista de inteiros.
2.  Chamar a função `analisar_caracteristicas_lista` passando a lista gerada.
3.  Imprimir os quatro resultados retornados pela função em linhas separadas, com mensagens claras, seguindo o formato dos exemplos.

**Considerações:**
*   Utilize `type hints` e `docstrings` na função para melhorar a clareza e documentação do código.
*   O número 0 não deve ser contado nem como positivo nem como negativo."""

def analisar_caracteristicas_lista(numeros: list[int]) -> tuple[int, int, int, int]:
    """
    Analisa uma lista de números inteiros e retorna a contagem de pares, ímpares,
    positivos e negativos.

    Args:
        numeros (list[int]): A lista de números inteiros a ser analisada.

    Returns:
        tuple[int, int, int, int]: Uma tupla contendo (contagem_pares, contagem_impares,
                                      contagem_positivos, contagem_negativos).
    """
    count_pares = 0
    count_impares = 0
    count_positivos = 0
    count_negativos = 0

    for num in numeros:
        # Verifica se o número é par ou ímpar
        if num % 2 == 0:
            count_pares += 1
        else:
            count_impares += 1

        # Verifica se o número é positivo ou negativo (ignorando o zero)
        if num > 0:
            count_positivos += 1
        elif num < 0:
            count_negativos += 1
            
    return count_pares, count_impares, count_positivos, count_negativos

# Leitura da entrada (sequência de números separados por espaço)
entrada_str = input().split()
lista_de_numeros = [int(x) for x in entrada_str]

# Chamada da função e desempacotamento dos resultados
pares, impares, positivos, negativos = analisar_caracteristicas_lista(lista_de_numeros)

# Impressão dos resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
