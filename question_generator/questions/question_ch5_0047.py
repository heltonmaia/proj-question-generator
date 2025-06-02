"""Sua tarefa é criar um programa em Python que ajude a analisar o desempenho de um aluno com base em suas notas. O programa deve primeiro solicitar ao usuário que insira **cinco notas** (valores decimais), uma por uma. Em seguida, você deve implementar uma função que receba essas cinco notas como argumentos individuais e retorne uma tupla contendo a menor nota, a maior nota e a média aritmética dessas notas. Finalmente, o programa principal deve exibir esses resultados de forma formatada.

A função deve ser chamada `analisar_desempenho_aluno` e deve ter a seguinte assinatura: `analisar_desempenho_aluno(n1: float, n2: float, n3: float, n4: float, n5: float) -> tuple[float, float, float]`.

**Observações:**
-   Não é necessário tratar entradas inválidas (assuma que o usuário sempre digitará números válidos).
-   As notas de saída (menor, maior, média) devem ser formatadas para duas casas decimais.
-   Certifique-se de incluir `docstrings` e `type hints` para a função, seguindo as boas práticas de Python."""

from typing import Tuple

def analisar_desempenho_aluno(n1: float, n2: float, n3: float, n4: float, n5: float) -> Tuple[float, float, float]:
    """
    Analisa cinco notas de um aluno e retorna a menor, a maior e a média.

    Args:
        n1 (float): Primeira nota.
        n2 (float): Segunda nota.
        n3 (float): Terceira nota.
        n4 (float): Quarta nota.
        n5 (float): Quinta nota.

    Returns:
        tuple[float, float, float]: Uma tupla contendo (menor_nota, maior_nota, media_das_notas).
    """
    notas = [n1, n2, n3, n4, n5]
    
    menor_nota = min(notas)
    maior_nota = max(notas)
    media_das_notas = sum(notas) / len(notas)
    
    return menor_nota, maior_nota, media_das_notas

# Parte principal do programa
print("Por favor, insira as cinco notas do aluno:")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())

menor, maior, media = analisar_desempenho_aluno(nota1, nota2, nota3, nota4, nota5)

print(f"Menor nota: {menor:.2f}")
print(f"Maior nota: {maior:.2f}")
print(f"Média das notas: {media:.2f}")
