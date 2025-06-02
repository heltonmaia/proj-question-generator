"""Escreva um programa Python que solicita ao usuário uma sequência de números inteiros, separados por espaços. O programa deve então processar essa sequência para calcular a soma dos números pares e a contagem dos números ímpares.

Para isso, você deve criar uma função chamada `analisar_numeros_da_lista` que receberá uma lista de números inteiros como argumento. Esta função deve retornar uma tupla contendo dois valores:
1.  A soma de todos os números pares encontrados na lista.
2.  A contagem total de números ímpares encontrados na lista.

No programa principal, após ler a entrada do usuário e convertê-la em uma lista de inteiros, chame a função `analisar_numeros_da_lista` e, em seguida, imprima os resultados de forma clara, indicando a soma dos pares e a contagem dos ímpares."""

def analisar_numeros_da_lista(numeros: list[int]) -> tuple[int, int]:
    """
    Analisa uma lista de números inteiros, calculando a soma dos pares
    e a contagem dos ímpares.

    Args:
        numeros: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo (soma_pares, contagem_impares).
    """
    soma_pares = 0
    contagem_impares = 0

    for num in numeros:
        if num % 2 == 0:
            soma_pares += num
        else:
            contagem_impares += 1
    
    return soma_pares, contagem_impares

# Leitura da entrada do usuário
entrada_str = input()
# Converte a string de entrada em uma lista de inteiros
if entrada_str.strip(): # Verifica se a entrada não é apenas espaço em branco
    lista_de_numeros = [int(x) for x in entrada_str.split()]
else:
    lista_de_numeros = [] # Retorna uma lista vazia se a entrada for vazia ou só espaços

# Chama a função para analisar a lista
soma_pares_resultado, contagem_impares_resultado = analisar_numeros_da_lista(lista_de_numeros)

# Imprime os resultados
print(f"Soma dos números pares: {soma_pares_resultado}")
print(f"Contagem dos números ímpares: {contagem_impares_resultado}")
