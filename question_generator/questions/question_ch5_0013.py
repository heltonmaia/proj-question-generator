"""Crie uma função Python chamada `calcular_estatisticas_lista` que receba uma lista de números inteiros como entrada. A função deve calcular a soma de todos os números na lista e a média aritmética desses números. Ela deve retornar ambos os valores como uma tupla: `(soma, media)`.

No programa principal, o programa deve ler uma única linha de entrada contendo uma sequência de números inteiros separados por espaço. Esses números devem ser convertidos em uma lista e, em seguida, passados para a função `calcular_estatisticas_lista`. Finalmente, o programa deve imprimir a soma e a média calculadas, formatando a média com duas casas decimais.

Considere o caso de uma lista vazia: a soma deve ser `0` e a média deve ser `0.0`."""

def calcular_estatisticas_lista(numeros: list[int]) -> tuple[int, float]:
    """
    Calcula a soma e a média de uma lista de números inteiros.

    Args:
        numeros: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo a soma (int) e a média (float) dos números.
        Retorna (0, 0.0) se a lista for vazia.
    """
    if not numeros:
        return 0, 0.0

    soma_total = sum(numeros)
    media_calculada = soma_total / len(numeros)
    return soma_total, media_calculada

# Leitura da entrada de números inteiros separados por espaço
entrada_str = input()
numeros_str = entrada_str.split()

# Converte a lista de strings para uma lista de inteiros
numeros_int = [int(s) for s in numeros_str] if numeros_str else []

# Chama a função e desempacota os resultados
soma_final, media_final = calcular_estatisticas_lista(numeros_int)

# Imprime os resultados formatados
print(f"Soma dos números: {soma_final}")
print(f"Média dos números: {media_final:.2f}")
