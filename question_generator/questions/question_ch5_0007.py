"""Desenvolva um programa em Python que calcule a área e o perímetro de um retângulo. O programa deve solicitar ao usuário o comprimento e a largura do retângulo.

Crie uma função chamada `calcular_retangulo` que receba o comprimento e a largura como parâmetros (ambos do tipo `float`). Esta função deve calcular a área e o perímetro do retângulo e retornar ambos os valores como uma tupla. Utilize type hints para indicar os tipos dos parâmetros e do retorno da função, e inclua uma docstring para descrever sua funcionalidade.

No programa principal, obtenha as dimensões do usuário, chame a função `calcular_retangulo` para obter a área e o perímetro, e, em seguida, imprima esses resultados na tela, formatando-os para exibir sempre duas casas decimais.

Fórmulas:
*   **Área** = comprimento × largura
*   **Perímetro** = 2 × (comprimento + largura)"""

def calcular_retangulo(comprimento: float, largura: float) -> tuple[float, float]:
    """
    Calcula a área e o perímetro de um retângulo.

    Args:
        comprimento (float): O comprimento do retângulo.
        largura (float): A largura do retângulo.

    Returns:
        tuple[float, float]: Uma tupla contendo a área e o perímetro do retângulo.
    """
    area = comprimento * largura
    perimetro = 2 * (comprimento + largura)
    return area, perimetro

# Leitura dos dados do usuário
comprimento_usuario = float(input())
largura_usuario = float(input())

# Chamada da função e desempacotamento dos resultados
area_calculada, perimetro_calculado = calcular_retangulo(comprimento_usuario, largura_usuario)

# Impressão dos resultados formatados
print(f"Área: {area_calculada:.2f}")
print(f"Perímetro: {perimetro_calculado:.2f}")
