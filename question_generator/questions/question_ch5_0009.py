"""Crie uma função Python chamada `analisar_texto` que receba uma string (texto) como argumento.

A função deve retornar uma tupla contendo três valores, nesta ordem:

1.  O número total de **caracteres alfabéticos** (letras de A-Z) no texto, **ignorando espaços, números e outros caracteres não alfabéticos**.
2.  O número de **vogais** (a, e, i, o, u), considerando tanto letras maiúsculas quanto minúsculas.
3.  O número de **consoantes**, considerando tanto letras maiúsculas quanto minúsculas.

A função deve ser robusta para lidar com textos vazios ou textos contendo apenas caracteres não alfabéticos.

*Exemplo de uso:*
```python
total_letras, vogais, consoantes = analisar_texto("Olá Mundo!")
print(f"Total de letras: {total_letras}, Vogais: {vogais}, Consoantes: {consoantes}")
# Saída esperada para o exemplo: Total de letras: 8, Vogais: 4, Consoantes: 4
```"""

def analisar_texto(texto: str) -> tuple[int, int, int]:
    """
    Analisa um texto e retorna o número total de letras, vogais e consoantes.

    Args:
        texto (str): O texto a ser analisado.

    Returns:
        tuple[int, int, int]: Uma tupla contendo (total_letras, vogais, consoantes).
    """
    total_letras = 0
    vogais = 0
    consoantes = 0
    
    vogais_set = {'a', 'e', 'i', 'o', 'u'}
    
    for char in texto:
        char_lower = char.lower()
        if 'a' <= char_lower <= 'z':  # Verifica se é uma letra alfabética
            total_letras += 1
            if char_lower in vogais_set:
                vogais += 1
            else:
                consoantes += 1
    
    return total_letras, vogais, consoantes

# Para testes automáticos, o programa principal pode chamar a função
# com entradas de exemplo e imprimir os resultados.
# Exemplo para execução:
# texto_entrada = input()
# total_l, v, c = analisar_texto(texto_entrada)
# print(f"Total de letras: {total_l}")
# print(f"Vogais: {v}")
# print(f"Consoantes: {c}")
