"""Você deve criar um programa Python que calcula e exibe as estatísticas básicas (soma, média, menor e maior valor) de uma lista de números fornecida pelo usuário. O programa deve ser modular, utilizando funções para cada etapa do processo.

1.  **Função para Leitura de Dados (`ler_numeros_lista`):**
    *   Esta função deve solicitar ao usuário que digite uma série de números (inteiros ou decimais) separados por espaços em uma única linha.
    *   A função deve converter esta entrada em uma `list` de `float`s.
    *   Deve retornar a lista de números.

2.  **Função para Análise de Estatísticas (`analisar_estatisticas_lista`):**
    *   Esta função receberá a lista de números (do tipo `list[float]`) como argumento.
    *   Ela deve calcular:
        *   A soma de todos os números na lista.
        *   A média aritmética dos números na lista.
        *   O menor número na lista.
        *   O maior número na lista.
    *   Se a lista de entrada estiver vazia, ela deve retornar `(0.0, 0.0, None, None)` para a soma, média, menor e maior, respectivamente.
    *   A função deve retornar esses quatro valores como uma tupla.

3.  **Programa Principal:**
    *   No programa principal, utilize a função `ler_numeros_lista` para obter os dados do usuário.
    *   Em seguida, passe a lista resultante para a função `analisar_estatisticas_lista`.
    *   Por fim, imprima os resultados de forma clara, formatando os valores numéricos (soma, média, menor, maior) para duas casas decimais. Se a lista for vazia, exiba uma mensagem apropriada."""

from typing import List, Tuple, Union

def ler_numeros_lista() -> List[float]:
    """
    Solicita ao usuário uma série de números separados por espaços
    e retorna-os como uma lista de floats.
    """
    entrada = input("Digite os números separados por espaços: ")
    if not entrada.strip():
        return []
    numeros_str = entrada.split()
    return [float(num) for num in numeros_str]

def analisar_estatisticas_lista(numeros: List[float]) -> Tuple[float, float, Union[float, None], Union[float, None]]:
    """
    Calcula e retorna a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros (List[float]): Uma lista de números de ponto flutuante.

    Returns:
        Tuple[float, float, Union[float, None], Union[float, None]]:
        Uma tupla contendo (soma, media, menor_valor, maior_valor).
        Retorna (0.0, 0.0, None, None) se a lista for vazia.
    """
    if not numeros:
        return 0.0, 0.0, None, None

    soma_total = sum(numeros)
    quantidade = len(numeros)
    media = soma_total / quantidade
    menor_valor = min(numeros)
    maior_valor = max(numeros)

    return soma_total, media, menor_valor, maior_valor

# Programa Principal
lista_de_numeros = ler_numeros_lista()
soma, media, menor, maior = analisar_estatisticas_lista(lista_de_numeros)

if not lista_de_numeros:
    print("A lista de números está vazia. Nenhuma estatística para exibir.")
else:
    print(f"Soma: {soma:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Menor valor: {menor:.2f}")
    print(f"Maior valor: {maior:.2f}")
