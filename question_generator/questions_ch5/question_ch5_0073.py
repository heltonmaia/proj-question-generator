"""Você foi incumbido de desenvolver um sistema simples para ajudar um professor a analisar o desempenho dos alunos. Sua tarefa é criar um programa Python que utilize funções para processar uma lista de notas e retornar informações estatísticas importantes.

Para isso, siga os passos abaixo:

1.  Crie uma função chamada `analisar_notas` que receba uma lista de números (`list[float]`) como argumento.
2.  Esta função deve calcular e retornar os seguintes valores, nesta ordem, como uma tupla:
    *   A **soma total** das notas.
    *   A **média** das notas.
    *   A **maior nota** encontrada na lista.
    *   A **menor nota** encontrada na lista.
    *   Um valor booleano (`bool`) indicando se a **lista estava vazia** (`True` se vazia, `False` caso contrário).
3.  A função deve lidar graciosamente com o caso de uma lista de notas vazia. Se a lista estiver vazia, a soma, média, maior e menor nota devem ser retornados como `0.0`. O valor booleano deve indicar `True`.
4.  Utilize `docstrings` e `type hints` para documentar a função, conforme as boas práticas de Python.
5.  No programa principal, solicite ao usuário que insira as notas separadas por espaços em uma única linha. Converta essa entrada em uma lista de números de ponto flutuante.
6.  Chame a função `analisar_notas` com a lista obtida.
7.  Por fim, exiba os resultados retornados pela função de forma clara e formatada. Se a lista estiver vazia, uma mensagem apropriada deve ser exibida. A média deve ser formatada com duas casas decimais."""

from typing import List, Tuple

def analisar_notas(notas: List[float]) -> Tuple[float, float, float, float, bool]:
    """
    Analisa uma lista de notas de alunos, calculando soma, média,
    maior nota, menor nota e indicando se a lista estava vazia.

    Args:
        notas (List[float]): Uma lista de notas.

    Returns:
        Tuple[float, float, float, float, bool]: Uma tupla contendo:
            - A soma total das notas.
            - A média das notas.
            - A maior nota.
            - A menor nota.
            - Um booleano True se a lista estiver vazia, False caso contrário.
            Retorna 0.0 para soma, média, maior e menor se a lista for vazia.
    """
    if not notas:
        return 0.0, 0.0, 0.0, 0.0, True
    
    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)
    
    return soma, media, maior, menor, False

# Programa principal
entrada_str = input()
notas_str = entrada_str.split()

# Converte strings para float
notas_float = [float(nota) for nota in notas_str]

soma_res, media_res, maior_res, menor_res, lista_vazia = analisar_notas(notas_float)

if lista_vazia:
    print("Nenhuma nota inserida para análise.")
else:
    print("Notas analisadas:")
    print(f"Soma: {soma_res}")
    print(f"Média: {media_res:.2f}")
    print(f"Maior nota: {maior_res}")
    print(f"Menor nota: {menor_res}")
