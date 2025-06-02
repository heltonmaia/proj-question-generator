"""Você foi encarregado de desenvolver um programa para analisar dados de temperatura diária. O objetivo é criar uma função que calcule a temperatura média de uma série de medições e determine quantos dias tiveram a temperatura acima de um certo limite.

Sua tarefa é implementar uma função chamada `analisar_temperaturas` que receba os seguintes parâmetros:

1.  `temperaturas`: Uma lista de números de ponto flutuante (`float`), representando as temperaturas registradas em diferentes dias.
2.  `limite`: Um número de ponto flutuante (`float`), representando a temperatura limite que será usada para contar os dias "quentes".

A função deve retornar dois valores em uma tupla:
*   A temperatura média da lista de `temperaturas`, arredondada para duas casas decimais.
*   A contagem de quantos dias na lista tiveram a temperatura estritamente maior que o `limite` fornecido.

O programa principal deve ler uma sequência de temperaturas (separadas por vírgulas) e o valor do limite. Em seguida, ele deve chamar a função `analisar_temperaturas` e imprimir os resultados formatados conforme os exemplos de saída.

**Exemplo de uso:**
Se a entrada for:
`20.5, 22.0, 25.5, 19.0, 23.0`
`21.0`

A função calculará a média e contará os dias em que a temperatura foi maior que `21.0`."""

def analisar_temperaturas(temperaturas: list[float], limite: float) -> tuple[float, int]:
    """
    Calcula a temperatura média e a quantidade de dias com temperatura acima de um limite.

    Args:
        temperaturas (list[float]): Uma lista de temperaturas diárias.
        limite (float): A temperatura limite para contagem de dias quentes.

    Returns:
        tuple[float, int]: Uma tupla contendo a temperatura média (arredondada para 2 casas decimais)
                           e o número de dias com temperatura acima do limite.
    """
    if not temperaturas:
        return 0.00, 0

    soma_temperaturas = sum(temperaturas)
    media = soma_temperaturas / len(temperaturas)

    dias_acima_limite = 0
    for temp in temperaturas:
        if temp > limite:
            dias_acima_limite += 1

    return round(media, 2), dias_acima_limite

# Leitura da entrada
# Assume que as temperaturas são fornecidas como uma string separada por vírgulas
temperaturas_str = input()
if temperaturas_str.strip(): # Verifica se a string não está vazia ou contém apenas espaços
    temperaturas = [float(t.strip()) for t in temperaturas_str.split(',')]
else:
    temperaturas = [] # Lista vazia se a entrada for vazia

limite_temperatura = float(input())

# Chamada da função e impressão dos resultados
media_temp, dias_quentes = analisar_temperaturas(temperaturas, limite_temperatura)

print(f"Temperatura Média: {media_temp:.2f}")
print(f"Dias acima do limite: {dias_quentes}")
