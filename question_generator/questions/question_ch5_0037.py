def analisar_temperaturas(temperaturas: list[float], limite_quente: float) -> tuple[float, float, float, int]:
    """
    Analisa uma lista de temperaturas diárias e retorna estatísticas.

    Args:
        temperaturas: Uma lista de temperaturas diárias (não vazia).
        limite_quente: O limite de temperatura para considerar um dia "quente".

    Returns:
        Uma tupla contendo (média, máxima, mínima, contagem de dias quentes).
    """
    media = sum(temperaturas) / len(temperaturas)
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)
    
    dias_quentes = 0
    for temp in temperaturas:
        if temp > limite_quente:
            dias_quentes += 1
            
    return round(media, 2), max_temp, min_temp, dias_quentes

# Leitura da entrada das temperaturas
temperaturas_str = input().split()
temperaturas_float = [float(t) for t in temperaturas_str]

# Leitura da entrada do limite_quente
limite_quente_input = float(input())

# Chamada da função e desempacotamento dos resultados
media, max_temp, min_temp, dias_quentes = analisar_temperaturas(temperaturas_float, limite_quente_input)

# Impressão dos resultados
print(f"Média: {media:.2f}")
print(f"Máxima: {max_temp}")
print(f"Mínima: {min_temp}")
print(f"Dias Quentes: {dias_quentes}")
