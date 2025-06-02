"""Crie uma função Python chamada `classificar_numeros` que recebe três números inteiros como argumentos. Esta função deve analisar esses três números e retornar uma tupla contendo três valores booleanos:

1.  O primeiro booleano deve indicar se o primeiro número é par (`True` se for par, `False` caso contrário).
2.  O segundo booleano deve indicar se o segundo número é positivo (`True` se for positivo, `False` caso contrário).
3.  O terceiro booleano deve indicar se o terceiro número é zero (`True` se for zero, `False` caso contrário).

No programa principal, você deverá:
1.  Solicitar ao usuário que insira três números inteiros, um por linha.
2.  Chamar a função `classificar_numeros` com os números lidos.
3.  Desempacotar os valores booleanos retornados pela função em variáveis separadas.
4.  Imprimir na tela os resultados de forma clara, usando mensagens como "O primeiro número é par: True", "O segundo número é positivo: False", etc."""

from typing import Tuple

def classificar_numeros(num1: int, num2: int, num3: int) -> Tuple[bool, bool, bool]:
    """
    Classifica três números inteiros de acordo com as condições especificadas.

    Args:
        num1 (int): O primeiro número inteiro.
        num2 (int): O segundo número inteiro.
        num3 (int): O terceiro número inteiro.

    Returns:
        Tuple[bool, bool, bool]: Uma tupla contendo:
                                 - True se num1 for par, False caso contrário.
                                 - True se num2 for positivo, False caso contrário.
                                 - True se num3 for zero, False caso contrário.
    """
    primeiro_par = (num1 % 2 == 0)
    segundo_positivo = (num2 > 0)
    terceiro_zero = (num3 == 0)
    
    return primeiro_par, segundo_positivo, terceiro_zero

# Programa principal
num1_input = int(input())
num2_input = int(input())
num3_input = int(input())

e_par, e_positivo, e_zero = classificar_numeros(num1_input, num2_input, num3_input)

print(f"O primeiro número é par: {e_par}")
print(f"O segundo número é positivo: {e_positivo}")
print(f"O terceiro número é zero: {e_zero}")
