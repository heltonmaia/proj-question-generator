"""Desenvolva um programa em Python que funcione como uma calculadora de área para diferentes formas geométricas: triângulo, círculo e retângulo. O programa deve receber a escolha do usuário por meio de um número (1 para triângulo, 2 para círculo, 3 para retângulo, 4 para sair) e, em seguida, solicitar as dimensões necessárias para calcular a área da forma escolhida.

O programa deve incluir as seguintes funções:
- `area_triangulo(base, altura)`: Recebe a base e a altura de um triângulo e retorna sua área.
- `area_circulo(raio)`: Recebe o raio de um círculo e retorna sua área.
- `area_retangulo(comprimento, largura)`: Recebe o comprimento e a largura de um retângulo e retorna sua área.

No corpo principal do programa, você deve:
1. Ler a opção do usuário (um número inteiro de 1 a 4).
2. Com base na opção, solicitar as dimensões necessárias (base e altura para triângulo; raio para círculo; comprimento e largura para retângulo).
3. Chamar a função de cálculo de área apropriada.
4. Imprimir a área calculada, formatada para duas casas decimais, ou a mensagem "Programa encerrado." se a opção for 4. Para opções inválidas, imprima "Opção inválida.".

**Observações:**
- Utilize a biblioteca `math` para obter o valor de π (pi) nos cálculos do círculo.
- Arredonde todos os resultados de área para duas casas decimais."""

import math

def area_triangulo(base: float, altura: float) -> float:
    """Calcula a área de um triângulo."""
    return (base * altura) / 2

def area_circulo(raio: float) -> float:
    """Calcula a área de um círculo."""
    return math.pi * (raio ** 2)

def area_retangulo(comprimento: float, largura: float) -> float:
    """Calcula a área de um retângulo."""
    return comprimento * largura

# Leitura da opção
opcao = input()

if opcao == '1':
    base = float(input())
    altura = float(input())
    area = area_triangulo(base, altura)
    print(f"A área do triângulo é: {area:.2f}")
elif opcao == '2':
    raio = float(input())
    area = area_circulo(raio)
    print(f"A área do círculo é: {area:.2f}")
elif opcao == '3':
    comprimento = float(input())
    largura = float(input())
    area = area_retangulo(comprimento, largura)
    print(f"A área do retângulo é: {area:.2f}")
elif opcao == '4':
    print("Programa encerrado.")
else:
    print("Opção inválida.")
