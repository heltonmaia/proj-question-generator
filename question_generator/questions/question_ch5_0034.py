"""Desenvolva um programa Python que calcule a área e o perímetro de um retângulo. Para isso, você deve criar uma função que receba o comprimento e a largura do retângulo como parâmetros e retorne ambos os valores calculados (área e perímetro) em uma única estrutura.

No programa principal, solicite ao usuário que insira o comprimento e a largura do retângulo. Em seguida, chame a função criada, desempacote os valores retornados e exiba a área e o perímetro com duas casas decimais de precisão.

Certifique-se de:
*   Definir uma função com type hints claros para os parâmetros e o retorno.
*   Incluir uma docstring para descrever o propósito da função, seus argumentos e o que ela retorna.
*   Apresentar a saída de forma clara e formatada.

**Fórmulas:**
*   Área = comprimento × largura
*   Perímetro = 2 × (comprimento + largura)"""

def calcular_area_perimetro_retangulo(comprimento: float, largura: float) -> tuple[float, float]:
    """
    Calcula a área e o perímetro de um retângulo.

    Args:
        comprimento (float): O comprimento do retângulo.
        largura (float): A largura do retângulo.

    Returns:
        tuple[float, float]: Uma tupla contendo a área e o perímetro do retângulo.
                             O primeiro elemento é a área, o segundo é o perímetro.
    """
    area = comprimento * largura
    perimetro = 2 * (comprimento + largura)
    return area, perimetro

# Programa principal
try:
    comprimento_input = float(input("Digite o comprimento do retângulo: "))
    largura_input = float(input("Digite a largura do retângulo: "))

    if comprimento_input <= 0 or largura_input <= 0:
        print("Comprimento e largura devem ser valores positivos.")
    else:
        area_calculada, perimetro_calculado = calcular_area_perimetro_retangulo(comprimento_input, largura_input)

        print(f"A área do retângulo é: {area_calculada:.2f}")
        print(f"O perímetro do retângulo é: {perimetro_calculado:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite números.")
