"""Crie um programa Python que seja capaz de analisar uma lista de números fornecidos pelo usuário e calcular suas estatísticas básicas. O programa deve:

1.  Solicitar ao usuário que insira uma sequência de números, separados por espaços, em uma única linha.
2.  Implementar uma função chamada `analisar_numeros` que receba uma lista de números de ponto flutuante (`list[float]`) como argumento.
3.  A função `analisar_numeros` deve calcular e retornar quatro valores: a soma total dos números, a média aritmética, o menor número e o maior número da lista. **Estes quatro valores devem ser retornados como uma tupla.**
4.  No programa principal, chame a função `analisar_numeros` com a lista fornecida pelo usuário e imprima os resultados de forma clara e formatada com duas casas decimais.

Certifique-se de que sua solução utilize `docstrings` para documentar a função e `type hints` para indicar os tipos dos parâmetros e do retorno, conforme boas práticas de programação."""

def analisar_numeros(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números de ponto flutuante.

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo a soma,
                                         a média, o menor e o maior número da lista,
                                         nesta ordem.
    Raises:
        ValueError: Se a lista de números estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista de números não pode estar vazia para esta análise.")
    
    soma = sum(numeros)
    media = soma / len(numeros)
    menor = min(numeros)
    maior = max(numeros)
    
    return soma, media, menor, maior

# Leitura da entrada do usuário
entrada_str = input() 
lista_str = entrada_str.split()

# Converte strings para floats
lista_numeros = [float(num) for num in lista_str]

# Chamada da função e exibição dos resultados
soma_total, media_calc, menor_valor, maior_valor = analisar_numeros(lista_numeros)

print(f"Soma: {soma_total:.2f}")
print(f"Média: {media_calc:.2f}")
print(f"Menor valor: {menor_valor:.2f}")
print(f"Maior valor: {maior_valor:.2f}")
