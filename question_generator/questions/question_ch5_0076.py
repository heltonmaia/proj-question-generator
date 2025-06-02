"""Desenvolva uma função Python chamada `analisar_notas` que receba uma lista de notas (números de ponto flutuante) de um estudante como entrada. Esta função deve calcular e retornar **três valores** em uma tupla:
1.  A média das notas.
2.  A maior nota encontrada na lista.
3.  A menor nota encontrada na lista.

A função deve ser capaz de lidar com uma lista vazia, retornando `(0.0, 0.0, 0.0)` nesses casos para a média, maior e menor nota, respectivamente. Para o cálculo da média, a soma das notas deve ser dividida pelo número total de notas.

No programa principal, solicite ao usuário uma sequência de notas separadas por espaços em uma única linha. Converta essas notas para uma lista de números de ponto flutuante, chame a função `analisar_notas` com essa lista e exiba os resultados formatados da seguinte maneira:
*   A média deve ser exibida com duas casas decimais.
*   A maior e a menor nota devem ser exibidas com uma casa decimal."""

def analisar_notas(notas: list[float]) -> tuple[float, float, float]:
    """
    Calcula a média, a maior e a menor nota de uma lista de notas.

    Args:
        notas (list[float]): Uma lista de notas de um estudante.

    Returns:
        tuple[float, float, float]: Uma tupla contendo a média, a maior e a menor nota.
                                     Se a lista for vazia, retorna (0.0, 0.0, 0.0).
    """
    if not notas:
        return 0.0, 0.0, 0.0
    
    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    
    return media, maior_nota, menor_nota

# Programa principal
entrada_notas_str = input()
# Converte a string de entrada para uma lista de floats.
# Se a entrada for vazia (apenas Enter), split() retornará [], resultando em uma lista vazia.
notas_list = [float(nota) for nota in entrada_notas_str.split()]

# Chama a função e desempacota os múltiplos valores de retorno
media, maior, menor = analisar_notas(notas_list)

# Exibe os resultados formatados
print(f"Média: {media:.2f}")
print(f"Maior nota: {maior:.1f}")
print(f"Menor nota: {menor:.1f}")
