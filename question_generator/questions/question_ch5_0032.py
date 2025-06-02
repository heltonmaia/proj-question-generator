"""Sua tarefa é criar um programa Python que realize uma análise estatística básica de uma lista de números fornecida pelo usuário. O programa deve:

1.  **Definir uma função** chamada `analisar_numeros` que aceite uma lista de números (inteiros ou decimais) como argumento.
2.  Dentro desta função, calcule a **soma** de todos os números, a **média** dos números, a **quantidade de números positivos** e a **quantidade de números negativos**.
    *   Considere que o número `0` não é positivo nem negativo.
    *   Se a lista estiver vazia, a soma deve ser `0.0`, a média `0.0`, e as contagens `0`.
3.  A função `analisar_numeros` deve **retornar todos esses quatro valores** como uma tupla, na seguinte ordem: `(soma, media, qtd_positivos, qtd_negativos)`.
4.  No **programa principal**, leia uma única linha de entrada que conterá uma sequência de números separados por espaços (ex: `10 2.5 -5 0 7`).
5.  Converta a entrada lida em uma lista de números decimais (`float`).
6.  Chame a função `analisar_numeros` com a lista criada.
7.  Por fim, **imprima os resultados** de forma clara e formatada, indicando cada métrica calculada. A soma e a média devem ser formatadas com duas casas decimais."""

from typing import List, Tuple

def analisar_numeros(lista_de_numeros: List[float]) -> Tuple[float, float, int, int]:
    """
    Analisa uma lista de números, calculando a soma, média,
    quantidade de positivos e quantidade de negativos.

    Args:
        lista_de_numeros (List[float]): Uma lista de números (inteiros ou decimais).

    Returns:
        Tuple[float, float, int, int]: Uma tupla contendo (soma, media, qtd_positivos, qtd_negativos).
    """
    soma = 0.0
    media = 0.0
    qtd_positivos = 0
    qtd_negativos = 0

    if not lista_de_numeros:
        return (soma, media, qtd_positivos, qtd_negativos)

    soma = sum(lista_de_numeros)
    media = soma / len(lista_de_numeros)

    for num in lista_de_numeros:
        if num > 0:
            qtd_positivos += 1
        elif num < 0:
            qtd_negativos += 1
            
    return (soma, media, qtd_positivos, qtd_negativos)

# Leitura da linha de números e conversão para float
numeros_str = input().split()
numeros = [float(n) for n in numeros_str] if numeros_str else []

# Chama a função de análise
soma_total, media_calc, positivos_cont, negativos_cont = analisar_numeros(numeros)

# Imprime os resultados formatados
print(f"Soma dos números: {soma_total:.2f}")
print(f"Média dos números: {media_calc:.2f}")
print(f"Quantidade de números positivos: {positivos_cont}")
print(f"Quantidade de números negativos: {negativos_cont}")
