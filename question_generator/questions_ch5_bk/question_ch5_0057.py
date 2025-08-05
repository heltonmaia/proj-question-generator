"""Crie uma função Python chamada `calcular_estatisticas_lista` que recebe uma lista de números (inteiros ou de ponto flutuante) como argumento.
A função deve calcular e retornar dois valores: a soma de todos os números na lista e a média aritmética desses números.

**Condições Especiais:**
- Se a lista de entrada estiver vazia, a função deve retornar uma tupla `(0.0, 0.0)` (soma 0.0 e média 0.0).
- Todos os resultados numéricos (soma e média) devem ser tratados como números de ponto flutuante para garantir precisão na média.

No programa principal, leia uma linha de números do usuário (separados por espaço), converta-os para uma lista de números (utilizando `float` para cada elemento), chame a função `calcular_estatisticas_lista` e, em seguida, imprima a soma e a média calculadas, formatando a saída para duas casas decimais.

**Exemplo de interação:**
Entrada: `10 20 30`
Saída:
```
Soma: 60.00
Média: 20.00
```"""

def calcular_estatisticas_lista(numeros: list[float]) -> tuple[float, float]:
    """
    Calcula a soma e a média de uma lista de números.

    Args:
        numeros: Uma lista de números (inteiros ou de ponto flutuante).

    Returns:
        Uma tupla contendo a soma (float) e a média (float) dos números.
        Retorna (0.0, 0.0) se a lista estiver vazia.
    """
    if not numeros:
        return 0.0, 0.0
    
    total_soma = sum(numeros)
    total_media = total_soma / len(numeros)
    
    return float(total_soma), float(total_media)

# Leitura da entrada: espera uma linha com números separados por espaço
entrada_str = input()

# Converte a string de entrada para uma lista de números de ponto flutuante
if entrada_str.strip() == "": # Trata o caso de entrada vazia
    lista_numeros = []
else:
    lista_numeros = [float(x) for x in entrada_str.split()]

# Chama a função para calcular as estatísticas
soma_calculada, media_calculada = calcular_estatisticas_lista(lista_numeros)

# Imprime os resultados formatados
print(f"Soma: {soma_calculada:.2f}")
print(f"Média: {media_calculada:.2f}")
