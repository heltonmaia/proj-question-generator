"""Desenvolva um programa Python que realize a análise estatística de uma lista de números. O programa deve conter uma função que receba uma lista de números (inteiros ou de ponto flutuante) como argumento e retorne quatro valores: a soma dos elementos, a média aritmética, o maior valor e o menor valor da lista.

No programa principal, o usuário deverá fornecer uma sequência de números separados por espaços. O programa então converterá esses números em uma lista de valores numéricos (ponto flutuante), chamará a função criada e exibirá todos os resultados de forma formatada.

**Requisitos:**
- Crie uma função chamada `analisar_estatisticas` que receba uma lista de números (`list[float]`) e retorne uma tupla contendo a soma, a média, o maior e o menor valor (todos como `float`).
- Utilize as funções `sum()`, `len()`, `max()`, e `min()` do Python para os cálculos.
- A saída deve formatar a média para duas casas decimais.
- Considere que a lista de entrada sempre conterá pelo menos um número."""

def analisar_estatisticas(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, maior e menor valor de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números (inteiros ou ponto flutuante).

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo (soma, media, maior, menor).
    """
    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return soma, media, maior, menor

# Programa principal
entrada_str = input("Digite os números separados por espaços: ")
numeros_str = entrada_str.split()

# Converte strings para float
numeros_float = []
for num_str in numeros_str:
    numeros_float.append(float(num_str))

soma_total, media_total, maior_valor, menor_valor = analisar_estatisticas(numeros_float)

print(f"Soma dos números: {soma_total}")
print(f"Média dos números: {media_total:.2f}")
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
