def analisar_lista_numeros(lista: list[int]) -> tuple[int, float, int, int]:
    """
    Analisa uma lista de números inteiros, calculando sua soma, média,
    quantidade de números pares e quantidade de números ímpares.

    Args:
        lista (list[int]): Uma lista de números inteiros.

    Returns:
        tuple[int, float, int, int]: Uma tupla contendo:
            - A soma de todos os números.
            - A média aritmética dos números (float).
            - A contagem de números pares.
            - A contagem de números ímpares.
    """
    soma = 0
    pares = 0
    impares = 0

    for numero in lista:
        soma += numero
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    media = soma / len(lista)

    return soma, media, pares, impares

# Programa principal
# Ler a linha de entrada e converter para uma lista de inteiros
entrada_str = input()
numeros_str = entrada_str.split()
lista_de_numeros = [int(num) for num in numeros_str]

# Chamar a função e desempacotar os resultados
soma_total, media_calculada, qtd_pares, qtd_impares = analisar_lista_numeros(lista_de_numeros)

# Imprimir os resultados formatados
print(f"Soma dos números: {soma_total}")
print(f"Média dos números: {media_calculada:.2f}")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
