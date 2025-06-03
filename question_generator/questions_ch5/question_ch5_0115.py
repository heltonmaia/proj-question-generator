"""Desenvolva um programa em Python que realize uma análise estatística básica em uma lista de números inteiros. O programa deve incluir uma função principal que recebe essa lista e retorna múltiplos valores, encapsulando os resultados de diferentes cálculos.

Sua tarefa é:

1.  **Definir uma função** chamada `analisar_estatisticas_lista` que aceite uma lista de números inteiros como parâmetro (`numeros: list[int]`).
2.  Dentro desta função, calcule as seguintes estatísticas:
    *   A soma de todos os números **pares** na lista.
    *   A soma de todos os números **ímpares** na lista.
    *   A contagem total de números **positivos** (maiores que zero) na lista.
    *   A contagem total de números **negativos** (menores que zero) na lista.
3.  A função `analisar_estatisticas_lista` deve **retornar todos esses quatro valores** como uma tupla.
4.  No **programa principal**:
    *   Solicite ao usuário que insira uma sequência de números inteiros, separados por espaços.
    *   Converta a entrada do usuário em uma lista de inteiros.
    *   Chame a função `analisar_estatisticas_lista` com a lista criada.
    *   Imprima os resultados retornados pela função em um formato claro e legível, conforme o exemplo de saída.

**Observações:**
*   Considere o número `0` como um número par, mas ele não deve ser contado como positivo nem negativo.
*   A função deve lidar corretamente com listas vazias."""

def analisar_estatisticas_lista(numeros: list[int]) -> tuple[int, int, int, int]:
    """
    Analisa uma lista de números inteiros e retorna estatísticas sobre eles.

    Args:
        numeros (list[int]): A lista de números inteiros a ser analisada.

    Returns:
        tuple[int, int, int, int]: Uma tupla contendo:
            - A soma dos números pares.
            - A soma dos números ímpares.
            - A contagem de números positivos (ignorando o zero).
            - A contagem de números negativos (ignorando o zero).
    """
    soma_pares = 0
    soma_impares = 0
    cont_positivos = 0
    cont_negativos = 0

    for num in numeros:
        if num % 2 == 0:
            soma_pares += num
        else:
            soma_impares += num

        if num > 0:
            cont_positivos += 1
        elif num < 0:
            cont_negativos += 1
        # Números zero são tratados como pares na soma, mas não são contados como positivos nem negativos.

    return soma_pares, soma_impares, cont_positivos, cont_negativos

# Programa principal
# Lê a entrada como uma linha de números separados por espaço e converte para uma lista de inteiros.
# Se a entrada for uma linha vazia ou apenas espaços, lista_numeros será uma lista vazia.
lista_numeros = [int(x) for x in input().split()]

# Chama a função e desempacota os valores retornados
soma_pares_res, soma_impares_res, cont_positivos_res, cont_negativos_res = analisar_estatisticas_lista(lista_numeros)

# Imprime os resultados
print(f"Soma dos pares: {soma_pares_res}")
print(f"Soma dos ímpares: {soma_impares_res}")
print(f"Total de positivos: {cont_positivos_res}")
print(f"Total de negativos: {cont_negativos_res}")
