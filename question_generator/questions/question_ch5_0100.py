"""Desenvolva um programa Python que execute as seguintes tarefas:

1.  **Função `analisar_numeros`:** Crie uma função chamada `analisar_numeros` que receba uma lista de números (inteiros ou de ponto flutuante) como argumento. Esta função deve calcular e retornar uma tupla contendo três valores, nesta ordem:
    *   A soma de todos os números positivos (incluindo o zero, se presente).
    *   A contagem total de números negativos.
    *   O maior número presente na lista.
    Se a lista de entrada estiver vazia, a função deve retornar a tupla `(0.0, 0, None)`.

2.  **Programa Principal:** No programa principal, leia uma linha de números fornecida pelo usuário. Assuma que os números serão separados por espaços. Converta esses números em uma lista de valores de ponto flutuante. Em seguida, chame a função `analisar_numeros` com essa lista e imprima os resultados obtidos de forma clara e formatada com duas casas decimais para valores de ponto flutuante, conforme os exemplos de saída."""

def analisar_numeros(lista_de_numeros: list[float]) -> tuple[float, int, float | None]:
    """
    Analisa uma lista de números, calculando a soma dos positivos,
    a contagem dos negativos e o maior número.

    Args:
        lista_de_numeros (list[float]): Uma lista de números inteiros ou de ponto flutuante.

    Returns:
        tuple[float, int, float | None]: Uma tupla contendo:
            - A soma dos números positivos.
            - A contagem de números negativos.
            - O maior número da lista, ou None se a lista estiver vazia.
    """
    if not lista_de_numeros:
        return 0.0, 0, None

    soma_positivos = 0.0
    contagem_negativos = 0
    
    for num in lista_de_numeros:
        if num >= 0:
            soma_positivos += num
        else:
            contagem_negativos += 1
            
    maior_numero = max(lista_de_numeros)

    return soma_positivos, contagem_negativos, maior_numero

# Programa Principal
entrada_str = input()
if entrada_str.strip() == "":
    numeros_str = []
else:
    numeros_str = entrada_str.split()

lista_de_numeros = [float(x) for x in numeros_str]

soma_pos, count_neg, maior_num = analisar_numeros(lista_de_numeros)

print(f"Soma dos Positivos: {soma_pos:.2f}")
print(f"Contagem dos Negativos: {count_neg}")
if maior_num is not None:
    print(f"Maior Número: {maior_num:.2f}")
else:
    print("Maior Número: Nenhum")
