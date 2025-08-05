"""Sua tarefa é criar uma função Python que calcule algumas estatísticas básicas para uma lista de números.

Desenvolva uma função chamada `analisar_estatisticas_lista` que receba um único parâmetro: uma lista de números (`list[float]`).

Esta função deve realizar as seguintes operações:
1.  Calcular a soma de todos os números na lista.
2.  Calcular a média aritmética dos números na lista.

A função deve retornar **dois valores**: a soma total e a média. Use uma tupla para o retorno dos múltiplos valores.

**Condição Especial:** Se a lista de entrada estiver vazia, a função deve retornar `(0.0, 0.0)` para a soma e a média, respectivamente, para evitar erros de divisão por zero.

Inclua uma `docstring` clara para a função, explicando seu propósito, parâmetros e o que ela retorna. Utilize `type hints` para os parâmetros e o retorno da função.

No programa principal, você deve ler uma série de números fornecidos pelo usuário (em uma única linha, separados por espaço), convertê-los em uma lista de números de ponto flutuante e, em seguida, chamar a função `analisar_estatisticas_lista` para obter a soma e a média. Finalmente, imprima os resultados formatados com duas casas decimais."""

def analisar_estatisticas_lista(numeros: list[float]) -> tuple[float, float]:
    """
    Calcula a soma e a média de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números (inteiros ou floats).

    Returns:
        tuple[float, float]: Uma tupla contendo a soma e a média dos números.
                              Retorna (0.0, 0.0) se a lista estiver vazia.
    """
    if not numeros:
        return 0.0, 0.0
    
    soma = sum(numeros)
    media = soma / len(numeros)
    return soma, media

# Lê a linha de entrada do usuário
entrada_raw = input()

# Converte a string de entrada para uma lista de floats
# Trata o caso de entrada vazia para criar uma lista vazia
if entrada_raw.strip() == "":
    lista_numeros = []
else:
    lista_numeros = [float(x) for x in entrada_raw.split()]

# Chama a função para analisar a lista
soma_total, media_total = analisar_estatisticas_lista(lista_numeros)

# Imprime os resultados formatados
print(f"Soma total: {soma_total:.2f}")
print(f"Média total: {media_total:.2f}")
