"""Sua tarefa é criar uma função em Python que analise uma lista de números inteiros e retorne diversas estatísticas sobre ela. A função deve ser capaz de identificar e contar a quantidade de números pares, ímpares, positivos, negativos e zeros presentes na lista.

Crie uma função chamada `analisar_lista_numeros` que receba um único parâmetro: `lista_de_numeros` (uma lista de inteiros).

A função deve retornar uma tupla contendo **cinco** valores inteiros, na seguinte ordem:
1.  O número total de elementos pares.
2.  O número total de elementos ímpares.
3.  O número total de elementos positivos (maiores que zero).
4.  O número total de elementos negativos (menores que zero).
5.  O número total de zeros.

No programa principal, você deve ler uma linha de entrada contendo números inteiros separados por vírgulas (ex: `1, -2, 0, 4`), converter essa string em uma lista de inteiros, chamar a função `analisar_lista_numeros` e, por fim, exibir os resultados formatados na saída padrão.

**Observações:**
*   Considere que a lista de entrada conterá apenas números inteiros válidos.
*   Utilize laços de repetição (`for`) e estruturas condicionais (`if`, `elif`, `else`) para percorrer a lista e realizar as contagens.
*   Aproveite o conceito de funções com múltiplos valores de retorno, conforme abordado no material de estudo do Capítulo 5."""

from typing import List, Tuple

def analisar_lista_numeros(lista_de_numeros: List[int]) -> Tuple[int, int, int, int, int]:
    """
    Analisa uma lista de números inteiros, contando pares, ímpares,
    positivos, negativos e zeros.

    Args:
        lista_de_numeros: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo:
        - A contagem de números pares.
        - A contagem de números ímpares.
        - A contagem de números positivos.
        - A contagem de números negativos.
        - A contagem de zeros.
    """
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    zeros = 0

    for numero in lista_de_numeros:
        # Contagem de pares/ímpares
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        # Contagem de positivos/negativos/zeros
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:  # numero == 0
            zeros += 1
            
    return pares, impares, positivos, negativos, zeros

# --- Parte principal do programa para leitura e exibição ---
# Lendo a entrada como uma string de números separados por vírgula
entrada_str = input()

# Convertendo a string em uma lista de inteiros
# Trata o caso de entrada vazia para evitar erro no split/int
if entrada_str.strip() == "":
    numeros = []
else:
    numeros = [int(x.strip()) for x in entrada_str.split(',')]

# Chamando a função para analisar a lista
pares, impares, positivos, negativos, zeros = analisar_lista_numeros(numeros)

# Exibindo os resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de zeros: {zeros}")
