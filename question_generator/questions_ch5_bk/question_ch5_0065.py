"""Você foi contratado para criar um sistema de análise de desempenho para uma turma de alunos. Sua tarefa é desenvolver uma função em Python que receba uma lista de notas (números de ponto flutuante) e retorne o menor, o maior e a média dessas notas. A função deve ser robusta o suficiente para lidar com uma lista vazia, retornando valores apropriados nesse caso.

Implemente a função `analisar_notas(notas)` que:
- Receba uma lista de `float` como parâmetro.
- Retorne uma tupla contendo o menor, o maior e a média das notas.
- Se a lista estiver vazia, deve retornar `(None, None, None)` para indicar que não há notas para analisar.
- A média deve ser arredondada para duas casas decimais.

No programa principal, você deve:
1. Ler uma linha de entrada contendo várias notas separadas por espaço (podem ser inteiros ou decimais).
2. Converter essas entradas para uma lista de `float`.
3. Chamar a função `analisar_notas` com a lista de notas.
4. Imprimir os resultados no formato especificado nos testes."""

def analisar_notas(notas: list[float]) -> tuple[float | None, float | None, float | None]:
    """
    Analisa uma lista de notas, retornando a menor, a maior e a média.

    Args:
        notas: Uma lista de números de ponto flutuante representando as notas.

    Returns:
        Uma tupla contendo (menor_nota, maior_nota, media_notas).
        Retorna (None, None, None) se a lista de notas estiver vazia.
    """
    if not notas:
        return None, None, None

    menor = min(notas)
    maior = max(notas)
    media = sum(notas) / len(notas)

    return menor, maior, round(media, 2)

# Programa principal
entrada_str = input()
if entrada_str.strip() == "":
    lista_notas = []
else:
    try:
        lista_notas = [float(x) for x in entrada_str.split()]
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de inserir números separados por espaços.")
        lista_notas = [] # Para que o programa não quebre e exiba a mensagem de lista vazia

menor_nota, maior_nota, media_notas = analisar_notas(lista_notas)

if menor_nota is None:
    print("Nenhuma nota para analisar.")
else:
    print(f"Menor nota: {menor_nota}")
    print(f"Maior nota: {maior_nota}")
    print(f"Média das notas: {media_notas}")
