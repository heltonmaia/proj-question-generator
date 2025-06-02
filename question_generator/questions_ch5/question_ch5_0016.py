"""Você foi contratado para criar um sistema de análise de temperaturas diárias. Seu programa deve ser capaz de receber uma lista de temperaturas e, a partir dela, calcular a temperatura média e a quantidade de dias em que a temperatura esteve acima de um valor limite predefinido.

Implemente uma função Python chamada `analisar_temperaturas` que:
1.  Receba dois argumentos:
    *   `temperaturas`: uma lista de números de ponto flutuante (float), representando as temperaturas diárias.
    *   `limite`: um número de ponto flutuante (float), representando a temperatura limite para a contagem.
2.  Calcule a **temperatura média** da lista fornecida.
3.  Conte o número de dias em que a temperatura foi **estritamente maior** que o `limite` fornecido.
4.  Retorne uma tupla contendo dois valores: a temperatura média (como `float`) e a contagem de dias acima do limite (como `int`).

No programa principal, você deve:
*   Solicitar ao usuário que digite as temperaturas diárias, separadas por espaços (ex: `22.5 28.0 24.1 30.5 26.0`).
*   Solicitar ao usuário que digite o valor limite (ex: `25.0`).
*   Processar as entradas para criar a lista de floats e o limite float.
*   Chamar a função `analisar_temperaturas` com os dados obtidos.
*   Imprimir os resultados formatados para duas casas decimais para a média e o número inteiro para a contagem, seguindo o formato especificado nos exemplos de saída.
*   Considere o caso de uma lista de temperaturas vazia, onde a média deve ser `0.00` e a contagem `0`."""

from typing import List, Tuple

def analisar_temperaturas(temperaturas: List[float], limite: float) -> Tuple[float, int]:
    """
    Analisa uma lista de temperaturas, calculando a média e a contagem de dias
    com temperatura acima de um limite.

    Args:
        temperaturas: Uma lista de temperaturas diárias.
        limite: O valor limite de temperatura para a contagem.

    Returns:
        Uma tupla contendo a temperatura média e a contagem de dias acima do limite.
    """
    if not temperaturas:
        return 0.0, 0

    soma_temperaturas = sum(temperaturas)
    media_temperaturas = soma_temperaturas / len(temperaturas)

    dias_acima_limite = 0
    for temp in temperaturas:
        if temp > limite:
            dias_acima_limite += 1
            
    return media_temperaturas, dias_acima_limite

# --- Programa Principal ---
if __name__ == "__main__":
    # Leitura da lista de temperaturas
    temperaturas_str = input()
    if temperaturas_str.strip(): # Verifica se a string não está vazia ou apenas com espaços
        temperaturas = [float(temp) for temp in temperaturas_str.split()]
    else:
        temperaturas = [] # Lista vazia se a entrada for vazia

    # Leitura do limite
    limite = float(input())

    # Chamada da função e impressão dos resultados
    media, contagem = analisar_temperaturas(temperaturas, limite)

    print(f"Temperatura Média: {media:.2f}ºC")
    print(f"Dias acima de {limite:.1f}ºC: {contagem}")
