"""Desenvolva um programa Python que determine o menor e o maior número entre três valores fornecidos pelo usuário. Para isso, o programa deve modularizar a lógica utilizando duas funções principais:

1.  Uma função `ler_numeros()`: Esta função não receberá parâmetros. Ela será responsável por solicitar ao usuário que insira três números (podem ser inteiros ou decimais) e deverá retornar esses três valores como uma tupla.
2.  Uma função `encontrar_menor_maior(n1, n2, n3)`: Esta função receberá os três números como parâmetros. Ela será responsável por identificar qual deles é o menor e qual é o maior. A função deve retornar uma tupla contendo o menor e o maior valor, **nesta ordem**.

No programa principal, você deve:
*   Chamar a função `ler_numeros()` para obter as entradas do usuário.
*   Em seguida, passar esses valores para a função `encontrar_menor_maior()`.
*   Por fim, exibir os resultados de forma clara e formatada, indicando qual é o menor e qual é o maior número.

**Exemplo de Interação:**

```
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8
O menor número é: 5.0
O maior número é: 10.0
```"""

def ler_numeros() -> tuple[float, float, float]:
    """
    Solicita ao usuário que insira três números e os retorna como uma tupla de floats.
    """
    print("Por favor, digite três números:")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    return num1, num2, num3

def encontrar_menor_maior(n1: float, n2: float, n3: float) -> tuple[float, float]:
    """
    Recebe três números floats e retorna uma tupla com o menor e o maior valor.
    """
    menor = min(n1, n2, n3)
    maior = max(n1, n2, n3)
    return menor, maior

# Programa principal
if __name__ == "__main__":
    # Obtém os números do usuário usando a função ler_numeros
    num1_in, num2_in, num3_in = ler_numeros()
    
    # Encontra o menor e o maior número usando a função encontrar_menor_maior
    menor_val, maior_val = encontrar_menor_maior(num1_in, num2_in, num3_in)
    
    # Exibe os resultados
    print(f"O menor número é: {menor_val}")
    print(f"O maior número é: {maior_val}")
