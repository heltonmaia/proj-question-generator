"""Você foi contratado para analisar dados de temperatura de uma semana. Sua tarefa é escrever um programa Python que realize duas operações principais sobre uma lista de temperaturas: calcular a temperatura média da semana e identificar quantos dias a temperatura esteve acima de um determinado limite.

Crie uma função chamada `analisar_temperaturas` que receba dois argumentos:
1.  `temperaturas`: uma lista de números de ponto flutuante (`float`), representando as temperaturas diárias.
2.  `limite`: um número de ponto flutuante (`float`), representando o limite de temperatura a ser comparado.

A função deve retornar uma tupla contendo dois valores:
1.  A temperatura média calculada (um `float`).
2.  A contagem de dias em que a temperatura foi estritamente maior que o `limite` (um `int`).

No programa principal, solicite ao usuário uma lista de temperaturas diárias (separadas por espaço) e um valor para o limite. Em seguida, chame a função `analisar_temperaturas` e imprima os resultados de forma clara, formatando a temperatura média com duas casas decimais."""

from typing import List, Tuple

def analisar_temperaturas(temperaturas: List[float], limite: float) -> Tuple[float, int]:
    """
    Calcula a temperatura média e a contagem de dias acima de um limite.

    Args:
        temperaturas: Uma lista de temperaturas diárias.
        limite: O limite de temperatura para comparação.

    Returns:
        Uma tupla contendo a temperatura média e a contagem de dias
        em que a temperatura foi acima do limite.
    """
    if not temperaturas:
        return 0.0, 0

    media = sum(temperaturas) / len(temperaturas)
    dias_acima_do_limite = 0
    for temp in temperaturas:
        if temp > limite:
            dias_acima_do_limite += 1
            
    return media, dias_acima_do_limite

# Programa principal
# Solicita as temperaturas como uma string e as converte para uma lista de floats
temperaturas_str = input("Digite as temperaturas diárias separadas por espaço (ex: 20.5 22.0 19.8): ")
temperaturas_list = [float(t) for t in temperaturas_str.split()]

# Solicita o limite de temperatura
limite_valor = float(input("Digite o limite de temperatura: "))

# Chama a função e desempacota os resultados
media_temp, contagem_acima = analisar_temperaturas(temperaturas_list, limite_valor)

# Imprime os resultados formatados
print(f"Temperatura média da semana: {media_temp:.2f}°C")
print(f"Dias com temperatura acima de {limite_valor}°C: {contagem_acima}")
