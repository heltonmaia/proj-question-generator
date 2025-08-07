"""Você foi encarregado de desenvolver um programa Python capaz de aplicar diferentes operações matemáticas a uma lista de números fornecida pelo usuário. Para isso, você deve implementar uma abordagem modular utilizando funções, incluindo uma função de ordem superior.

Seu programa deve conter as seguintes funções:

1.  **`ler_lista_numeros()`**:
    *   Esta função deve solicitar ao usuário que insira uma sequência de números separados por espaço (ex: `'4 9 16 25 36'`).
    *   Ela deve converter essa sequência em uma lista de números do tipo `float` e retorná-la.

2.  **`processar_lista(operacao, lista_numeros)`**:
    *   Esta é uma função de ordem superior que receberá dois parâmetros:
        *   `operacao`: Uma função que representa a operação matemática a ser aplicada.
        *   `lista_numeros`: Uma lista de números (do tipo `float`).
    *   A função deve retornar uma **nova lista** contendo os resultados da aplicação da `operacao` a cada elemento de `lista_numeros`.

3.  **Funções de Operação Específicas**: Crie as seguintes funções que serão passadas como argumento para `processar_lista`:
    *   **`dobrar(x: float) -> float`**: Recebe um número `x` e retorna o dobro dele.
    *   **`quadrado(x: float) -> float`**: Recebe um número `x` e retorna o seu quadrado.
    *   **`raiz_quadrada(x: float) -> float`**: Recebe um número `x` e retorna a sua raiz quadrada. **Importe o módulo `math` para usar `math.sqrt()`**. Para este exercício, assuma que os números da lista serão sempre não-negativos ao chamar esta função. O resultado deve ser arredondado para duas casas decimais.

No programa principal, você deve:
*   Obter a lista de números do usuário utilizando a função `ler_lista_numeros()`.
*   Demonstrar o uso da função `processar_lista()` com cada uma das funções de operação (`dobrar`, `quadrado`, `raiz_quadrada`), imprimindo a lista resultante para cada caso."""

import math

def ler_lista_numeros() -> list[float]:
    """
    Solicita ao usuário uma sequência de números separados por espaço
    e retorna uma lista de floats.
    """
    entrada = input("Digite uma sequência de números separados por espaço: ")
    return [float(x) for x in entrada.split()]

def processar_lista(operacao, lista_numeros: list[float]) -> list[float]:
    """
    Aplica uma operação a cada elemento de uma lista de números.

    Args:
        operacao: Uma função que define a operação a ser aplicada.
        lista_numeros: A lista de números a ser processada.

    Returns:
        Uma nova lista com os resultados da operação aplicada.
    """
    return [operacao(num) for num in lista_numeros]

def dobrar(x: float) -> float:
    """
    Retorna o dobro de um número.
    """
    return x * 2

def quadrado(x: float) -> float:
    """
    Retorna o quadrado de um número.
    """
    return x ** 2

def raiz_quadrada(x: float) -> float:
    """
    Retorna a raiz quadrada de um número, arredondada para duas casas decimais.
    Assume que x será não-negativo.
    """
    return round(math.sqrt(x), 2)

# --- Programa Principal ---
numeros = ler_lista_numeros()

# Aplicando as operações e imprimindo os resultados
print(f"Lista original: {numeros}")

resultados_dobro = processar_lista(dobrar, numeros)
print(f"Resultados ao dobrar: {resultados_dobro}")

resultados_quadrado = processar_lista(quadrado, numeros)
print(f"Resultados ao elevar ao quadrado: {resultados_quadrado}")

resultados_raiz = processar_lista(raiz_quadrada, numeros)
print(f"Resultados da raiz quadrada: {resultados_raiz}")
