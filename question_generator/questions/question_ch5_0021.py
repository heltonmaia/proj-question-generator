"""Crie uma função Python que receba uma lista de números inteiros. Esta função deve calcular a soma de todos os números presentes na lista e, adicionalmente, contar quantos números pares existem nela.

A função deve retornar ambos os resultados (a soma total e a contagem de números pares) como uma tupla.

No programa principal, solicite ao usuário que insira uma série de números inteiros em uma única linha, separados por espaços. Em seguida, utilize a função criada para processar a lista de números e imprima os resultados obtidos de forma clara e formatada."""

def analisar_lista_numeros(lista: list[int]) -> tuple[int, int]:
    """
    Calcula a soma de todos os números em uma lista e a quantidade de números pares.

    Args:
        lista: Uma lista de números inteiros.

    Returns:
        Uma tupla contendo (soma_total, contagem_pares).
    """
    soma_total = 0
    contagem_pares = 0
    for numero in lista:
        soma_total += numero
        if numero % 2 == 0:
            contagem_pares += 1
    return soma_total, contagem_pares

# Programa principal
try:
    entrada_str = input("Digite números inteiros separados por espaço: ")
    numeros_str = entrada_str.split()
    lista_numeros = [int(num) for num in numeros_str]

    soma, pares = analisar_lista_numeros(lista_numeros)

    print(f"Soma total dos números: {soma}")
    print(f"Quantidade de números pares: {pares}")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros separados por espaço.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
