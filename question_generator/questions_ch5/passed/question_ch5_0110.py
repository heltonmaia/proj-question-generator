"""Desenvolva um programa Python para auxiliar na análise do desempenho escolar de um aluno. O programa deve ser capaz de receber uma série de notas e, a partir delas, calcular a média e identificar a maior nota obtida.

Para isso, siga as instruções:

1.  **Leitura de Entrada:** O programa deve ler uma única linha de entrada contendo diversas notas (números de ponto flutuante), separadas por espaços.
2.  **Conversão para Lista:** Converta essas notas em uma lista de números de ponto flutuante (`float`).
3.  **Função `analisar_notas`:**
    *   Crie uma função chamada `analisar_notas` que receba como parâmetro uma lista de notas (`list[float]`).
    *   Esta função deve calcular a média aritmética de todas as notas na lista.
    *   Ela também deve encontrar a maior nota presente na lista.
    *   A função deve retornar esses dois valores como uma tupla: `(media, maior_nota)`.
    *   **Tratamento de Exceção:** Se a lista de notas estiver vazia, a função deve retornar `(0.0, 0.0)` para evitar erros de divisão por zero ou ao tentar encontrar o máximo em uma lista vazia.
4.  **Programa Principal:**
    *   No programa principal, chame a função `analisar_notas` com a lista de notas lida da entrada.
    *   Imprima os resultados formatados com duas casas decimais, no seguinte formato: `"Média das notas: X.XX, Maior nota: Y.YY"`.

**Exemplo:**
Se a entrada for "7.5 8.0 6.0", a média é 7.166... e a maior nota é 8.0. A saída esperada seria "Média das notas: 7.17, Maior nota: 8.00"."""

def analisar_notas(notas: list[float]) -> tuple[float, float]:
    """
    Calcula a média e a maior nota de uma lista de notas.

    Args:
        notas (list[float]): Uma lista de notas numéricas.

    Returns:
        tuple[float, float]: Uma tupla contendo a média das notas e a maior nota.
                             Se a lista for vazia, retorna (0.0, 0.0).
    """
    if not notas:
        return 0.0, 0.0
    
    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    return media, maior_nota

# Leitura da entrada
entrada_str = input()

# Converte a string de entrada para uma lista de floats
notas = []
if entrada_str.strip(): # Verifica se a linha não está vazia ou contém apenas espaços
    notas_str = entrada_str.split()
    notas = [float(nota) for nota in notas_str]

# Chama a função e desempacota os resultados
media_calculada, maior_nota_encontrada = analisar_notas(notas)

# Imprime os resultados formatados
print(f"Média das notas: {media_calculada:.2f}, Maior nota: {maior_nota_encontrada:.2f}")
