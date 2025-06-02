"""Crie um programa em Python que demonstre o uso de funções de ordem superior, ou seja, funções que podem receber outras funções como argumentos. Seu programa deve permitir aplicar diferentes operações matemáticas a uma lista de números inteiros.

Sua tarefa é implementar as seguintes funções:

1.  `dobro(numero: int) -> int`: Uma função simples que recebe um número inteiro e retorna o dobro desse número.
2.  `triplo(numero: int) -> int`: Uma função simples que recebe um número inteiro e retorna o triplo desse número.
3.  `quadrado(numero: int) -> int`: Uma função simples que recebe um número inteiro e retorna o quadrado desse número.
4.  `processar_lista(lista: list[int], operacao: callable) -> list[int]`: Esta é a função principal. Ela deve receber uma lista de números inteiros e uma outra função (`operacao`). Para cada número na lista, `processar_lista` deve aplicar a `operacao` fornecida e retornar uma *nova lista* contendo os resultados.

No programa principal, você deve:
- Solicitar ao usuário que insira uma sequência de números inteiros, separados por espaços.
- Converter essa entrada em uma lista de inteiros.
- Utilizar a função `processar_lista` para calcular e exibir:
    - A lista com o dobro de cada número.
    - A lista com o triplo de cada número.
    - A lista com o quadrado de cada número.

Certifique-se de usar `docstrings` e `type hints` para documentar suas funções, conforme as boas práticas de Python. O programa deve lidar com entradas vazias ou inválidas."""

from typing import Callable

def dobro(numero: int) -> int:
    """
    Calcula o dobro de um número inteiro.

    Args:
        numero: O número inteiro a ser dobrado.

    Returns:
        O dobro do número.
    """
    return numero * 2

def triplo(numero: int) -> int:
    """
    Calcula o triplo de um número inteiro.

    Args:
        numero: O número inteiro a ser triplicado.

    Returns:
        O triplo do número.
    """
    return numero * 3

def quadrado(numero: int) -> int:
    """
    Calcula o quadrado de um número inteiro.

    Args:
        numero: O número inteiro a ser elevado ao quadrado.

    Returns:
        O quadrado do número.
    """
    return numero ** 2

def processar_lista(lista: list[int], operacao: Callable[[int], int]) -> list[int]:
    """
    Aplica uma função de operação a cada elemento de uma lista de números.

    Args:
        lista: Uma lista de números inteiros.
        operacao: Uma função que recebe um inteiro e retorna um inteiro,
                  a ser aplicada a cada elemento da lista.

    Returns:
        Uma nova lista contendo os resultados da operação aplicada a cada elemento.
    """
    return [operacao(elemento) for elemento in lista]

if __name__ == "__main__":
    entrada_str = input("Digite uma sequência de números inteiros separados por espaços: ")
    
    numeros: list[int] = []
    if entrada_str.strip() == "":
        print("A lista de números está vazia.")
    else:
        try:
            numeros = [int(n) for n in entrada_str.split()]
            
            print(f"Lista original: {numeros}")

            # Calculando o dobro de cada número na lista
            resultados_dobro = processar_lista(numeros, dobro)
            print(f"Dobro de cada número: {resultados_dobro}")

            # Calculando o triplo de cada número na lista
            resultados_triplo = processar_lista(numeros, triplo)
            print(f"Triplo de cada número: {resultados_triplo}")

            # Calculando o quadrado de cada número na lista
            resultados_quadrado = processar_lista(numeros, quadrado)
            print(f"Quadrado de cada número: {resultados_quadrado}")
            
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros separados por espaços.")
