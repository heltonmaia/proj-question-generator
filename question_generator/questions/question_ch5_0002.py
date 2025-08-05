"""Você foi contratado para ajudar uma pequena loja a analisar seus dados de vendas diárias. Sua tarefa é criar um programa Python que receba uma lista de valores inteiros, representando as vendas de cada dia. O programa deve calcular e retornar três informações importantes sobre essas vendas: a soma total das vendas, a média diária de vendas e a quantidade de dias registrados (número de elementos na lista).

Crie uma função chamada `analisar_vendas_diarias` que aceite uma lista de números inteiros como parâmetro. Esta função deve utilizar `docstrings` e `type hints` e retornar uma tupla contendo a soma total, a média (como um `float`) e a contagem de elementos na lista, nesta ordem.

Considere que a lista de vendas sempre conterá pelo menos um valor.

No programa principal, leia uma linha de números inteiros separados por espaço (assumindo que o usuário fornecerá a lista nesse formato), converta-os para uma lista de inteiros, chame a função e imprima os resultados de forma clara. A média diária de vendas deve ser formatada para exibir duas casas decimais."""

def analisar_vendas_diarias(vendas: list[int]) -> tuple[int, float, int]:
    """
    Analisa uma lista de vendas diárias, calculando a soma total, a média
    e a quantidade de dias registrados.

    Args:
        vendas (list[int]): Uma lista de números inteiros representando as vendas diárias.
                            Assume-se que a lista conterá pelo menos um valor.

    Returns:
        tuple[int, float, int]: Uma tupla contendo:
            - A soma total das vendas (int).
            - A média diária de vendas (float).
            - A quantidade de dias registrados (int).
    """
    total_vendas = sum(vendas)
    quantidade_dias = len(vendas)
    
    # A garantia do enunciado de que a lista não é vazia evita ZeroDivisionError
    media_vendas = total_vendas / quantidade_dias
    
    return total_vendas, media_vendas, quantidade_dias

# Leitura da entrada: espera uma linha de números inteiros separados por espaço
entrada_str = input()
vendas_lista_str = entrada_str.split()
vendas_lista_int = [int(v) for v in vendas_lista_str]

# Chamando a função para obter os resultados
soma, media, contagem = analisar_vendas_diarias(vendas_lista_int)

# Imprimindo os resultados formatados
print(f"Soma Total de Vendas: {soma}")
print(f"Média Diária de Vendas: {media:.2f}")
print(f"Quantidade de Dias Registrados: {contagem}")
