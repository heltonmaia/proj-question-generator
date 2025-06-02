"""Crie uma função Python chamada `analisar_numeros` que receba uma lista de números (inteiros ou de ponto flutuante) como argumento. Esta função deve calcular e retornar dois valores:
1.  A soma de todos os números na lista.
2.  A média aritmética desses números.

Ambos os valores (soma e média) devem ser retornados pela mesma função. Se a lista de entrada estiver vazia, a função deve retornar `0.0` para a soma e `0.0` para a média.

No programa principal, o programa deve ler uma linha de entrada que contém números separados por vírgula (por exemplo, `10, 20, 30.5`). Converta esses números para uma lista de `float` e, em seguida, chame a função `analisar_numeros` com essa lista. Finalmente, imprima a soma e a média calculadas, formatando a média com duas casas decimais."""

from typing import List, Tuple

def analisar_numeros(numeros: List[float]) -> Tuple[float, float]:
    """
    Calcula a soma e a média de uma lista de números.

    Args:
        numeros: Uma lista de números (inteiros ou de ponto flutuante).

    Returns:
        Uma tupla contendo a soma dos números e a média dos números.
        Retorna (0.0, 0.0) se a lista estiver vazia para evitar divisão por zero.
    """
    if not numeros:
        return 0.0, 0.0
    
    soma = sum(numeros)
    media = soma / len(numeros)
    return soma, media

# Programa principal
entrada_str = input()
if entrada_str.strip() == "": 
    lista_numeros = []
else:
    # Converte a string de entrada (e.g., "10, 20, 30.5") para uma lista de floats
    lista_numeros = [float(x.strip()) for x in entrada_str.split(',')]

soma_resultado, media_resultado = analisar_numeros(lista_numeros)

print(f"Soma: {soma_resultado}")
print(f"Média: {media_resultado:.2f}")
