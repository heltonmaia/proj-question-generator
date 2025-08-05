"""Desenvolva um programa Python que calcule a área e o perímetro de um retângulo. O programa deve solicitar ao usuário que insira a largura e a altura do retângulo. Em seguida, utilize uma função para realizar os cálculos e retornar ambos os resultados.

A função deve ser nomeada `calcular_area_perimetro_retangulo` e receber a largura e a altura como parâmetros. Ela deve retornar uma tupla contendo a área e o perímetro, respectivamente.

No programa principal, após ler as dimensões, chame a função criada e exiba os resultados formatados com duas casas decimais.

**Fórmulas:**
*   **Área:** `largura * altura`
*   **Perímetro:** `2 * (largura + altura)`"""

def calcular_area_perimetro_retangulo(largura: float, altura: float) -> tuple[float, float]:
    """
    Calcula a área e o perímetro de um retângulo.

    Args:
        largura (float): A largura do retângulo.
        altura (float): A altura do retângulo.

    Returns:
        tuple[float, float]: Uma tupla contendo a área e o perímetro do retângulo.
    """
    area = largura * altura
    perimetro = 2 * (largura + altura)
    return area, perimetro

# Leitura das dimensões
largura_input = float(input())
altura_input = float(input())

# Chama a função para calcular a área e o perímetro
area_result, perimetro_result = calcular_area_perimetro_retangulo(largura_input, altura_input)

# Exibe os resultados formatados
print(f"A área do retângulo é: {area_result:.2f}")
print(f"O perímetro do retângulo é: {perimetro_result:.2f}")
