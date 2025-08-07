"""Crie uma função Python chamada `analisar_numeros` que receba uma lista de números (inteiros ou de ponto flutuante) como argumento. Esta função deve calcular e retornar, em uma tupla, os seguintes valores, nesta ordem:
1.  A soma de todos os elementos na lista.
2.  A média aritmética dos elementos na lista.
3.  O menor valor presente na lista.
4.  O maior valor presente na lista.

Sua função deve incluir `docstrings` e `type hints` para garantir clareza e documentação. No programa principal, você deve ler uma única linha de entrada contendo números separados por espaço, converter esses números para o tipo apropriado (ponto flutuante), e então chamar a função `analisar_numeros` com essa lista. Por fim, imprima os resultados da soma, média, menor e maior valor, formatando a média e os valores mínimo e máximo para duas casas decimais."""

from typing import List, Tuple

def analisar_numeros(numeros: List[float]) -> Tuple[float, float, float, float]:
    """
    Calcula a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros (List[float]): Uma lista de números (inteiros ou ponto flutuante).
                               Assume-se que a lista não estará vazia para este exercício.

    Returns:
        Tuple[float, float, float, float]: Uma tupla contendo a soma, média,
                                           menor valor e maior valor da lista,
                                           nesta ordem.
    """
    soma_total = sum(numeros)
    media = soma_total / len(numeros)
    menor_valor = min(numeros)
    maior_valor = max(numeros)

    return soma_total, media, menor_valor, maior_valor

# Leitura da entrada: uma linha com números separados por espaço
entrada_str = input()
numeros_str = entrada_str.split()
numeros_float = [float(num) for num in numeros_str]

# Chama a função e desempacota os resultados
soma, media, menor, maior = analisar_numeros(numeros_float)

# Imprime os resultados formatados
print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")
print(f"Menor valor: {menor:.2f}")
print(f"Maior valor: {maior:.2f}")
