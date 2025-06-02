"""Você foi contratado para desenvolver uma ferramenta simples de análise de dados. Sua tarefa é criar um programa em Python que receba uma série de números (inteiros ou decimais) inseridos pelo usuário em uma única linha, separados por espaços. O programa deve então calcular a soma e a média aritmética desses números.

Para isso, você deve:
1.  **Ler os números:** O programa deve ler uma linha de entrada do usuário, que contém os números separados por espaços.
2.  **Converter para uma lista de números:** Converta a string de entrada em uma lista de números (ponto flutuante).
3.  **Criar uma função `analisar_numeros`:** Essa função deve receber uma lista de números como parâmetro e retornar dois valores: a soma de todos os números na lista e a média aritmética desses números.
    *   A função deve utilizar `docstrings` para documentar sua funcionalidade, parâmetros e retorno.
    *   Deve usar `type hints` para indicar os tipos dos parâmetros e do valor de retorno.
    *   **Observação:** Se a lista de entrada for vazia (ou seja, se o usuário não digitar nenhum número), a função deve retornar `(0.0, 0.0)` para a soma e a média, respectivamente, para evitar erros de divisão por zero.
4.  **Exibir os resultados:** No programa principal, após chamar a função e desempacotar os valores, imprima a soma e a média formatadas com duas casas decimais.

Exemplo de interação:
Entrada: `10 20 30 40 50`
Saída esperada:
`Soma: 150.00`
`Média: 30.00`"""

from typing import List, Tuple

def analisar_numeros(numeros: List[float]) -> Tuple[float, float]:
    """
    Calcula a soma e a média de uma lista de números.

    Args:
        numeros (List[float]): Uma lista de números (inteiros ou decimais).

    Returns:
        Tuple[float, float]: Uma tupla contendo a soma dos números e a média aritmética.
                             Retorna (0.0, 0.0) se a lista for vazia.
    """
    if not numeros:
        return (0.0, 0.0)

    soma_total = sum(numeros)
    media = soma_total / len(numeros)
    return (soma_total, media)

# Leitura da entrada do usuário
entrada_str = input()

# Converte a string de entrada para uma lista de números (float)
# Trata o caso de entrada vazia ou apenas espaços
if entrada_str.strip(): # Verifica se a string não está vazia ou contém apenas espaços em branco
    lista_de_numeros = [float(x) for x in entrada_str.split()]
else:
    lista_de_numeros = []

# Chama a função e desempacota os resultados
soma_final, media_final = analisar_numeros(lista_de_numeros)

# Imprime os resultados formatados
print(f"Soma: {soma_final:.2f}")
print(f"Média: {media_final:.2f}")
