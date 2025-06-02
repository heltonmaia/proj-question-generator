"""Desenvolva um programa Python que utilize funções para analisar uma lista de números inteiros. O programa deve seguir os passos abaixo:

1.  **Ler a lista de números:** Solicite ao usuário que insira uma sequência de números inteiros separados por espaços na mesma linha (ex: `1 2 3 4 5`). Converta essa entrada em uma lista de inteiros.
2.  **Função de Análise (`analisar_lista_numeros`):** Implemente uma função chamada `analisar_lista_numeros` que aceite uma lista de inteiros (`list[int]`) como parâmetro.
3.  **Cálculos na Função:** Esta função deve calcular e retornar três valores como uma tupla (`tuple[int, int, int]`):
    *   A soma de todos os números na lista.
    *   A contagem de números pares na lista.
    *   A contagem de números ímpares na lista.
    (Dica: Utilize o operador de módulo `%` para verificar se um número é par ou ípar.)
4.  **Exibição dos Resultados:** No programa principal, após ler a entrada e chamar a função `analisar_lista_numeros`, desempacote os valores de retorno em variáveis apropriadas. Em seguida, imprima a soma total, a quantidade de números pares e a quantidade de números ímpares de forma clara, cada um em uma linha separada."""

from typing import List, Tuple

def analisar_lista_numeros(numeros: List[int]) -> Tuple[int, int, int]:
    """
    Analisa uma lista de números inteiros, retornando a soma,
    a contagem de números pares e a contagem de números ímpares.

    Args:
        numeros: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo (soma_total, quantidade_pares, quantidade_impares).
    """
    soma_total = 0
    quantidade_pares = 0
    quantidade_impares = 0

    for num in numeros:
        soma_total += num
        if num % 2 == 0:
            quantidade_pares += 1
        else:
            quantidade_impares += 1
            
    return soma_total, quantidade_pares, quantidade_impares

# Leitura da entrada de números separados por espaços
entrada_str = input()
numeros_str = entrada_str.split() # Divide a string em uma lista de strings

# Converte cada string para inteiro
numeros_int = [int(num) for num in numeros_str]

# Chamada da função e desempacotamento dos resultados
soma, pares, impares = analisar_lista_numeros(numeros_int)

# Impressão dos resultados
print(f"Soma total: {soma}")
print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
