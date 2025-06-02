"""Você foi contratado para criar um pequeno sistema de análise de desempenho para estudantes. O sistema deve receber uma lista de notas (números de ponto flutuante) e, em seguida, calcular e retornar a soma total, a média, a nota mais alta e a nota mais baixa dessa lista.

Sua tarefa é implementar uma função Python chamada `analisar_notas` que aceita uma lista de notas como argumento. Esta função deve:
1. Calcular a soma de todas as notas.
2. Calcular a média das notas.
3. Encontrar a nota mais alta (máxima).
4. Encontrar a nota mais baixa (mínima).

A função deve retornar esses quatro valores em uma tupla, nesta ordem: (soma, media, nota_maxima, nota_minima).

No programa principal, solicite ao usuário que insira uma série de notas (separadas por espaços) e, após converter essas notas para uma lista de `float`, chame a função `analisar_notas`. Finalmente, imprima os resultados de forma clara e formatada com duas casas decimais."""

def analisar_notas(notas: list[float]) -> tuple[float, float, float, float]:
    """
    Analisa uma lista de notas, calculando a soma, média, nota máxima e mínima.

    Args:
        notas (list[float]): Uma lista de notas de ponto flutuante.
                             Assume-se que a lista não estará vazia.

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo a soma, média,
                                           nota máxima e nota mínima, respectivamente.
    """
    soma = sum(notas)
    media = soma / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)
    return soma, media, nota_maxima, nota_minima

# Leitura da entrada do usuário como uma string de notas separadas por espaço
notas_str = input()

# Converte a string de notas para uma lista de floats
# Utiliza uma compreensão de lista para converter cada parte da string em float
notas_lista = [float(nota) for nota in notas_str.split()]

# Chama a função para analisar as notas e desempacota os resultados
soma_total, media_final, nota_alta, nota_baixa = analisar_notas(notas_lista)

# Imprime os resultados formatados com duas casas decimais
print(f"Soma das notas: {soma_total:.2f}")
print(f"Média das notas: {media_final:.2f}")
print(f"Nota mais alta: {nota_alta:.2f}")
print(f"Nota mais baixa: {nota_baixa:.2f}")
