"""Você foi encarregado de desenvolver um programa em Python que analise uma lista de números e forneça estatísticas básicas sobre eles. O programa deve ser capaz de receber múltiplos números como entrada, processá-los e apresentar a soma, a média, o menor e o maior valor.

Para isso, siga os passos abaixo:

1.  **Função `analisar_estatisticas(numeros: list[float]) -> tuple[float, float, float, float]`:**
    *   Crie uma função chamada `analisar_estatisticas` que aceite uma lista de números de ponto flutuante (`float`) como argumento.
    *   Dentro dessa função, calcule a **soma total**, a **média aritmética**, o **menor valor** e o **maior valor** presentes na lista.
    *   A função deve retornar esses quatro resultados em uma tupla, na seguinte ordem: `(soma, media, menor, maior)`.
    *   Adicione uma docstring e type hints para clareza.
    *   **Observação:** Assuma que a lista de entrada conterá pelo menos um número.

2.  **Programa Principal:**
    *   No programa principal, solicite ao usuário que insira uma série de números separados por espaço em uma única linha.
    *   Converta a entrada do usuário em uma lista de números de ponto flutuante.
    *   Chame a função `analisar_estatisticas` com a lista de números fornecida.
    *   Imprima os resultados obtidos (soma, média, menor e maior valor) de forma clara e formatada. A soma, o menor e o maior valor devem ser exibidos com uma casa decimal (ex: `150.0`), e a média deve ser exibida com duas casas decimais (ex: `30.00`)."""

def analisar_estatisticas(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números de ponto flutuante.
                               Assume-se que a lista conterá pelo menos um número.

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo (soma, media, menor, maior).
    """
    soma = sum(numeros)
    media = soma / len(numeros)
    menor = min(numeros)
    maior = max(numeros)

    return soma, media, menor, maior

# Programa principal
# A entrada será uma linha de números separados por espaço
entrada_str = input()
numeros_str = entrada_str.split()
numeros_float = [float(num) for num in numeros_str]

# Desempacota os múltiplos valores retornados pela função
soma_total, media_aritmetica, menor_valor, maior_valor = analisar_estatisticas(numeros_float)

# Imprime os resultados formatados
print(f"Soma: {soma_total:.1f}")
print(f"Média: {media_aritmetica:.2f}")
print(f"Menor valor: {menor_valor:.1f}")
print(f"Maior valor: {maior_valor:.1f}")
