"""Imagine que você tem uma lista de números. O objetivo é calcular o n-ésimo número da sequência de Fibonacci para cada número dessa lista e imprimir a soma total desses números.

A sequência de Fibonacci é como uma escada em espiral, onde cada número é a soma dos dois anteriores. Ela começa com 0 e 1, e continua infinitamente: 0, 1, 1, 2, 3, 5, 8, 13, 21…

Para isso, você precisará criar duas funções recursivas:

1.  **`fibonacci(n)`**: Essa função receberá um número inteiro `n` como entrada e, usando a recursão, calculará e retornará o n-ésimo número correspondente na sequência de Fibonacci. As condições de base são: `fibonacci(0)` deve retornar 0 e `fibonacci(1)` deve retornar 1.
2.  **`soma_recursiva(lista_numeros)`**: Essa função receberá uma lista de números inteiros como argumento e, novamente usando a recursão, somará todos os elementos dessa lista e retornará o total. A condição de base é quando a lista está vazia, devendo retornar 0.

No programa principal, você deve:
- Ler uma linha de entrada contendo números inteiros separados por vírgulas (ex: "1,2,3,4,5").
- Converter essa entrada em uma lista de inteiros.
- Para cada número na lista, calcular o n-ésimo Fibonacci usando a função `fibonacci`.
- Armazenar os resultados do Fibonacci em uma nova lista.
- Calcular a soma total dos números na lista de resultados do Fibonacci usando a função `soma_recursiva`.
- Imprimir na tela a soma total."""

def fibonacci(n: int) -> int:
    """
    Calcula o n-ésimo número da sequência de Fibonacci de forma recursiva.

    Args:
        n (int): O índice do número na sequência de Fibonacci a ser calculado.

    Returns:
        int: O n-ésimo número da sequência de Fibonacci.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def soma_recursiva(lista_numeros: list[int]) -> int:
    """
    Soma todos os elementos de uma lista de números inteiros de forma recursiva.

    Args:
        lista_numeros (list[int]): A lista de números a ser somada.

    Returns:
        int: A soma de todos os elementos da lista.
    """
    if not lista_numeros: # Condição base: lista vazia
        return 0
    else:
        # Pega o primeiro elemento e soma com a soma recursiva do restante da lista
        return lista_numeros[0] + soma_recursiva(lista_numeros[1:])

# Leitura da entrada
entrada_str = input()
numeros_input = [int(x.strip()) for x in entrada_str.split(',')]

# Calcular Fibonacci para cada número e armazenar em uma nova lista
resultados_fibonacci = []
for num in numeros_input:
    resultados_fibonacci.append(fibonacci(num))

# Calcular a soma total dos resultados de Fibonacci
soma_total_fib = soma_recursiva(resultados_fibonacci)

# Imprimir o resultado
print(soma_total_fib)
