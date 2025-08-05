"""Você foi contratado(a) para desenvolver um sistema simples de análise de desempenho escolar. Sua tarefa é criar um programa Python que realize as seguintes operações:

1.  **Leitura de Notas:** Solicite ao usuário que insira as notas de um estudante em uma única linha, separadas por espaços (ex: `8.5 7.0 9.0`). As notas devem ser interpretadas como números de ponto flutuante.
2.  **Análise de Notas:** Crie uma função chamada `analisar_notas` que receba uma lista de notas (`list[float]`) como parâmetro. Esta função deve calcular e retornar três valores:
    *   A média aritmética das notas.
    *   A nota mais alta na lista.
    *   A nota mais baixa na lista.
    A função deve utilizar `docstrings` e `type hints` para documentar seus parâmetros e o tipo de retorno (uma tupla).
3.  **Exibição de Resultados:** No programa principal, após receber as notas e chamar a função `analisar_notas`, desempacote os valores retornados para variáveis distintas. Em seguida, exiba na tela:
    *   A média das notas (formatada para duas casas decimais).
    *   A nota mais alta (formatada para duas casas decimais).
    *   A nota mais baixa (formatada para duas casas decimais).
    *   Um "Status" indicando se o estudante foi "Aprovado" (se a média for igual ou superior a 7.0) ou "Reprovado" (se a média for inferior a 7.0).
4.  **Tratamento de Entrada:** O programa deve ser robusto para lidar com entradas de usuário inválidas. Se o usuário não digitar números ou digitar uma linha vazia, uma mensagem de erro apropriada deve ser exibida."""

def analisar_notas(notas: list[float]) -> tuple[float, float, float]:
    """
    Analisa uma lista de notas de um estudante, calculando a média,
    a nota mais alta e a nota mais baixa.

    Args:
        notas (list[float]): Uma lista de notas do estudante.

    Returns:
        tuple[float, float, float]: Uma tupla contendo a média, a nota mais alta
                                     e a nota mais baixa, nesta ordem.
                                     Retorna (0.0, 0.0, 0.0) se a lista de notas estiver vazia.
    """
    if not notas:
        return 0.0, 0.0, 0.0  # Retorna valores padrão para lista vazia

    media = sum(notas) / len(notas)
    nota_mais_alta = max(notas)
    nota_mais_baixa = min(notas)
    return media, nota_mais_alta, nota_mais_baixa

if __name__ == "__main__":
    entrada_raw = input("Digite as notas do estudante separadas por espaço (ex: 8.5 7.0 9.0): ")
    
    # Processa a entrada para obter uma lista de strings de notas
    notas_str = entrada_raw.strip().split()

    if not notas_str:
        print("Nenhuma nota foi inserida. Não é possível realizar a análise.")
    else:
        try:
            # Converte as strings de notas para float
            notas_aluno = [float(nota) for nota in notas_str]

            # Chama a função de análise e desempacota os resultados
            media_final, maior_nota, menor_nota = analisar_notas(notas_aluno)

            # Exibe os resultados formatados
            print(f"Média: {media_final:.2f}")
            print(f"Nota mais alta: {maior_nota:.2f}")
            print(f"Nota mais baixa: {menor_nota:.2f}")

            # Determina e exibe o status de aprovação
            if media_final >= 7.0:
                print("Status: Aprovado")
            else:
                print("Status: Reprovado")

        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números válidos separados por espaço.")
