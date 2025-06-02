"""Crie um programa em Python que funcione como uma calculadora de área para diferentes formas geométricas, incluindo triângulo, círculo e retângulo. O programa deve apresentar um menu interativo ao usuário para que ele selecione a forma desejada e, em seguida, solicite as dimensões necessárias para calcular a área.

O programa deve ter as seguintes funcionalidades:

1.  **Menu de Opções:**
    *   Opção 1: Calcular a área de um triângulo (solicita base e altura).
    *   Opção 2: Calcular a área de um círculo (solicita raio).
    *   Opção 3: Calcular a área de um retângulo (solicita comprimento e largura).
    *   Opção 4: Sair do programa.
2.  **Funções Dedicadas:** Implemente funções separadas para o cálculo da área de cada forma:
    *   `area_triangulo(base: float, altura: float) -> float`
    *   `area_circulo(raio: float) -> float`
    *   `area_retangulo(comprimento: float, largura: float) -> float`
3.  **Cálculos e Saída:**
    *   Utilize a biblioteca `math` para obter o valor de pi (`math.pi`) no cálculo da área do círculo.
    *   Todos os resultados das áreas devem ser arredondados para **duas casas decimais**.
    *   A saída deve ser clara e indicar a área calculada.

O programa deve continuar exibindo o menu até que o usuário escolha a opção para sair."""

import math

def area_triangulo(base: float, altura: float) -> float:
    """
    Calcula a área de um triângulo.

    Args:
        base (float): A base do triângulo.
        altura (float): A altura do triângulo.

    Returns:
        float: A área do triângulo.
    """
    return (base * altura) / 2

def area_circulo(raio: float) -> float:
    """
    Calcula a área de um círculo.

    Args:
        raio (float): O raio do círculo.

    Returns:
        float: A área do círculo.
    """
    return math.pi * (raio ** 2)

def area_retangulo(comprimento: float, largura: float) -> float:
    """
    Calcula a área de um retângulo.

    Args:
        comprimento (float): O comprimento do retângulo.
        largura (float): A largura do retângulo.

    Returns:
        float: A área do retângulo.
    """
    return comprimento * largura

while True:
    print("\n--- Calculadora de Área de Formas Geométricas ---")
    print("1. Triângulo")
    print("2. Círculo")
    print("3. Retângulo")
    print("4. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            area = area_triangulo(base, altura)
            print(f"A área do triângulo é: {area:.2f}")
        elif opcao == 2:
            raio = float(input("Digite o raio do círculo: "))
            area = area_circulo(raio)
            print(f"A área do círculo é: {area:.2f}")
        elif opcao == 3:
            comprimento = float(input("Digite o comprimento do retângulo: "))
            largura = float(input("Digite a largura do retângulo: "))
            area = area_retangulo(comprimento, largura)
            print(f"A área do retângulo é: {area:.2f}")
        elif opcao == 4:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
