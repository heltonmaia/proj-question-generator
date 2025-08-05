"""Crie um programa em Python que defina uma função para calcular estatísticas básicas de uma lista de números. A função, `analisar_estatisticas`, deve receber uma lista de números (inteiros ou decimais) como argumento.

A função deve retornar quatro valores:
1.  A soma de todos os números na lista.
2.  A média dos números na lista.
3.  O menor valor na lista.
4.  O maior valor na lista.

No programa principal, leia uma linha de números separados por espaço do usuário. Converta-os para uma lista de números de ponto flutuante (`float`). Em seguida, chame a função `analisar_estatisticas` com essa lista e imprima os resultados formatados. Todos os resultados numéricos de ponto flutuante (soma, média, menor valor, maior valor) devem ser formatados para duas casas decimais. Assuma que a lista de entrada sempre conterá pelo menos um número."""

def analisar_estatisticas(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros: Uma lista de números (inteiros ou decimais).
                 Assume-se que a lista não estará vazia.

    Returns:
        Uma tupla contendo (soma, media, menor, maior).
    """
    soma_total = sum(numeros)
    media_total = soma_total / len(numeros)
    menor_valor = min(numeros)
    maior_valor = max(numeros)

    return soma_total, media_total, menor_valor, maior_valor

# Programa principal
entrada_str = input()
numeros_str = entrada_str.split()
lista_numeros = [float(n) for n in numeros_str]

soma, media, menor, maior = analisar_estatisticas(lista_numeros)

print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")
print(f"Menor valor: {menor:.2f}")
print(f"Maior valor: {maior:.2f}")
