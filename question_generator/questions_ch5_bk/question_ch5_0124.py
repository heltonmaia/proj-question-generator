"""Você foi contratado para criar um programa Python que ajude a analisar um conjunto de dados numéricos. Sua tarefa é desenvolver uma solução que seja capaz de calcular a soma total e a média aritmética de uma sequência de números fornecida pelo usuário. O programa deve ser modularizado utilizando funções para organizar o código.

Para isso, você deve seguir as seguintes instruções:

1.  **Função para Análise de Números (`analisar_numeros`):**
    *   Crie uma função chamada `analisar_numeros` que receba uma lista de números de ponto flutuante (`float`) como parâmetro.
    *   Dentro dessa função, calcule a soma de todos os números na lista e a média desses números.
    *   A função deve retornar uma tupla contendo dois valores: a soma (tipo `float`) e a média (tipo `float`).
    *   **Regra Importante:** Se a lista de entrada for vazia, a função deve retornar `(0.0, 0.0)` para a soma e a média, respectivamente, para evitar erros de divisão por zero.
    *   Utilize `docstrings` e `type hints` para documentar sua função e indicar os tipos de parâmetros e retorno, conforme boas práticas de Python.

2.  **Programa Principal:**
    *   No programa principal, você deve solicitar ao usuário que digite uma sequência de números separados por espaços em uma única linha.
    *   Converta essa sequência de strings em uma lista de números de ponto flutuante (`float`). Lembre-se de tratar o caso em que o usuário pode digitar uma linha vazia.
    *   Passe a lista de números resultante para a função `analisar_numeros`.
    *   Finalmente, imprima os resultados da soma total e da média aritmética, formatados com duas casas decimais.

**Exemplo de interação:**

```
Digite os números separados por espaços: 10.5 5.0 12.75
Soma: 28.25
Média: 9.42
```"""

def analisar_numeros(lista_de_numeros: list[float]) -> tuple[float, float]:
    """
    Calcula a soma e a média de uma lista de números.

    Args:
        lista_de_numeros (list[float]): A lista de números a ser analisada.

    Returns:
        tuple[float, float]: Uma tupla contendo a soma total e a média dos números.
                             Retorna (0.0, 0.0) se a lista for vazia.
    """
    if not lista_de_numeros:
        return 0.0, 0.0
    
    soma = sum(lista_de_numeros)
    media = soma / len(lista_de_numeros)
    return soma, media

# Programa Principal
entrada_str = input("Digite os números separados por espaços: ")

# Converte a string de entrada em uma lista de floats
# Filtra strings vazias resultantes de múltiplos espaços ou entrada vazia
numeros_str = [num for num in entrada_str.split() if num]

# Converte cada string numérica para float
lista_de_numeros = [float(num) for num in numeros_str]

# Chama a função para analisar os números
soma_total, media_final = analisar_numeros(lista_de_numeros)

# Imprime os resultados formatados
print(f"Soma: {soma_total:.2f}")
print(f"Média: {media_final:.2f}")
