"""Desenvolva um programa que determine o menor e o maior número entre três valores fornecidos pelo usuário. O programa deve utilizar funções para realizar as operações necessárias, demonstrando o uso de funções com e sem retorno, e o retorno de múltiplos valores. Siga as instruções:

1.  Crie uma função chamada `ler_numeros()` que solicite ao usuário que insira três números. Utilize `float(input())` para garantir que o programa possa lidar tanto com números inteiros quanto com decimais. Esta função deve retornar os três valores lidos como uma tupla.
2.  Implemente uma função chamada `encontrar_menor_maior(a, b, c)` que receba três números (do tipo `float`) como parâmetros e retorne uma tupla contendo o menor e o maior valor entre eles, nesta ordem.
3.  No programa principal, utilize as funções criadas para:
    *   Obter os três números do usuário chamando `ler_numeros()`.
    *   Calcular o menor e o maior valor chamando `encontrar_menor_maior()`.
    *   Exibir os resultados na tela, seguindo o formato de saída dos exemplos."""

def ler_numeros() -> tuple[float, float, float]:
    """
    Solicita ao usuário que insira três números e os retorna como floats.
    """
    print("Por favor, insira o primeiro número:")
    num1 = float(input())
    print("Por favor, insira o segundo número:")
    num2 = float(input())
    print("Por favor, insira o terceiro número:")
    num3 = float(input())
    return num1, num2, num3

def encontrar_menor_maior(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Encontra o menor e o maior valor entre três números.

    Args:
        a (float): O primeiro número.
        b (float): O segundo número.
        c (float): O terceiro número.

    Returns:
        tuple[float, float]: Uma tupla contendo o menor e o maior valor, nesta ordem.
    """
    menor = min(a, b, c)
    maior = max(a, b, c)
    return menor, maior

# Programa principal
# As mensagens de input são para guiar o usuário na execução interativa.
# Para testes automatizados, a entrada deve ser fornecida sequencialmente.
num1, num2, num3 = ler_numeros()
menor, maior = encontrar_menor_maior(num1, num2, num3)

print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")
