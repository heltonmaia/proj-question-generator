"""Desenvolva um programa Python que realize uma análise estatística básica em uma lista de números inteiros fornecida pelo usuário. O programa deve incluir uma função que calcule a soma, a média, a quantidade de números pares e a quantidade de números ímpares da lista.

Sua tarefa é:

1.  **Leitura da Entrada:** Solicite ao usuário que digite uma série de números inteiros em uma única linha, separados por espaço. O programa deve ser capaz de lidar com uma linha de entrada vazia.
2.  **Função `analisar_numeros`:** Crie uma função chamada `analisar_numeros` que receba uma lista de números inteiros como argumento. Esta função deve:
    *   Calcular a soma de todos os elementos na lista.
    *   Calcular a média dos elementos na lista. Se a lista estiver vazia, a média deve ser `0.0`.
    *   Contar quantos números são pares.
    *   Contar quantos números são ímpares.
    *   Retornar esses quatro valores (soma, média, quantidade de pares, quantidade de ímpares) como uma tupla.
3.  **Programa Principal:** No programa principal, utilize a entrada do usuário para criar a lista de números, chame a função `analisar_numeros` e imprima os resultados de forma clara e formatada. A média deve ser exibida com duas casas decimais."""

def analisar_numeros(numeros: list[int]) -> tuple[int, float, int, int]:
    """
    Analisa uma lista de números inteiros, calculando soma, média,
    quantidade de pares e quantidade de ímpares.

    Args:
        numeros (list[int]): Uma lista de números inteiros.

    Returns:
        tuple[int, float, int, int]: Uma tupla contendo:
            - A soma de todos os números.
            - A média dos números (0.0 se a lista estiver vazia).
            - A contagem de números pares.
            - A contagem de números ímpares.
    """
    soma = 0
    pares = 0
    impares = 0
    
    if not numeros: # Lida com lista vazia
        return 0, 0.0, 0, 0

    for num in numeros:
        soma += num
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    media = soma / len(numeros)
    
    return soma, media, pares, impares

# Leitura da entrada
entrada_str = input()

# Converte a string de entrada em uma lista de inteiros
# Lida com o caso de entrada vazia para evitar erro de split()
if entrada_str.strip() == "":
    lista_numeros = []
else:
    lista_numeros = [int(x) for x in entrada_str.split()]

# Chamada da função e exibição dos resultados
soma_total, media_total, num_pares, num_impares = analisar_numeros(lista_numeros)

print(f"Soma total: {soma_total}")
print(f"Média: {media_total:.2f}")
print(f"Números pares: {num_pares}")
print(f"Números ímpares: {num_impares}")
