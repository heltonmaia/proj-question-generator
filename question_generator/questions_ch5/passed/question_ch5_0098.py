"""Você foi contratado para desenvolver um sistema de cálculo de preços para uma loja. Sua tarefa é criar uma função em Python que determine o preço final de um produto, aplicando um desconto base e, opcionalmente, um desconto adicional para clientes membros.

Crie uma função chamada `calcular_preco_final` que aceite os seguintes parâmetros:
- `preco_original`: um valor float que representa o preço inicial do produto.
- `percentual_desconto`: um valor float que representa o percentual de desconto a ser aplicado (ex: 10 para 10%).
- `e_membro`: um valor booleano (`True` ou `False`) que indica se o cliente é um membro da loja.

A função deve realizar os seguintes cálculos:
1.  Aplicar o `percentual_desconto` sobre o `preco_original`.
2.  Se `e_membro` for `True`, aplicar um **desconto adicional** de 5% sobre o preço já com o desconto base.
3.  A função deve retornar o `preco_final` calculado.

Certifique-se de usar `type hints` para os parâmetros e o retorno da função, e inclua uma `docstring` clara que descreva o propósito da função, seus argumentos e o valor de retorno.

No programa principal, leia o preço original, o percentual de desconto e a informação de membro (como "Sim" ou "Nao") do usuário. Em seguida, chame a função `calcular_preco_final` com esses dados e imprima o preço final formatado com duas casas decimais.

**Exemplo de cálculo:**
- Preço original: R$ 100.00
- Desconto base: 10%
- Cliente membro: Sim
  - Preço com desconto base: R$ 100.00 * (1 - 0.10) = R$ 90.00
  - Preço final (com 5% adicional): R$ 90.00 * (1 - 0.05) = R$ 85.50"""

def calcular_preco_final(preco_original: float, percentual_desconto: float, e_membro: bool) -> float:
    """
    Calcula o preço final de um produto após aplicar um desconto base
    e, opcionalmente, um desconto adicional para clientes membros.

    Args:
        preco_original (float): O preço inicial do produto.
        percentual_desconto (float): O percentual de desconto a ser aplicado (ex: 10 para 10%).
        e_membro (bool): True se o cliente for membro, False caso contrário.

    Returns:
        float: O preço final calculado.
    """
    # Converter percentual para fator de desconto
    fator_desconto_base = 1 - (percentual_desconto / 100)
    
    # Aplicar desconto base
    preco_apos_desconto_base = preco_original * fator_desconto_base
    
    # Aplicar desconto adicional para membros, se aplicável
    if e_membro:
        fator_desconto_membro = 1 - (5 / 100) # 5% de desconto adicional
        preco_final = preco_apos_desconto_base * fator_desconto_membro
    else:
        preco_final = preco_apos_desconto_base
        
    return preco_final

# --- Programa Principal ---
# Leitura da entrada do usuário
preco_original_input = float(input())
percentual_desconto_input = float(input())
e_membro_str_input = input()

# Conversão da string "Sim"/"Nao" para booleano
e_membro_bool = True if e_membro_str_input.lower() == "sim" else False

# Chamada da função e impressão do resultado
preco_final_calculado = calcular_preco_final(preco_original_input, percentual_desconto_input, e_membro_bool)

print(f"O preço final é: R$ {preco_final_calculado:.2f}")
