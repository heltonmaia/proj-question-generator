"""Crie um programa Python que defina uma função para calcular a idade de uma pessoa e classificar sua geração com base no ano de nascimento.

A função, nomeada `classificar_pessoa`, deve receber dois parâmetros: o nome da pessoa (string) e o ano de nascimento (inteiro). Ela deve retornar dois valores:
1.  A idade atual da pessoa (considerando o ano de 2024 como o ano atual).
2.  A classificação da geração da pessoa, de acordo com as seguintes faixas:
    *   **Geração Z:** Nascidos entre 1997 e 2012
    *   **Millennials:** Nascidos entre 1981 e 1996
    *   **Geração X:** Nascidos entre 1965 e 1980
    *   **Baby Boomers:** Nascidos entre 1946 e 1964
    *   **Outros:** Para anos de nascimento fora das faixas especificadas acima (incluindo anos futuros ou muito antigos).

Após definir a função, o programa principal deve solicitar ao usuário o nome e o ano de nascimento. Em seguida, ele deve chamar a função `classificar_pessoa` e imprimir os resultados formatados conforme os exemplos de saída."""

def classificar_pessoa(nome: str, ano_nascimento: int) -> tuple[int, str]:
    """
    Calcula a idade de uma pessoa e classifica sua geração.

    Args:
        nome (str): O nome da pessoa.
        ano_nascimento (int): O ano de nascimento da pessoa.

    Returns:
        tuple[int, str]: Uma tupla contendo a idade e a classificação da geração.
    """
    ano_atual = 2024
    idade = ano_atual - ano_nascimento
    
    if 1997 <= ano_nascimento <= 2012:
        geracao = "Geração Z"
    elif 1981 <= ano_nascimento <= 1996:
        geracao = "Millennials"
    elif 1965 <= ano_nascimento <= 1980:
        geracao = "Geração X"
    elif 1946 <= ano_nascimento <= 1964:
        geracao = "Baby Boomers"
    else:
        geracao = "Outros"
        
    return idade, geracao

# Programa principal
nome_usuario = input("Digite o nome da pessoa: ")
ano_nascimento_usuario = int(input("Digite o ano de nascimento: "))

idade_pessoa, geracao_pessoa = classificar_pessoa(nome_usuario, ano_nascimento_usuario)

print(f"Nome: {nome_usuario}")
print(f"Idade: {idade_pessoa} anos")
print(f"Geração: {geracao_pessoa}")
