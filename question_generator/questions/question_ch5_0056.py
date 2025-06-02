"""Você deve criar um programa Python que utilize funções para analisar um texto fornecido pelo usuário. A tarefa principal é desenvolver uma função que receba uma string como entrada e retorne informações detalhadas sobre ela.

Sua solução deve conter:

1.  **Uma função chamada `analisar_texto`**:
    *   Esta função deve receber um único argumento, que é a string de texto a ser analisada.
    *   Ela deve calcular e retornar **três valores** em uma tupla, na seguinte ordem:
        *   O número total de caracteres na string (incluindo espaços, pontuações, etc.).
        *   O número de vogais (considerando 'a', 'e', 'i', 'o', 'u', maiúsculas e minúsculas).
        *   O número de consoantes (considerando as demais letras do alfabeto, maiúsculas e minúsculas).
    *   Caracteres que não são letras (números, símbolos, espaços) devem ser contados no total de caracteres, mas não nas contagens de vogais ou consoantes.

2.  **Lógica no programa principal**:
    *   O programa deve solicitar que o usuário insira uma linha de texto.
    *   Em seguida, ele deve chamar a função `analisar_texto` com o texto fornecido.
    *   Por fim, deve imprimir os resultados de forma clara, indicando o total de caracteres, o número de vogais e o número de consoantes encontrados no texto.

Este exercício foca na criação e utilização de funções com múltiplos valores de retorno, bem como manipulação básica de strings e estruturas condicionais."""

def analisar_texto(texto: str) -> tuple[int, int, int]:
    """
    Analisa um texto e retorna o total de caracteres, o número de vogais e o número de consoantes.

    Args:
        texto (str): O texto a ser analisado.

    Returns:
        tuple[int, int, int]: Uma tupla contendo (total_caracteres, vogais, consoantes).
    """
    total_caracteres = len(texto)
    vogais = 0
    consoantes = 0
    
    vogais_set = {'a', 'e', 'i', 'o', 'u'}
    
    for char in texto:
        char_lower = char.lower()
        if 'a' <= char_lower <= 'z':  # Verifica se é uma letra do alfabeto
            if char_lower in vogais_set:
                vogais += 1
            else:
                consoantes += 1
                
    return total_caracteres, vogais, consoantes

# Parte principal do programa
texto_usuario = input()
total, num_vogais, num_consoantes = analisar_texto(texto_usuario)

print(f"Total de caracteres: {total}")
print(f"Número de vogais: {num_vogais}")
print(f"Número de consoantes: {num_consoantes}")
