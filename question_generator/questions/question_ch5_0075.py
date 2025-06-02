"""O problema: Os professores precisam de uma ferramenta simples para analisar as notas de uma turma. Eles querem saber a média das notas e qual foi a nota mais alta obtida na avaliação.

Sua tarefa é criar um programa Python que utilize funções para realizar essa análise.

Especificações:
1.  **Função `analisar_notas`**:
    *   Deve receber como parâmetro uma lista de números de ponto flutuante (`float`), representando as notas dos alunos.
    *   Deve calcular a média das notas.
    *   Deve encontrar a nota mais alta na lista.
    *   **Retornar dois valores**: a média das notas e a nota mais alta, como uma tupla (`tuple[float, float]`).
    *   **Tratamento de casos especiais**: Se a lista de notas estiver vazia, a função deve retornar `(0.0, 0.0)` para evitar erros de divisão por zero ou ao tentar encontrar o máximo em uma lista vazia.

2.  **Programa Principal**:
    *   Leia uma linha de entrada contendo as notas dos alunos, separadas por espaços (o usuário pode digitar "7.5 8.0 6.0 9.5").
    *   Converta essas notas para `float` e armazene-as em uma lista.
    *   Chame a função `analisar_notas` com a lista de notas.
    *   Imprima a média formatada com duas casas decimais e a maior nota formatada com duas casas decimais, conforme os exemplos de saída."""

def analisar_notas(notas: list[float]) -> tuple[float, float]:
    """
    Calcula a média e a maior nota de uma lista de notas.

    Args:
        notas (list[float]): Uma lista de notas de alunos.

    Returns:
        tuple[float, float]: Uma tupla contendo a média das notas e a maior nota.
                              Se a lista estiver vazia, retorna (0.0, 0.0).
    """
    if not notas:
        return 0.0, 0.0

    soma = sum(notas)
    media = soma / len(notas)
    maior_nota = max(notas)

    return media, maior_nota

if __name__ == '__main__':
    # Lê a linha de entrada e divide em strings
    notas_str = input().split()

    # Converte cada string para float
    notas = [float(nota) for nota in notas_str]

    # Chama a função para analisar as notas
    media_calculada, maior_nota_calculada = analisar_notas(notas)

    # Imprime os resultados formatados
    print(f"Média das notas: {media_calculada:.2f}")
    print(f"Maior nota: {maior_nota_calculada:.2f}")
