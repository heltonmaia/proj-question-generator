"""Crie uma função Python chamada `calcular_estatisticas_numericas` que receba uma lista de números (inteiros ou decimais) como argumento. A função deve calcular e retornar dois valores: a soma de todos os números da lista e a média desses números. Os valores devem ser retornados como uma tupla, na ordem `(soma, media)`.

Se a lista de entrada estiver vazia, a função deve retornar a tupla `(0.0, 0.0)` para evitar erros de divisão por zero e indicar a ausência de elementos.

No programa principal, leia uma linha de entrada que contenha números separados por espaços. Converta esses números para o tipo `float` e utilize-os para criar uma lista. Em seguida, chame a função `calcular_estatisticas_numericas` com essa lista e imprima a soma total e a média calculada, ambas formatadas para duas casas decimais."""

def calcular_estatisticas_numericas(numeros: list[float]) -> tuple[float, float]:
    """
    Calcula a soma e a média de uma lista de números.

    Args:
        numeros: Uma lista de números (inteiros ou decimais).

    Returns:
        Uma tupla contendo a soma total e a média dos números.
        Retorna (0.0, 0.0) se a lista estiver vazia.
    """
    if not numeros:
        return 0.0, 0.0
    
    soma = sum(numeros)
    media = soma / len(numeros)
    
    return soma, media

# Leitura da entrada: uma linha com números separados por espaço
# Se a entrada for vazia, cria uma lista vazia.
entrada_str = input()
if entrada_str.strip() == "":
    minha_lista_numeros = []
else:
    minha_lista_numeros = [float(x) for x in entrada_str.split()]

# Calcula as estatísticas
soma_total, media_calculada = calcular_estatisticas_numericas(minha_lista_numeros)

# Imprime os resultados formatados
print(f"Soma total: {soma_total:.2f}")
print(f"Média calculada: {media_calculada:.2f}")
