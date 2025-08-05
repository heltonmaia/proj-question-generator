"""Escreva um programa que defina uma função para analisar uma lista de números inteiros. Esta função deve receber uma lista como entrada e retornar três informações: a soma de todos os números pares na lista, a quantidade de números ímpares na lista e o maior número presente na lista.

No programa principal, o usuário deverá fornecer uma sequência de números inteiros separados por espaço em uma única linha. O programa deve ler esses números, convertê-los para uma lista de inteiros, chamar a função de análise e, por fim, imprimir os resultados formatados para a soma dos pares, a contagem dos ímpares e o maior número encontrado.

Considere que a lista de entrada nunca estará vazia para fins de teste."""

def analisar_lista_numeros(numeros: list[int]) -> tuple[int, int, int]:
    """
    Analisa uma lista de números inteiros para calcular a soma dos pares,
    a contagem dos ímpares e o maior número.

    Args:
        numeros (list[int]): Uma lista de números inteiros.
                             Assume-se que a lista não será vazia.

    Returns:
        tuple[int, int, int]: Uma tupla contendo:
                              (soma_dos_pares, contagem_dos_impares, maior_numero).
    """
    soma_dos_pares = 0
    contagem_dos_impares = 0
    
    # Inicializa maior_numero com o primeiro elemento, pois a lista não será vazia.
    maior_numero = numeros[0] 

    for num in numeros:
        if num % 2 == 0:
            soma_dos_pares += num
        else:
            contagem_dos_impares += 1
        
        if num > maior_numero:
            maior_numero = num
            
    return soma_dos_pares, contagem_dos_impares, maior_numero

# Leitura da entrada (uma linha de números separados por espaço)
entrada_str = input()
# Converte a string de entrada em uma lista de inteiros
lista_de_numeros = [int(x) for x in entrada_str.split()]

# Chama a função
soma_p, cont_i, maior_n = analisar_lista_numeros(lista_de_numeros)

# Imprime os resultados formatados
print(f"Soma dos números pares: {soma_p}")
print(f"Contagem de números ímpares: {cont_i}")
print(f"Maior número: {maior_n}")
