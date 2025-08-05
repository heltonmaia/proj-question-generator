"""Crie uma função Python chamada `classificar_numero` que aceite um único parâmetro, um número inteiro. Esta função deve analisar o número para determinar duas características:

1.  **Sinal do Número**: Se é "Positivo", "Negativo" ou "Zero".
2.  **Paridade do Número**: Se é "Par" ou "Ímpar".

A função `classificar_numero` deve retornar uma tupla contendo duas strings: a primeira string deve ser a classificação do sinal e a segunda string deve ser a classificação da paridade.

No programa principal, solicite ao usuário que digite um número inteiro. Em seguida, chame a função `classificar_numero` com o número fornecido pelo usuário e imprima os resultados retornados de forma clara, indicando o sinal e a paridade do número."""

def classificar_numero(numero: int) -> tuple[str, str]:
    """
    Classifica um número inteiro como Positivo/Negativo/Zero e Par/Ímpar.

    Args:
        numero: O número inteiro a ser classificado.

    Returns:
        Uma tupla de duas strings: (classificacao_sinal, classificacao_paridade).
    """
    # Classificação do sinal
    if numero > 0:
        sinal = "Positivo"
    elif numero < 0:
        sinal = "Negativo"
    else:
        sinal = "Zero"

    # Classificação da paridade
    if numero % 2 == 0:
        paridade = "Par"
    else:
        paridade = "Ímpar"

    return sinal, paridade

# Programa principal
num_digitado = int(input())

sinal_resultado, paridade_resultado = classificar_numero(num_digitado)

print(f"O número é: {sinal_resultado}")
print(f"O número é: {paridade_resultado}")
