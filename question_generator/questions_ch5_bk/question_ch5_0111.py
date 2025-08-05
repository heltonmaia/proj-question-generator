"""Crie uma função em Python chamada `analisar_estatisticas_lista` que receba uma **lista de números (inteiros ou decimais não vazia)**. Esta função deve calcular e retornar, nesta ordem, a **soma**, a **média**, o **maior valor** e o **menor valor** presentes na lista.

No programa principal, solicite ao usuário uma linha de números separados por espaços. Converta esses números em uma lista de valores numéricos (inteiros ou decimais). Em seguida, chame a função `analisar_estatisticas_lista` com essa lista e imprima os resultados formatados.

**Observações:**
- A entrada sempre conterá pelo menos um número.
- Todos os valores de saída (soma, média, maior, menor) devem ser formatados para duas casas decimais."""

def analisar_estatisticas_lista(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, maior e menor valor de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números (inteiros ou decimais).
                                Assume-se que a lista não está vazia.

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo a soma,
                                           a média, o maior valor e o menor valor.
    """
    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return soma, media, maior, menor

# Leitura da entrada
entrada_str = input()
numeros_str = entrada_str.split()
numeros = [float(num) for num in numeros_str]

# Chamada da função e desempacotamento dos resultados
soma_res, media_res, maior_res, menor_res = analisar_estatisticas_lista(numeros)

# Impressão dos resultados formatados
print(f"Soma: {soma_res:.2f}")
print(f"Média: {media_res:.2f}")
print(f"Maior valor: {maior_res:.2f}")
print(f"Menor valor: {menor_res:.2f}")
