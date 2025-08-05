"""Você foi encarregado de criar uma ferramenta simples para calcular juros e montante de investimentos. Sua tarefa é desenvolver um programa Python que utilize uma função para calcular o **juro simples** e o **montante final** de um investimento, dado o capital inicial, a taxa de juros anual e o tempo em anos.

Sua solução deve atender aos seguintes requisitos:

1.  **Criação de Função:** Implemente uma função chamada `calcular_juros_e_montante`.
2.  **Parâmetros:** A função deve receber três parâmetros:
    *   `capital` (tipo `float`): O valor principal do investimento.
    *   `taxa` (tipo `float`): A taxa de juros anual, expressa em decimal (por exemplo, `0.05` para 5%).
    *   `tempo` (tipo `float`): O período do investimento em anos.
3.  **Docstrings e Type Hints:** Adicione uma `docstring` clara à função, descrevendo seu propósito, parâmetros e o que ela retorna. Utilize `type hints` para indicar os tipos dos parâmetros e do valor de retorno.
4.  **Cálculos:**
    *   **Juro Simples (JS):** Calcule usando a fórmula `JS = Capital * Taxa * Tempo`.
    *   **Montante Final (M):** Calcule usando a fórmula `M = Capital + JS`.
5.  **Retorno da Função:** A função deve retornar uma **tupla** contendo dois valores: primeiro o `juro_simples` e, em seguida, o `montante_final`.
6.  **Interação com o Usuário:** No programa principal (fora da função), solicite ao usuário o `capital`, a `taxa` e o `tempo`. Em seguida, chame a função `calcular_juros_e_montante` com os valores fornecidos.
7.  **Saída Formatada:** Imprima os resultados do juro simples e do montante final, formatados com **duas casas decimais** e identificando claramente cada valor."""

def calcular_juros_e_montante(capital: float, taxa: float, tempo: float) -> tuple[float, float]:
    """
    Calcula o juro simples e o montante final de um investimento.

    Args:
        capital (float): O valor inicial do investimento.
        taxa (float): A taxa de juros anual (em decimal).
        tempo (float): O tempo do investimento em anos.

    Returns:
        tuple[float, float]: Uma tupla contendo (juro_simples, montante_final).
    """
    juros_simples = capital * taxa * tempo
    montante_final = capital + juros_simples
    return juros_simples, montante_final

# Leitura dos valores de entrada
capital_input = float(input())
taxa_input = float(input())
tempo_input = float(input())

# Chamada da função e desempacotamento dos resultados
juros, montante = calcular_juros_e_montante(capital_input, taxa_input, tempo_input)

# Impressão dos resultados formatados
print(f"Juro Simples: R$ {juros:.2f}")
print(f"Montante Final: R$ {montante:.2f}")
