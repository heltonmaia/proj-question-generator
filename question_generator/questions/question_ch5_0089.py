"""Você foi contratado para desenvolver uma ferramenta simples de análise de dados. Sua tarefa é criar uma função em Python que calcule a média, o menor valor e o maior valor de uma lista de números inteiros.

A função deve ser chamada `analisar_numeros` e receberá uma lista de números inteiros (`list[int]`) como parâmetro. Ela deve retornar três valores: a média dos números (do tipo `float`), o menor número (do tipo `int`) e o maior número (do tipo `int`), nesta ordem, como uma tupla. Se a lista estiver vazia, a função deve retornar `(0.0, 0, 0)`.

Adicionalmente, inclua uma `docstring` na sua função para descrever o que ela faz, seus parâmetros e o que ela retorna, e utilize `type hints` para indicar os tipos dos parâmetros e do retorno.

No programa principal, solicite ao usuário uma série de números inteiros (separados por espaço) para formar a lista. Em seguida, chame a função `analisar_numeros` com essa lista e imprima os resultados formatados, exibindo a média com duas casas decimais."""

def analisar_numeros(numeros: list[int]) -> tuple[float, int, int]:
    """
    Calcula a média, o menor e o maior valor de uma lista de números inteiros.

    Args:
        numeros (list[int]): Uma lista de números inteiros.

    Returns:
        tuple[float, int, int]: Uma tupla contendo a média (float),
                                o menor número (int) e o maior número (int).
                                Retorna (0.0, 0, 0) se a lista estiver vazia.
    """
    if not numeros:
        return 0.0, 0, 0

    media = sum(numeros) / len(numeros)
    menor = min(numeros)
    maior = max(numeros)
    return media, menor, maior

if __name__ == "__main__":
    entrada_str = input("Digite os números inteiros separados por espaço: ")
    
    # Processa a entrada para criar a lista de inteiros
    if entrada_str.strip() == "":
        numeros_int = []
    else:
        numeros_str = entrada_str.split()
        numeros_int = [int(num_str) for num_str in numeros_str]

    media_calc, menor_calc, maior_calc = analisar_numeros(numeros_int)

    print(f"Média: {media_calc:.2f}")
    print(f"Menor: {menor_calc}")
    print(f"Maior: {maior_calc}")
