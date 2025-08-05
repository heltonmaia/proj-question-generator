"""Você foi encarregado de criar um pequeno programa para análise de dados numéricos. Sua tarefa é desenvolver uma função em Python que calcule a média aritmética e o **intervalo (amplitude)** de uma lista de números. O intervalo é definido como a diferença entre o maior e o menor valor presente na lista.

Siga as seguintes especificações:

1.  Crie uma função chamada `analisar_estatisticas` que aceite uma lista de números (que podem ser inteiros ou decimais) como parâmetro.
2.  Dentro desta função, calcule a média de todos os números da lista.
3.  Ainda dentro da função, calcule o intervalo da lista (maior valor menos o menor valor).
4.  A função deve retornar esses dois resultados (média e intervalo) como uma tupla. Se a lista de entrada estiver vazia, a função deve retornar `(0.0, 0.0)`.
5.  No programa principal, solicite ao usuário uma sequência de números separados por vírgulas (ex: "10, 20, 15.5, 5").
6.  Converta a string de entrada em uma lista de números de ponto flutuante.
7.  Chame a função `analisar_estatisticas` com a lista de números obtida.
8.  Por fim, imprima a média e o intervalo calculados, formatando ambos com duas casas decimais."""

def analisar_estatisticas(numeros: list[float]) -> tuple[float, float]:
    """
    Calcula a média e o intervalo (amplitude) de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números (inteiros ou decimais).

    Returns:
        tuple[float, float]: Uma tupla contendo a média e o intervalo (maior - menor).
                             Retorna (0.0, 0.0) se a lista estiver vazia.
    """
    if not numeros:
        return 0.0, 0.0

    media = sum(numeros) / len(numeros)
    intervalo = max(numeros) - min(numeros)
    
    return media, intervalo

# Programa principal
# A entrada será lida como uma única linha de números separados por vírgulas.
entrada_str = input() 

# Converte a string de entrada em uma lista de números de ponto flutuante
numeros = [float(num.strip()) for num in entrada_str.split(',')]

# Chama a função para analisar as estatísticas
media_calculada, intervalo_calculado = analisar_estatisticas(numeros)

# Imprime os resultados formatados
print(f"Média: {media_calculada:.2f}")
print(f"Intervalo: {intervalo_calculado:.2f}")
