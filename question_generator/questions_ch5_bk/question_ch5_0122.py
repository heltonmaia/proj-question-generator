"""Você foi contratado para criar uma ferramenta de processamento de listas numéricas. O objetivo é desenvolver uma função de 'ordem superior' que possa aplicar qualquer operação matemática a cada elemento de uma lista de números inteiros.

Crie as seguintes funções:
1.  `dobrar(numero: int) -> int`: Uma função simples que recebe um número inteiro e retorna o seu dobro.
2.  `quadrado(numero: int) -> int`: Uma função simples que recebe um número inteiro e retorna o seu quadrado.
3.  `aplicar_operacao_na_lista(operacao: callable, lista_numeros: list[int]) -> list[int]`: Esta é a função de ordem superior. Ela deve receber dois argumentos:
    *   `operacao`: Uma função (como `dobrar` ou `quadrado`) que será aplicada a cada elemento da `lista_numeros`.
    *   `lista_numeros`: Uma lista de números inteiros.
    A função deve retornar uma *nova lista* contendo os resultados da `operacao` aplicada a cada elemento da `lista_numeros`.

No programa principal, você deve:
*   Ler uma linha de números inteiros separados por espaço e converter para uma lista.
*   Aplicar a função `dobrar` a esta lista usando `aplicar_operacao_na_lista` e imprimir a nova lista resultante, precedida pela etiqueta "Dobro: ".
*   Aplicar a função `quadrado` a esta mesma lista usando `aplicar_operacao_na_lista` e imprimir a nova lista resultante, precedida pela etiqueta "Quadrado: ".

Exemplos de entrada e saída serão fornecidos para guiar sua implementação."""

def dobrar(numero: int) -> int:
    """
    Retorna o dobro de um número inteiro.
    """
    return numero * 2

def quadrado(numero: int) -> int:
    """
    Retorna o quadrado de um número inteiro.
    """
    return numero ** 2

def aplicar_operacao_na_lista(operacao: callable, lista_numeros: list[int]) -> list[int]:
    """
    Aplica uma função a cada elemento de uma lista de números.

    Args:
        operacao: A função a ser aplicada (e.g., dobrar, quadrado).
        lista_numeros: A lista de números inteiros.

    Returns:
        Uma nova lista com os resultados da operação aplicada.
    """
    return [operacao(num) for num in lista_numeros]

# Leitura da entrada
# Assume que a entrada é uma linha de números inteiros separados por espaço
entrada_str = input()
numeros = [int(x) for x in entrada_str.split()]

# Aplicando as operações e imprimindo os resultados
resultados_dobrar = aplicar_operacao_na_lista(dobrar, numeros)
print(f"Dobro: {resultados_dobrar}")

resultados_quadrado = aplicar_operacao_na_lista(quadrado, numeros)
print(f"Quadrado: {resultados_quadrado}")
