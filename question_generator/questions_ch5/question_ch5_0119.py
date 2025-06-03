"""Crie um programa Python que realize uma análise estatística básica em uma lista de números fornecida pelo usuário. Para isso, você deverá implementar uma função que identifique e conte números positivos, negativos e zeros, além de calcular a soma total dos elementos.

Sua solução deve incluir:

1.  Uma função chamada `analisar_numeros` que aceite uma lista de números (inteiros ou decimais) como parâmetro. Esta função deve utilizar **type hints** para seus parâmetros e seu retorno, conforme boas práticas de Python.
2.  Dentro desta função, conte o número de elementos positivos, negativos e zeros na lista.
3.  Calcule a soma de todos os elementos da lista.
4.  A função deve retornar **quatro valores** em uma tupla: a contagem de positivos, a contagem de negativos, a contagem de zeros e a soma total dos números, **nesta exata ordem**.
5.  No programa principal, solicite ao usuário que digite uma série de números separados por espaços. Converta esta entrada em uma lista de números (assuma que todos os números serão do tipo `float` para simplificar o tratamento).
6.  Chame a função `analisar_numeros` com a lista obtida.
7.  Imprima os resultados retornados pela função de forma clara e formatada, indicando cada estatística. A soma total deve ser formatada para **duas casas decimais**.
8.  Inclua uma `docstring` na função `analisar_numeros` explicando seu propósito, argumentos e valor de retorno."""

from typing import List, Tuple

def analisar_numeros(numeros: List[float]) -> Tuple[int, int, int, float]:
    """
    Analisa uma lista de números para contar positivos, negativos, zeros e calcular a soma.

    Args:
        numeros: Uma lista de números (inteiros ou decimais).

    Returns:
        Uma tupla contendo (contagem_positivos, contagem_negativos, contagem_zeros, soma_total).
    """
    contagem_positivos = 0
    contagem_negativos = 0
    contagem_zeros = 0
    soma_total = 0.0

    for num in numeros:
        if num > 0:
            contagem_positivos += 1
        elif num < 0:
            contagem_negativos += 1
        else: # num == 0
            contagem_zeros += 1
        soma_total += num
    
    return contagem_positivos, contagem_negativos, contagem_zeros, soma_total

# Programa principal
entrada_str = input() # Assume a entrada de uma única linha de números separados por espaços
lista_numeros_str = entrada_str.split()
lista_numeros = [float(x) for x in lista_numeros_str]

positivos, negativos, zeros, soma = analisar_numeros(lista_numeros)

print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")
print(f"Quantidade de zeros: {zeros}")
print(f"Soma total: {soma:.2f}")
