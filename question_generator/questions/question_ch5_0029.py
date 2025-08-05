"""Você foi contratado para criar um pequeno programa de análise de dados para uma empresa que registra o desempenho de seus produtos em vendas. Para isso, você precisa desenvolver uma função em Python que receba uma lista de números (que podem representar, por exemplo, unidades vendidas ou lucros) e retorne várias estatísticas importantes sobre essa lista.

Sua tarefa é implementar uma função chamada `analisar_estatisticas_lista` que receba como parâmetro uma lista de números (inteiros ou decimais). Esta função deve calcular e retornar os seguintes valores:

1.  A soma de todos os números na lista.
2.  A média aritmética dos números na lista.
3.  O menor valor presente na lista.
4.  O maior valor presente na lista.

Todos esses quatro valores devem ser retornados como uma única tupla.

No programa principal, você deve:
*   Solicitar ao usuário que insira uma série de números em uma única linha, separados por espaços (ex: "10 20 30 40 50" ou "5.5 1.2 8.9 3.1").
*   Converter esses números para o tipo `float` e armazená-los em uma lista.
*   Chamar a função `analisar_estatisticas_lista` com a lista de números convertidos.
*   Imprimir os resultados obtidos (soma, média, menor valor, maior valor), formatando os valores numéricos com duas casas decimais.

Considere que a lista de entrada nunca estará vazia para simplificar o exercício."""

def analisar_estatisticas_lista(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números (inteiros ou decimais).
                                Assume-se que a lista não estará vazia.

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo (soma, media, menor_valor, maior_valor).
    """
    soma_total = sum(numeros)
    media = soma_total / len(numeros)
    menor_valor = min(numeros)
    maior_valor = max(numeros)
    return soma_total, media, menor_valor, maior_valor

# Leitura da entrada
# O usuário inserirá números separados por espaço em uma única linha
entrada_str = input()
numeros_str = entrada_str.split()
numeros_convertidos = [float(num) for num in numeros_str]

# Chamada da função e desempacotamento dos resultados
soma, media, menor, maior = analisar_estatisticas_lista(numeros_convertidos)

# Impressão dos resultados formatados
print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")
print(f"Menor valor: {menor:.2f}")
print(f"Maior valor: {maior:.2f}")
