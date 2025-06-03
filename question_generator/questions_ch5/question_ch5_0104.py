"""Sua tarefa é criar um programa Python que realize uma análise estatística básica em uma lista de números. Para isso, você deve implementar uma função e utilizá-la no programa principal.

1.  **Função `analisar_estatisticas_lista`**:
    *   Esta função deve receber uma lista de números (inteiros ou de ponto flutuante) como seu único argumento.
    *   Dentro da função, calcule o menor valor, o maior valor e a média aritmética de todos os números na lista.
    *   A função deve retornar esses três valores como uma tupla, na seguinte ordem: `(menor_valor, maior_valor, media)`.
    *   Adicione uma `docstring` à função explicando seu propósito, argumentos e retorno. Use `type hints` para os parâmetros e o tipo de retorno, seguindo o padrão visto no material.
    *   Se a lista de entrada estiver vazia, a função deve retornar `(None, None, None)` para indicar que as estatísticas não podem ser calculadas.

2.  **Programa Principal**:
    *   O programa deve ler uma linha de entrada contendo números separados por espaços.
    *   Converta a entrada do usuário em uma lista de números de ponto flutuante (`float`).
    *   Chame a função `analisar_estatisticas_lista` com a lista criada.
    *   Imprima os resultados obtidos da função.
        *   Se as estatísticas foram calculadas (lista não vazia), imprima o menor valor, o maior valor e a média, formatando a média para duas casas decimais.
        *   Se a lista de entrada estiver vazia, o programa deve imprimir a mensagem: "A lista está vazia, não é possível calcular as estatísticas.""""

def analisar_estatisticas_lista(numeros: list[float]) -> tuple[float, float, float]:
    """
    Calcula o menor valor, o maior valor e a média aritmética de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números (inteiros ou de ponto flutuante).

    Returns:
        tuple[float, float, float]: Uma tupla contendo (menor_valor, maior_valor, media).
                                    Retorna (None, None, None) se a lista estiver vazia.
    """
    if not numeros:
        return None, None, None
    
    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)
    media = soma / len(numeros)
    
    return menor, maior, media

# Programa Principal
entrada_str = input()
if entrada_str.strip() == "":
    lista_numeros = []
else:
    lista_numeros = [float(x) for x in entrada_str.split()]

menor, maior, media = analisar_estatisticas_lista(lista_numeros)

if menor is None: # Verifica se a lista estava vazia
    print("A lista está vazia, não é possível calcular as estatísticas.")
else:
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Média: {media:.2f}")
