"""Você foi contratado para criar um sistema de análise de dados para uma pequena empresa. Sua primeira tarefa é desenvolver um programa em Python que receba uma série de números inteiros do usuário. O programa deve continuar solicitando números até que o usuário digite a palavra "fim" (ignorando maiúsculas/minúsculas).

Após coletar todos os números, o programa deve analisar essa lista para determinar:
1.  A soma de todos os elementos.
2.  A quantidade de números pares.
3.  A quantidade de números ímpares.

Para organizar o código e promover a modularidade, implemente uma função chamada `analisar_numeros`. Esta função deve aceitar como parâmetro uma `lista_de_inteiros` (uma lista de `int`) e retornar uma tupla contendo os três valores calculados, na seguinte ordem: `(soma_total, contagem_pares, contagem_impares)`.

No programa principal, após coletar os números do usuário, chame a função `analisar_numeros` com a lista coletada e imprima os resultados de forma clara e organizada, conforme os exemplos de saída.

Utilize `docstrings` e `type hints` para documentar sua função e melhorar a clareza do código, seguindo as boas práticas apresentadas no material de estudo."""

def analisar_numeros(lista_de_inteiros: list[int]) -> tuple[int, int, int]:
    """
    Analisa uma lista de números inteiros, calculando a soma total,
    a contagem de números pares e a contagem de números ímpares.

    Args:
        lista_de_inteiros (list[int]): Uma lista de números inteiros.

    Returns:
        tuple[int, int, int]: Uma tupla contendo:
                              - A soma total dos números.
                              - A contagem de números pares.
                              - A contagem de números ímpares.
    """
    soma_total = 0
    contagem_pares = 0
    contagem_impares = 0

    for numero in lista_de_inteiros:
        soma_total += numero
        if numero % 2 == 0:
            contagem_pares += 1
        else:
            contagem_impares += 1
            
    return soma_total, contagem_pares, contagem_impares

# Programa principal
numeros_coletados = []
while True:
    entrada = input()
    if entrada.lower() == 'fim':
        break
    try:
        numeros_coletados.append(int(entrada))
    except ValueError:
        # Ignora entradas não numéricas que não sejam 'fim'
        continue

soma, pares, impares = analisar_numeros(numeros_coletados)

print(f"Soma total: {soma}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
