"""Desenvolva um programa Python que ajude um aluno a calcular as estatísticas de suas notas em uma disciplina. O programa deve solicitar ao usuário que insira três notas (números de ponto flutuante), que representam as avaliações de três unidades. Em seguida, o programa deve utilizar uma função para calcular a média, a maior nota e a menor nota entre as três notas fornecidas.

Você deve implementar a função `calcular_estatisticas_notas` que siga os seguintes requisitos:
- Receba três argumentos: `nota1`, `nota2`, `nota3` (todos do tipo `float`).
- Calcule a média aritmética das três notas.
- Encontre a nota mais alta (`maior_nota`).
- Encontre a nota mais baixa (`menor_nota`).
- Retorne uma tupla contendo a média, a maior nota e a menor nota, nessa ordem.
- Assuma que as notas inseridas estarão no intervalo válido (por exemplo, de 0.0 a 10.0).
- Os resultados da média devem ser arredondados para duas casas decimais.

No programa principal, você deve:
1. Ler as três notas do usuário.
2. Chamar a função `calcular_estatisticas_notas` com as notas lidas.
3. Imprimir a média, a maior nota e a menor nota, formatando a média para duas casas decimais."""

def calcular_estatisticas_notas(nota1: float, nota2: float, nota3: float) -> tuple[float, float, float]:
    """
    Calcula a média, a maior e a menor nota de três notas fornecidas.

    Args:
        nota1 (float): A primeira nota.
        nota2 (float): A segunda nota.
        nota3 (float): A terceira nota.

    Returns:
        tuple[float, float, float]: Uma tupla contendo a média das notas
                                     (arredondada para duas casas decimais),
                                     a maior nota e a menor nota, nessa ordem.
    """
    media = (nota1 + nota2 + nota3) / 3
    maior_nota = max(nota1, nota2, nota3)
    menor_nota = min(nota1, nota2, nota3)

    return round(media, 2), maior_nota, menor_nota

# Leitura das notas do usuário
n1 = float(input())
n2 = float(input())
n3 = float(input())

# Chamada da função e desempacotamento dos resultados
media_final, maior_final, menor_final = calcular_estatisticas_notas(n1, n2, n3)

# Impressão dos resultados
print(f"Média das notas: {media_final:.2f}")
print(f"Maior nota: {maior_final}")
print(f"Menor nota: {menor_final}")
