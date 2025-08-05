"""Desenvolva um programa Python que calcule diversas estatísticas para uma lista de números fornecida pelo usuário. O programa deve incluir uma função que receba uma lista de números e retorne a soma, a média, o menor e o maior valor presentes nessa lista.

Siga as seguintes instruções:

1.  **Função `analisar_estatisticas`**:
    *   Crie uma função chamada `analisar_estatisticas` que aceite um único parâmetro: `numeros`, uma lista de números de ponto flutuante.
    *   A função deve calcular:
        *   A soma de todos os números na lista.
        *   A média dos números na lista.
        *   O menor número na lista.
        *   O maior número na lista.
    *   A função deve retornar esses quatro valores como uma tupla, na seguinte ordem: `(soma, media, menor, maior)`.
    *   **Importante**: Assuma que a lista de entrada `numeros` sempre conterá pelo menos um número.
2.  **Entrada do Usuário**:
    *   No programa principal, solicite ao usuário que insira uma série de números em uma única linha, separados por espaços.
    *   Converta esses números para uma lista de valores de ponto flutuante.
3.  **Saída**:
    *   Chame a função `analisar_estatisticas` com a lista de números obtida.
    *   Imprima os resultados (soma, média, menor, maior) de forma clara, cada um em uma linha separada, formatando os valores numéricos com duas casas decimais.

Exemplo de como a saída deve parecer:
```
Soma: XX.XX
Média: XX.XX
Menor: XX.XX
Maior: XX.XX
```"""

def analisar_estatisticas(numeros: list[float]) -> tuple[float, float, float, float]:
    """
    Calcula a soma, média, menor e maior valor de uma lista de números.

    Args:
        numeros (list[float]): Uma lista de números de ponto flutuante.
                               Assume-se que a lista conterá pelo menos um número.

    Returns:
        tuple[float, float, float, float]: Uma tupla contendo (soma, media, menor, maior).
    """
    soma = sum(numeros)
    media = soma / len(numeros)
    menor = min(numeros)
    maior = max(numeros)
    return (soma, media, menor, maior)

# --- Programa Principal ---
if __name__ == "__main__":
    # Solicita a entrada de números separados por espaço
    entrada_str = input()
    
    # Converte a string de entrada para uma lista de floats
    # Remove espaços extras e divide a string, depois converte cada parte para float
    numeros_lista = [float(x) for x in entrada_str.split()]

    # Chama a função para analisar as estatísticas
    soma_total, media_calculada, menor_valor, maior_valor = analisar_estatisticas(numeros_lista)

    # Imprime os resultados formatados
    print(f"Soma: {soma_total:.2f}")
    print(f"Média: {media_calculada:.2f}")
    print(f"Menor: {menor_valor:.2f}")
    print(f"Maior: {maior_valor:.2f}")
