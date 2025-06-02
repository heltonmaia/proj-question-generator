"""Crie uma função Python chamada `analisar_estatisticas` que receba uma lista de números de ponto flutuante (`float`) como argumento. Esta função deve calcular a soma total, a média aritmética, o valor máximo e o valor mínimo dos números na lista.

A função `analisar_estatisticas` deve retornar esses quatro valores em uma tupla, na ordem `(soma, media, maximo, minimo)`.

Seu programa deve ler uma linha de números de ponto flutuante (separados por espaços) fornecidos pelo usuário, converter esses números em uma lista de `float`s, e então utilizar a função `analisar_estatisticas` para obter as estatísticas. Finalmente, imprima os resultados de forma clara, formatando a soma e a média com duas casas decimais.

**Observação:** Para este exercício, você pode assumir que a lista de entrada conterá sempre pelo menos um número."""

def analisar_estatisticas(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, valor máximo e valor mínimo de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números de ponto flutuante.
                                Assume-se que a lista não estará vazia.

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo a soma, média,
                                           valor máximo e valor mínimo, nesta ordem.
    """
    total = sum(numeros)
    quantidade = len(numeros)
    media = total / quantidade
    maximo = max(numeros)
    minimo = min(numeros)

    return (total, media, maximo, minimo)

# Leitura da entrada (uma linha de números separados por espaço)
entrada_str = input()
numeros_str = entrada_str.split()
numeros_float = [float(num) for num in numeros_str]

# Chamada da função e desempacotamento dos resultados
soma, media, maximo, minimo = analisar_estatisticas(numeros_float)

# Impressão dos resultados
print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
