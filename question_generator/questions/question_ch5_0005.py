"""Desenvolva um programa Python que inclua uma função chamada `calcular_operacoes` que recebe dois números (inteiros ou decimais) como parâmetros. Esta função deve calcular e retornar **três** resultados: a soma, o produto e a diferença (primeiro número menos o segundo) desses dois números.

No programa principal, o usuário deverá fornecer os dois números. Em seguida, utilize a função `calcular_operacoes` para obter os resultados e imprima-os formatados na tela.

**Requisitos:**
- A função `calcular_operacoes` deve usar `type hints` para indicar os tipos dos parâmetros de entrada e o tipo de retorno.
- A função deve retornar uma tupla contendo a soma, o produto e a diferença, nesta ordem.
- O programa principal deve ler os dois números de entrada e imprimir os resultados de forma clara, indicando qual valor corresponde à soma, ao produto e à diferença. Todos os resultados devem ser formatados com duas casas decimais."""

def calcular_operacoes(num1: float, num2: float) -> tuple[float, float, float]:
    """
    Calcula a soma, o produto e a diferença de dois números.

    Args:
        num1 (float): O primeiro número.
        num2 (float): O segundo número.

    Returns:
        tuple[float, float, float]: Uma tupla contendo (soma, produto, diferenca).
    """
    soma = num1 + num2
    produto = num1 * num2
    diferenca = num1 - num2
    return soma, produto, diferenca

# Leitura dos números do usuário
numero_a = float(input())
numero_b = float(input())

# Chamada da função e desempacotamento dos resultados
soma_res, produto_res, diferenca_res = calcular_operacoes(numero_a, numero_b)

# Impressão dos resultados
print(f"Soma: {soma_res:.2f}")
print(f"Produto: {produto_res:.2f}")
print(f"Diferença: {diferenca_res:.2f}")
