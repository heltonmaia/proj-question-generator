""": Análise de Notas de Alunos

Crie um programa Python que auxilie um professor na análise de notas de seus alunos. O programa deve ser capaz de coletar notas, calcular estatísticas básicas e classificar o desempenho.

Sua solução deve incluir as seguintes funções:

1.  `ler_notas() -> list[float]`: Esta função deve solicitar ao usuário que insira as notas dos alunos, uma por uma. O usuário deve digitar 'fim' (sem aspas, em minúsculas) para indicar que terminou de inserir as notas. A função deve armazenar as notas válidas em uma lista de números de ponto flutuante e retorná-la.

2.  `analisar_desempenho(notas: list[float]) -> tuple[float, float, float, int, int]`: Esta função recebe uma lista de notas como parâmetro. Ela deve calcular e retornar uma tupla contendo, na seguinte ordem:
    *   A **média** das notas.
    *   A **nota mais alta** (máxima).
    *   A **nota mais baixa** (mínima).
    *   A **quantidade de notas aprovadas**, considerando a média mínima de **7.0** para aprovação.
    *   A **quantidade de notas reprovadas**.
    *   **Observação**: Se a lista de notas estiver vazia, a função deve retornar `(0.0, 0.0, 0.0, 0, 0)` para evitar erros de cálculo.

No programa principal:
*   Chame `ler_notas()` para obter a lista de notas do usuário.
*   Chame `analisar_desempenho()` com a lista obtida.
*   Imprima todos os resultados de forma clara, formatando a média, nota máxima e mínima com duas casas decimais.

**Objetivo Educacional:** Este exercício reforça o uso de funções para modularização do código, manipulação de listas, tratamento de entrada do usuário e o retorno de múltiplos valores via tuplas."""

from typing import List, Tuple

def ler_notas() -> List[float]:
    """
    Solicita ao usuário que insira as notas dos alunos.
    A entrada de notas termina quando o usuário digita 'fim'.

    Returns:
        Uma lista de números de ponto flutuante representando as notas.
    """
    notas = []
    while True:
        entrada = input()
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            # Ignora entradas que não são números válidos ou 'fim'
            pass 
    return notas

def analisar_desempenho(notas: List[float]) -> Tuple[float, float, float, int, int]:
    """
    Analisa uma lista de notas e retorna a média, nota mais alta, nota mais baixa,
    e a contagem de notas aprovadas/reprovadas.

    Args:
        notas: Uma lista de notas de ponto flutuante.

    Returns:
        Uma tupla contendo (media, nota_maxima, nota_minima, aprovados, reprovados).
        Retorna (0.0, 0.0, 0.0, 0, 0) se a lista estiver vazia.
    """
    if not notas:
        return 0.0, 0.0, 0.0, 0, 0

    media = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)

    aprovados = 0
    reprovados = 0
    for nota in notas:
        if nota >= 7.0:
            aprovados += 1
        else:
            reprovados += 1
            
    return media, nota_maxima, nota_minima, aprovados, reprovados

# Programa principal
notas_alunos = ler_notas()
media, maxima, minima, num_aprovados, num_reprovados = analisar_desempenho(notas_alunos)

if not notas_alunos:
    print("Nenhuma nota foi inserida para análise.")
else:
    print(f"Média das notas: {media:.2f}")
    print(f"Nota mais alta: {maxima:.2f}")
    print(f"Nota mais baixa: {minima:.2f}")
    print(f"Notas aprovadas (>= 7.0): {num_aprovados}")
    print(f"Notas reprovadas (< 7.0): {num_reprovados}")
