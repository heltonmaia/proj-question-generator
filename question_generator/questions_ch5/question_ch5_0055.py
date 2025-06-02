"""Desenvolva uma função em Python que receba uma lista de números (inteiros ou decimais) e calcule duas estatísticas básicas sobre essa lista: a soma de todos os seus elementos e a média aritmética desses elementos. A função deve retornar ambos os valores.

O programa principal deve ser responsável por:
1.  Ler uma sequência de números da entrada, onde os números são separados por espaços.
2.  Converter essa sequência para uma lista de números decimais (`float`).
3.  Chamar a função desenvolvida, passando a lista de números como argumento.
4.  Imprimir os resultados da soma e da média, formatando a média com duas casas decimais.

**Observação:** Se a lista de entrada for vazia, a soma deve ser 0.0 e a média também 0.0 para evitar erros de divisão por zero. Inclua uma docstring e type hints para clareza e boa prática de código."""

def calcular_estatisticas(numeros: list[float]) -> tuple[float, float]:
    """
    Calcula a soma e a média de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números (inteiros ou decimais).

    Returns:
        tuple[float, float]: Uma tupla contendo a soma total dos números
                              e a média aritmética. Se a lista for vazia,
                              retorna (0.0, 0.0).
    """
    soma_total = sum(numeros)
    if not numeros:
        media_total = 0.0
    else:
        media_total = soma_total / len(numeros)
    
    return soma_total, media_total

# Bloco principal para leitura de entrada e exibição de saída
entrada_str = input()
if entrada_str.strip() == "":
    lista_numeros = []
else:
    lista_numeros = [float(x) for x in entrada_str.split()]

soma_resultado, media_resultado = calcular_estatisticas(lista_numeros)

print(f"Soma: {soma_resultado:.2f}")
print(f"Média: {media_resultado:.2f}")
