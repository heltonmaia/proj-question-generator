"""Sua tarefa é desenvolver um programa Python que utilize uma função para calcular estatísticas de temperatura a partir de uma lista de valores.

Crie uma função chamada `calcular_estatisticas_temperatura` que aceite uma lista de números de ponto flutuante (representando temperaturas diárias) como argumento. Esta função deve calcular e retornar três valores: a temperatura mínima, a temperatura máxima e a temperatura média da lista. Para garantir a clareza e a legibilidade do código, inclua uma docstring e type hints para os parâmetros e o valor de retorno da função.

No programa principal, o usuário deverá fornecer uma sequência de temperaturas em uma única linha, separadas por espaços. O programa deve ler esta entrada, converter os valores para números de ponto flutuante, e então passá-los para a função `calcular_estatisticas_temperatura`.

Após receber os resultados da função, o programa principal deve imprimi-los no console, formatando a temperatura média para duas casas decimais.

A função deve ser robusta o suficiente para lidar com o caso de uma lista vazia (ou entrada inválida que resulte em uma lista vazia), imprimindo uma mensagem apropriada em vez de tentar realizar cálculos impossíveis."""

def calcular_estatisticas_temperatura(temperaturas: list[float]) -> tuple[float | None, float | None, float | None]:
    """
    Calcula as estatísticas de temperatura (mínima, máxima, média) de uma lista.

    Args:
        temperaturas (list[float]): Uma lista de temperaturas em ponto flutuante.

    Returns:
        tuple[float | None, float | None, float | None]: Uma tupla contendo a temperatura mínima,
                                     a temperatura máxima e a temperatura média.
                                     Retorna (None, None, None) se a lista for vazia.
    """
    if not temperaturas:
        return None, None, None

    min_temp = min(temperaturas)
    max_temp = max(temperaturas)
    avg_temp = sum(temperaturas) / len(temperaturas)
    return min_temp, max_temp, avg_temp

# Leitura da entrada
try:
    temperaturas_str = input().split()
    temperaturas = [float(temp) for temp in temperaturas_str]
except ValueError:
    print("Entrada inválida. Certifique-se de inserir números separados por espaços.")
    temperaturas = [] # Garante que a lista esteja vazia para tratamento consistente

# Chamada da função e impressão dos resultados
min_t, max_t, avg_t = calcular_estatisticas_temperatura(temperaturas)

if min_t is not None:
    print(f"Temperatura Mínima: {min_t:.2f}°C")
    print(f"Temperatura Máxima: {max_t:.2f}°C")
    print(f"Temperatura Média: {avg_t:.2f}°C")
else:
    print("Não foi possível calcular as estatísticas para uma lista vazia ou inválida.")
