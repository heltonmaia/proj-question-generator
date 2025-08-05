"""Desenvolva um programa Python que demonstre a flexibilidade de passar funções como argumentos, um conceito fundamental em programação modular. Seu programa deve:

1.  **Ler uma lista de números:** Solicite ao usuário que digite uma série de números (inteiros ou decimais) separados por espaços em uma única linha. Converta essa entrada em uma lista de números de ponto flutuante.
2.  **Criar a função de processamento de lista:** Implemente uma função chamada `processar_lista(lista, operacao)` que aceita dois parâmetros: uma `lista` de números e uma `operacao` (que é uma outra função). Esta função `processar_lista` deve aplicar a `operacao` a cada elemento da `lista` de entrada e retornar uma *nova lista* contendo os resultados dessas operações.
3.  **Definir operações específicas:**
    *   Crie uma função regular (nomeada) chamada `triplicar_valor(x)` que retorna o triplo do número `x`.
    *   Utilize uma **função anônima (lambda)** diretamente como argumento para `processar_lista` para definir uma operação que calcula a metade de um número (`x / 2`).
4.  **Aplicar e exibir resultados:**
    *   Use a função `processar_lista` para aplicar `triplicar_valor` à lista de números lida do usuário.
    *   Use a função `processar_lista` novamente para aplicar a função lambda (cálculo da metade) à mesma lista original.
    *   Finalmente, imprima a lista original, a lista com os valores triplicados e a lista com os valores divididos pela metade. Todos os números de ponto flutuante nas listas de saída devem ser formatados com **duas casas decimais**."""

def processar_lista(lista: list[float | int], operacao) -> list[float]:
    """
    Aplica uma operação a cada elemento de uma lista e retorna uma nova lista.

    Args:
        lista: A lista de números a ser processada.
        operacao: A função a ser aplicada a cada elemento da lista.

    Returns:
        Uma nova lista com os resultados da operação aplicada, todos como float.
    """
    return [float(operacao(elemento)) for elemento in lista]

def triplicar_valor(x: float | int) -> float:
    """
    Retorna o triplo de um número.

    Args:
        x: O número a ser triplicado.

    Returns:
        O triplo do número.
    """
    return x * 3

def formatar_lista_para_impressao(lista_numeros: list) -> str:
    """
    Formata uma lista de números para string com duas casas decimais para floats.
    """
    return "[" + ", ".join([f"{num:.2f}" for num in lista_numeros]) + "]"

# 1. Leitura da lista de números
# A entrada esperada é uma linha com números separados por espaços.
numeros_originais_str = input()
numeros_originais = [float(num) for num in numeros_originais_str.split()]

# 3.1. Aplicando a função triplicar_valor
lista_triplicada = processar_lista(numeros_originais, triplicar_valor)

# 3.2. Aplicando uma função lambda para calcular a metade
lista_metade = processar_lista(numeros_originais, lambda x: x / 2)

# 4. Impressão dos resultados
print(f"Lista original: {formatar_lista_para_impressao(numeros_originais)}")
print(f"Lista triplicada: {formatar_lista_para_impressao(lista_triplicada)}")
print(f"Lista com a metade: {formatar_lista_para_impressao(lista_metade)}")
