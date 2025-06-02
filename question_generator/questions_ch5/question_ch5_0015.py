"""Desenvolva um programa Python que calcule a média de três notas de um aluno e, com base nessa média, determine o seu status. Para isso, você deve criar uma função específica que utilize os conceitos de funções com retorno de múltiplos valores.

Sua solução deve incluir:
1.  Uma função chamada `analisar_notas` que receba três parâmetros de tipo `float` (representando as notas `nota1`, `nota2` e `nota3`).
2.  Dentro da função, calcule a média aritmética das três notas.
3.  Com base na média calculada, determine o status do aluno, seguindo as seguintes regras:
    *   "Aprovado" se a média for igual ou superior a 7.0.
    *   "Recuperação" se a média for entre 5.0 (inclusive) e 6.9 (inclusive).
    *   "Reprovado" se a média for inferior a 5.0.
4.  A função `analisar_notas` deve retornar uma tupla contendo dois valores: a média calculada (tipo `float`) e o status do aluno (tipo `str`).
5.  No programa principal, solicite ao usuário que insira as três notas (uma por linha). Em seguida, chame a função `analisar_notas` com os valores fornecidos e imprima a média e o status formatados. A média deve ser exibida com duas casas decimais.

Utilize docstrings e type hints na sua função para melhorar a clareza e documentação do código, conforme boas práticas de programação em Python."""

def analisar_notas(nota1: float, nota2: float, nota3: float) -> tuple[float, str]:
    """
    Calcula a média de três notas e determina o status do aluno.

    Args:
        nota1 (float): A primeira nota.
        nota2 (float): A segunda nota.
        nota3 (float): A terceira nota.

    Returns:
        tuple[float, str]: Uma tupla contendo a média das notas (float) 
                           e o status do aluno (str).
                           O status pode ser "Aprovado", "Recuperação" ou "Reprovado".
    """
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0:
        status = "Aprovado"
    elif media >= 5.0:
        status = "Recuperação"
    else:
        status = "Reprovado"
    
    return media, status

# Leitura das notas do usuário
n1 = float(input())
n2 = float(input())
n3 = float(input())

# Chamada da função e desempacotamento dos resultados
media_final, status_final = analisar_notas(n1, n2, n3)

# Impressão dos resultados formatados
print(f"Média: {media_final:.2f}")
print(f"Status: {status_final}")
