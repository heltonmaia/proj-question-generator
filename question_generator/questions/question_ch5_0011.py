"""Você foi encarregado de criar um programa Python que atue como uma calculadora de áreas para três formas geométricas distintas: **retângulo**, **círculo** e **triângulo**.

Para cada forma, o programa deverá:
1.  **Solicitar as dimensões necessárias** ao usuário (comprimento e largura para o retângulo; raio para o círculo; base e altura para o triângulo).
2.  **Utilizar uma função específica** para calcular a área da forma correspondente.
3.  **Exibir o resultado** da área calculada, formatado com duas casas decimais.

Implemente as seguintes funções:
*   `calcular_area_retangulo(comprimento, largura)`: Recebe o comprimento e a largura, e retorna a área do retângulo (`comprimento * largura`).
*   `calcular_area_circulo(raio)`: Recebe o raio e retorna a área do círculo (`π * raio²`).
*   `calcular_area_triangulo(base, altura)`: Recebe a base e a altura, e retorna a área do triângulo `((base * altura) / 2)`.

Certifique-se de importar o módulo `math` para utilizar a constante `math.pi` no cálculo da área do círculo."""

import math

def calcular_area_retangulo(comprimento: float, largura: float) -> float:
    """
    Calcula a área de um retângulo.

    Args:
        comprimento (float): O comprimento do retângulo.
        largura (float): A largura do retângulo.

    Returns:
        float: A área calculada do retângulo.
    """
    return comprimento * largura

def calcular_area_circulo(raio: float) -> float:
    """
    Calcula a área de um círculo.

    Args:
        raio (float): O raio do círculo.

    Returns:
        float: A área calculada do círculo.
    """
    return math.pi * (raio ** 2)

def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula a área de um triângulo.

    Args:
        base (float): A base do triângulo.
        altura (float): A altura do triângulo.

    Returns:
        float: A área calculada do triângulo.
    """
    return (base * altura) / 2

# --- Cálculo da Área do Retângulo ---
print("--- Cálculo da Área do Retângulo ---")
comp_ret = float(input("Digite o comprimento do retângulo: "))
larg_ret = float(input("Digite a largura do retângulo: "))
area_ret = calcular_area_retangulo(comp_ret, larg_ret)
print(f"A área do retângulo é: {area_ret:.2f}\n")

# --- Cálculo da Área do Círculo ---
print("--- Cálculo da Área do Círculo ---")
raio_circ = float(input("Digite o raio do círculo: "))
area_circ = calcular_area_circulo(raio_circ)
print(f"A área do círculo é: {area_circ:.2f}\n")

# --- Cálculo da Área do Triângulo ---
print("--- Cálculo da Área do Triângulo ---")
base_tri = float(input("Digite a base do triângulo: "))
alt_tri = float(input("Digite a altura do triângulo: "))
area_tri = calcular_area_triangulo(base_tri, alt_tri)
print(f"A área do triângulo é: {area_tri:.2f}")
