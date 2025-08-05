"""Crie uma função em Python chamada `analisar_desempenho_notas` que receba uma lista de números de ponto flutuante (representando notas de alunos) como argumento.

A função deve realizar duas tarefas principais:
1.  Calcular a média aritmética de todas as notas presentes na lista.
2.  Contar quantos alunos obtiveram uma nota estritamente superior à média calculada.

A função deve retornar esses dois valores como uma tupla: a média das notas (do tipo `float`) e a contagem de notas acima da média (do tipo `int`).

No programa principal, solicite ao usuário que digite uma sequência de notas (separadas por espaço). Converta essas notas em uma lista de números de ponto flutuante e, em seguida, chame a função `analisar_desempenho_notas` com essa lista. Finalmente, imprima a média calculada (formatada para duas casas decimais) e o número de notas que estão acima dessa média.

Certifique-se de que a função `analisar_desempenho_notas` inclua docstrings para documentação e type hints para clareza dos tipos de dados envolvidos."""

from typing import List, Tuple

def analisar_desempenho_notas(notas: List[float]) -> Tuple[float, int]:
    """
    Calcula a média de uma lista de notas e conta quantas notas são superiores à média.

    Args:
        notas (List[float]): Uma lista de números de ponto flutuante representando as notas dos alunos.

    Returns:
        Tuple[float, int]: Uma tupla contendo a média das notas (float) 
                           e o número de notas estritamente acima da média (int).
                           Retorna (0.0, 0) se a lista de notas for vazia.
    """
    if not notas:
        return 0.0, 0

    soma_notas = sum(notas)
    media = soma_notas / len(notas)
    
    notas_acima_media = 0
    for nota in notas:
        if nota > media:
            notas_acima_media += 1
            
    return media, notas_acima_media

# Programa principal
try:
    entrada_notas_str = input("Digite as notas separadas por espaço (ex: 7.5 8.0 6.0): ")
    # Converte a string de entrada em uma lista de floats
    notas_lista = [float(nota) for nota in entrada_notas_str.split()]

    media_calculada, num_acima_media = analisar_desempenho_notas(notas_lista)

    print(f"Média das notas: {media_calculada:.2f}")
    print(f"Número de notas acima da média: {num_acima_media}")
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números separados por espaço.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
