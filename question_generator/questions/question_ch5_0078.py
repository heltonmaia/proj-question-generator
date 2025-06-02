"""Crie uma função Python que receba uma lista de números (inteiros ou de ponto flutuante) como entrada. A função deve calcular e retornar quatro valores: a soma de todos os elementos, a média dos elementos, o menor valor e o maior valor da lista.

A função deve ser nomeada `analisar_estatisticas_lista` e incluir `docstrings` e `type hints` para clareza e documentação, conforme recomendado no material de estudo.

**Casos Especiais:**
- Se a lista estiver vazia, a função deve retornar uma tupla com valores indicando a ausência de dados: `(0.0, 0.0, None, None)`.
- A média deve ser calculada como um número de ponto flutuante.
- O menor e o maior valor devem ser retornados como números de ponto flutuante (ou `None` se a lista for vazia).

No programa principal, você deve ler uma linha de entrada contendo números separados por vírgulas (ex: `10.5,20.0,5.0,15.0`). Converta esses números para uma lista de valores numéricos e, em seguida, chame a função `analisar_estatisticas_lista` com essa lista. Por fim, imprima os resultados da soma, média, menor e maior valor, cada um em uma nova linha e no formato especificado nos testes."""

from typing import List, Tuple, Optional

def analisar_estatisticas_lista(numeros: List[float]) -> Tuple[float, float, Optional[float], Optional[float]]:
    """
    Calcula a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros: Uma lista de números (int ou float).

    Returns:
        Uma tupla contendo (soma, media, menor_valor, maior_valor).
        Retorna (0.0, 0.0, None, None) se a lista estiver vazia.
    """
    if not numeros:
        return 0.0, 0.0, None, None

    soma_total = sum(numeros)
    media = float(soma_total) / len(numeros)
    menor = min(numeros)
    maior = max(numeros)

    return soma_total, media, float(menor), float(maior)

# Programa principal
entrada_str = input()

# Converte a entrada para uma lista de floats, tratando entradas vazias e strings vazias após a vírgula
if entrada_str.strip() == "":
    lista_numeros = []
else:
    lista_numeros = [float(x.strip()) for x in entrada_str.split(',') if x.strip()]

soma, media, menor, maior = analisar_estatisticas_lista(lista_numeros)

# Formata a saída para valores None
menor_str = f"{menor}" if menor is not None else "None"
maior_str = f"{maior}" if maior is not None else "None"

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Menor: {menor_str}")
print(f"Maior: {maior_str}")
