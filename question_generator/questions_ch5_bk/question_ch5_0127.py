"""Você deve criar um programa Python que realize a análise estatística básica de uma sequência de números fornecida pelo usuário.

1.  O programa deve solicitar ao usuário que digite uma série de números de ponto flutuante, separados por espaços, em uma única linha.
2.  Desenvolva uma função chamada `calcular_estatisticas` que receba uma lista de números (`list[float]`) como parâmetro.
3.  Dentro desta função, calcule a **soma** de todos os números da lista e a **média aritmética**.
4.  A função `calcular_estatisticas` deve retornar dois valores: a soma e a média, em uma tupla.
5.  No programa principal, após obter a entrada do usuário e converter os números para uma lista de `float`s, chame a função `calcular_estatisticas`.
6.  Caso a lista de números fornecida pelo usuário esteja vazia (ou seja, o usuário não digitou nenhum número ou apenas espaços), sua função deve retornar uma soma de `0.0` e uma média de `0.0`.
7.  Por fim, imprima os resultados da soma e da média formatados com duas casas decimais, conforme os exemplos de saída."""

from typing import List, Tuple

def calcular_estatisticas(numeros: List[float]) -> Tuple[float, float]:
    """
    Calcula a soma e a média de uma lista de números.

    Args:
        numeros: Uma lista de números de ponto flutuante.

    Returns:
        Uma tupla contendo a soma total e a média dos números.
        Retorna (0.0, 0.0) se a lista estiver vazia.
    """
    if not numeros:
        return 0.0, 0.0
    
    soma = sum(numeros)
    media = soma / len(numeros)
    return soma, media

# Leitura da entrada do usuário
# O método .split() sem argumentos divide a string por qualquer espaço em branco
# e descarta strings vazias resultantes (útil para múltiplos espaços ou entrada vazia).
entrada_str = input()
lista_numeros = [float(num) for num in entrada_str.split()]

# Chama a função e desempacota os resultados
soma_total, media_final = calcular_estatisticas(lista_numeros)

# Imprime os resultados formatados
print(f"Soma: {soma_total:.2f}")
print(f"Média: {media_final:.2f}")
