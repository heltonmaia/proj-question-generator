"""Desenvolva um programa Python que utilize uma função para calcular o preço final de um produto após a aplicação de um desconto, e também retorne o valor total do desconto concedido.

A função deve ser chamada `calcular_preco_com_desconto` e receberá dois parâmetros:
1.  `preco_original`: o preço inicial do produto (float).
2.  `percentual_desconto`: o percentual de desconto a ser aplicado (float, por exemplo, `10` para 10%).

A função deve retornar dois valores:
1.  O `preco_final` após o desconto.
2.  O `valor_desconto` aplicado.

No programa principal, solicite ao usuário o preço original do produto e o percentual de desconto. Em seguida, chame a função criada e imprima o preço final e o valor do desconto, ambos formatados com duas casas decimais.

**Exemplo de cálculo:**
Se o preço original for R$ 100,00 e o desconto for de 10%, o preço final será R$ 90,00 e o valor do desconto será R$ 10,00."""

def calcular_preco_com_desconto(preco_original: float, percentual_desconto: float) -> tuple[float, float]:
    """
    Calcula o preço final de um produto após um desconto e o valor do desconto.

    Args:
        preco_original (float): O preço inicial do produto.
        percentual_desconto (float): O percentual de desconto a ser aplicado (ex: 10 para 10%).

    Returns:
        tuple[float, float]: Uma tupla contendo o preço final e o valor do desconto.
    """
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final, valor_desconto

# Programa principal
preco_original_input = float(input())
percentual_desconto_input = float(input())

preco_final, valor_desconto = calcular_preco_com_desconto(preco_original_input, percentual_desconto_input)

print(f"Preço Final: R$ {preco_final:.2f}")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
