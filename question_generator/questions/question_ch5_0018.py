"""Crie uma função Python chamada `analisar_estatisticas_lista` que receba uma lista de números (do tipo `float` ou `int`) como argumento. Esta função deve calcular e retornar, em uma única tupla, os seguintes valores, nesta ordem:

1.  A soma de todos os números na lista.
2.  A média aritmética dos números na lista.
3.  O menor valor presente na lista.
4.  O maior valor presente na lista.

Se a lista estiver vazia, a função deve retornar uma tupla com `(0.0, 0.0, None, None)` para indicar que não é possível calcular as estatísticas.

No programa principal, leia uma linha de entrada que conterá vários números separados por espaços. Converta esses números para uma lista de floats e passe-a para a função. Em seguida, imprima os resultados formatados como indicado nos exemplos de teste. Utilize docstrings e type hints para documentar sua função, conforme as boas práticas de Python."""

from typing import List, Tuple, Optional

def analisar_estatisticas_lista(numeros: List[float]) -> Tuple[float, float, Optional[float], Optional[float]]:
    """
    Calcula estatísticas básicas (soma, média, menor, maior) para uma lista de números.

    Args:
        numeros (List[float]): Uma lista de números (inteiros ou floats).

    Returns:
        Tuple[float, float, Optional[float], Optional[float]]: Uma tupla contendo:
            - A soma de todos os números.
            - A média aritmética dos números.
            - O menor valor presente na lista.
            - O maior valor presente na lista.
            Retorna (0.0, 0.0, None, None) se a lista for vazia.
    """
    if not numeros:
        return 0.0, 0.0, None, None

    soma_total = sum(numeros)
    quantidade = len(numeros)
    media = soma_total / quantidade
    menor_valor = min(numeros)
    maior_valor = max(numeros)

    return soma_total, media, menor_valor, maior_valor

# Programa principal
entrada_str = input()
lista_numeros = [float(x) for x in entrada_str.split()] if entrada_str.strip() else []

soma_res, media_res, menor_res, maior_res = analisar_estatisticas_lista(lista_numeros)

print(f"Soma: {soma_res:.2f}")
if media_res is not None:
    print(f"Média: {media_res:.2f}")
else:
    print(f"Média: {media_res}")
if menor_res is not None:
    print(f"Menor: {menor_res:.2f}")
else:
    print(f"Menor: {menor_res}")
if maior_res is not None:
    print(f"Maior: {maior_res:.2f}")
else:
    print(f"Maior: {maior_res}")
