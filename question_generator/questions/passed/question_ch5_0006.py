"""Desenvolva um programa que determine o menor e o maior número entre três valores fornecidos pelo usuário. O programa deve utilizar funções para realizar as operações necessárias. Siga as instruções:

*   Crie uma função chamada `ler_numeros()` que solicite ao usuário que insira três números e retorne esses valores.
*   Implemente uma função chamada `encontrar_menor_maior(a, b, c)` que receba três números como parâmetros e retorne uma tupla contendo o menor e o maior valor, nesta ordem.
*   No programa principal, utilize as funções criadas para:
    *   Obter os três números do usuário.
    *   Calcular o menor e o maior valor.
    *   Exibir os resultados.

Certifique-se de que o programa trate adequadamente diferentes tipos de entrada, incluindo números inteiros e decimais."""

def ler_numeros() -> tuple[float, float, float]:
    """
    Solicita ao usuário que insira três números (um por linha) e retorna esses valores.
    Os valores são lidos como float para suportar inteiros e decimais.
    """
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    return num1, num2, num3

def encontrar_menor_maior(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Encontra o menor e o maior valor entre três números dados.
    Args:
        a (float): O primeiro número.
        b (float): O segundo número.
        c (float): O terceiro número.
    Retorna:
        tuple[float, float]: Uma tupla contendo o menor e o maior valor, nesta ordem.
    """
    menor = min(a, b, c)
    maior = max(a, b, c)
    return menor, maior

# Programa principal
num1, num2, num3 = ler_numeros()
menor, maior = encontrar_menor_maior(num1, num2, num3)

print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")
