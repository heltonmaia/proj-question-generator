"""O objetivo é criar um programa que calcule a área e o perímetro de um retângulo. Você deverá implementar uma função que retorne ambos os valores de uma só vez, demonstrando o uso de múltiplos retornos.

1.  **Função `calcular_retangulo`**:
    *   Esta função deve receber dois parâmetros: `comprimento` (float) e `largura` (float).
    *   Dentro da função, calcule a **área** (comprimento \* largura) e o **perímetro** (2 \* (comprimento + largura)).
    *   A função deve retornar esses dois valores como uma tupla: `(area, perimetro)`.
    *   Inclua uma `docstring` clara e `type hints` para os parâmetros e o retorno.

2.  **Programa Principal**:
    *   Solicite ao usuário que insira o comprimento e a largura do retângulo.
    *   Chame a função `calcular_retangulo` com os valores fornecidos pelo usuário.
    *   Desempacote os valores retornados pela função em variáveis separadas (por exemplo, `area_calculada`, `perimetro_calculado`).
    *   Imprima a área e o perímetro calculados, formatando-os com duas casas decimais."""

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

# Programa Principal
comprimento_input = float(input())
largura_input = float(input())

area_calculada, perimetro_calculado = calcular_retangulo(comprimento_input, largura_input)

print(f"A área do retângulo é: {area_calculada:.2f}")
print(f"O perímetro do retângulo é: {perimetro_calculado:.2f}")
