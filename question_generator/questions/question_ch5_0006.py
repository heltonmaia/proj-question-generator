"""Você foi incumbido de criar um programa Python para realizar uma análise estatística básica em uma lista de números de ponto flutuante. O programa deve ser modularizado utilizando funções, com um foco especial na capacidade de uma função retornar múltiplos valores.

Sua tarefa é:

1.  **Definir uma Função `analisar_estatisticas_lista`**:
    *   Esta função deve aceitar um único argumento: uma lista de números de ponto flutuante (`list[float]`).
    *   Ela deve calcular a **soma**, a **média**, o **valor mínimo** e o **valor máximo** de todos os números na lista.
    *   A função deve retornar esses quatro valores em uma única tupla, na seguinte ordem: `(soma, media, minimo, maximo)`.
    *   Inclua uma `docstring` clara e `type hints` para documentar a função, conforme as boas práticas de Python.

2.  **No Programa Principal**:
    *   O programa deve ler uma única linha de entrada contendo números de ponto flutuante separados por espaços (ex: "10.5 20.0 5.5 15.0 25.0").
    *   Converta esses números para uma lista de `float`.
    *   Chame a função `analisar_estatisticas_lista` com essa lista.
    *   Desempacote os valores retornados em variáveis separadas.
    *   Imprima os resultados de forma clara e formatada, arredondando os valores numéricos para duas casas decimais.

Considere que a lista de entrada nunca será vazia para este exercício."""

def analisar_estatisticas_lista(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, valor mínimo e valor máximo de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números de ponto flutuante.

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo (soma, media, minimo, maximo).
    """
    soma_total = sum(numeros)
    media_total = soma_total / len(numeros)
    minimo_valor = min(numeros)
    maximo_valor = max(numeros)

    return soma_total, media_total, minimo_valor, maximo_valor

# Programa principal
try:
    # Leitura da entrada: uma linha com números separados por espaço
    entrada_str = input()
    numeros_float = [float(x) for x in entrada_str.split()]

    soma, media, minimo, maximo = analisar_estatisticas_lista(numeros_float)

    print(f"Soma: {soma:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Mínimo: {minimo:.2f}")
    print(f"Máximo: {maximo:.2f}")

except ValueError:
    print("Entrada inválida. Certifique-se de inserir números de ponto flutuante separados por espaços.")
except ZeroDivisionError:
    print("A lista de números não pode ser vazia.") # Embora o enunciado diga que não será, é boa prática.
