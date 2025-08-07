"""O Máximo Divisor Comum (MDC) de dois números inteiros não negativos é o maior inteiro que divide ambos os números sem deixar resto. O algoritmo de Euclides é um método eficiente para calcular o MDC e pode ser implementado de forma recursiva.

Sua tarefa é implementar uma função Python recursiva chamada `calcular_mdc` que receba dois números inteiros não negativos como entrada (`a` e `b`) e retorne o MDC desses números.

A lógica recursiva do algoritmo de Euclides é a seguinte:
*   **Condição base:** Se `b` for 0, o MDC é `a`.
*   **Passo recursivo:** Caso contrário, o MDC de `a` e `b` é o mesmo que o MDC de `b` e do resto da divisão de `a` por `b` (`a % b`).

Após implementar a função, o programa deve solicitar ao usuário dois números inteiros, chamar a função `calcular_mdc` com esses números e, em seguida, imprimir o resultado formatado."""

def calcular_mdc(a: int, b: int) -> int:
    """
    Calcula o Máximo Divisor Comum (MDC) de dois números inteiros não negativos
    usando o algoritmo de Euclides recursivo.

    Args:
        a (int): O primeiro número inteiro não negativo.
        b (int): O segundo número inteiro não negativo.

    Returns:
        int: O Máximo Divisor Comum (MDC) de 'a' e 'b'.
    """
    if b == 0:
        return a
    else:
        return calcular_mdc(b, a % b)

# Leitura da entrada
num1 = int(input())
num2 = int(input())

# Chamada da função e impressão do resultado
resultado_mdc = calcular_mdc(num1, num2)
print(f"O MDC de {num1} e {num2} é: {resultado_mdc}")
