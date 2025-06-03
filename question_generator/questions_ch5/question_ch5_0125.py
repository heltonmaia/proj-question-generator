"""Você foi encarregado de desenvolver um programa em Python que analise uma lista de números e retorne diversas estatísticas importantes. Para isso, você deve criar uma função que seja capaz de calcular e retornar múltiplos valores, demonstrando o uso de funções com múltiplos retornos.

Sua tarefa é:

1.  **Criar uma função** chamada `analisar_estatisticas` que receba uma lista de números de ponto flutuante (`list[float]`) como parâmetro.
2.  Esta função deve calcular a **soma**, a **média**, o **menor valor** e o **maior valor** da lista.
3.  A função deve retornar esses quatro valores em uma **tupla** no seguinte formato: `(soma, media, minimo, maximo)`.
4.  **Condição especial:** Se a lista de entrada estiver vazia, a função deve retornar `(0.0, 0.0, 0.0, 0.0)`.
5.  Utilize **docstrings** e **type hints** para documentar e clarear o código da função.
6.  No programa principal, leia uma linha de entrada contendo números separados por espaços, converta-os para uma lista de `float`s, chame a função `analisar_estatisticas` e imprima os resultados formatados para duas casas decimais.

**Exemplo de interação:**

Se a entrada for: `10.5 20.0 5.0 15.5`
A função deve calcular:
*   Soma: 10.5 + 20.0 + 5.0 + 15.5 = 51.0
*   Média: 51.0 / 4 = 12.75
*   Mínimo: 5.0
*   Máximo: 20.0

A saída esperada deve ser:
```
Soma: 51.00
Média: 12.75
Mínimo: 5.00
Máximo: 20.00
```"""

from typing import List, Tuple

def analisar_estatisticas(numeros: List[float]) -> Tuple[float, float, float, float]:
    """
    Calcula a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros (List[float]): Uma lista de números de ponto flutuante.

    Returns:
        Tuple[float, float, float, float]: Uma tupla contendo (soma, media, minimo, maximo).
                                          Retorna (0.0, 0.0, 0.0, 0.0) se a lista estiver vazia.
    """
    if not numeros:
        return 0.0, 0.0, 0.0, 0.0

    soma_total = sum(numeros)
    media = soma_total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)

    return soma_total, media, minimo, maximo

if __name__ == "__main__":
    entrada_str = input()
    if entrada_str.strip() == "":
        lista_numeros = []
    else:
        lista_numeros = [float(x) for x in entrada_str.split()]

    soma, media, minimo, maximo = analisar_estatisticas(lista_numeros)

    print(f"Soma: {soma:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Mínimo: {minimo:.2f}")
    print(f"Máximo: {maximo:.2f}")
