"""Você foi encarregado de criar um sistema simples para analisar o desempenho de alunos com base em suas notas. Para isso, você deve desenvolver um programa Python que utilize funções para calcular e apresentar estatísticas importantes de uma lista de notas.

Sua tarefa é implementar uma função chamada `analisar_notas` que receba uma lista de números de ponto flutuante (representando as notas) como entrada. Esta função deve calcular e retornar os seguintes resultados:

1.  **Média das notas:** A média aritmética de todas as notas na lista.
2.  **Maior nota:** A nota mais alta encontrada na lista.
3.  **Menor nota:** A nota mais baixa encontrada na lista.
4.  **Status de aprovação:** Um valor booleano (`True` ou `False`) indicando se *todas* as notas na lista são iguais ou superiores a 7.0 (considerando 7.0 como a nota mínima para aprovação).

A função deve utilizar *type hints* para indicar os tipos dos parâmetros e do valor de retorno (que será uma tupla contendo a média, a maior nota, a menor nota e o status de aprovação). Caso a lista de notas esteja vazia, a função deve retornar `(0.0, 0.0, 0.0, False)`.

No programa principal, você deve:
- Solicitar ao usuário que insira as notas em uma única linha, separadas por espaços (ex: `8.5 7.0 9.2 6.5`).
- Converter essas notas para uma lista de números de ponto flutuante.
- Chamar a função `analisar_notas` com a lista de notas.
- Imprimir os resultados formatados com duas casas decimais para as notas (média, maior e menor), e o valor booleano para o status de aprovação."""

def analisar_notas(notas: list[float]) -> tuple[float, float, float, bool]:
    """
    Analisa uma lista de notas de alunos, calculando média, maior, menor nota
    e verificando se todas as notas são de aprovação (>= 7.0).

    Args:
        notas (list[float]): Uma lista de notas.

    Returns:
        tuple[float, float, float, bool]: Uma tupla contendo:
            - A média das notas.
            - A maior nota.
            - A menor nota.
            - True se todas as notas forem >= 7.0, False caso contrário.
            Retorna (0.0, 0.0, 0.0, False) se a lista de notas estiver vazia.
    """
    if not notas:
        return 0.0, 0.0, 0.0, False 

    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    
    todas_aprovadas = all(nota >= 7.0 for nota in notas)
    
    return media, maior_nota, menor_nota, todas_aprovadas

# Leitura de notas como uma linha de string separada por espaços
notas_str = input().split()
notas_aluno = [float(nota) for nota in notas_str]

# Chama a função e desempacota os resultados
media, maior, menor, aprovado = analisar_notas(notas_aluno)

# Imprime os resultados formatados
print(f"Média das notas: {media:.2f}")
print(f"Maior nota: {maior:.2f}")
print(f"Menor nota: {menor:.2f}")
print(f"Todas as notas foram de aprovação? {aprovado}")
