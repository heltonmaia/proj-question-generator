"""Crie uma função Python chamada `analisar_string` que aceite uma única string como argumento. Sua função deve analisar a string e retornar três informações distintas:
1.  O comprimento total da string.
2.  A contagem de vogais (considerando 'a', 'e', 'i', 'o', 'u', tanto maiúsculas quanto minúsculas).
3.  A contagem de consoantes (apenas letras do alfabeto que não são vogais, tanto maiúsculas quanto minúsculas).

A função deve retornar esses três valores como uma tupla, na ordem: (comprimento, vogais, consoantes).

No programa principal, peça ao usuário para digitar uma frase ou palavra. Em seguida, chame a função `analisar_string` com a entrada do usuário e imprima os resultados retornados de forma legível, indicando cada valor (comprimento, número de vogais, número de consoantes)."""

def analisar_string(texto: str) -> tuple[int, int, int]:
    """
    Analisa uma string e retorna seu comprimento, número de vogais e número de consoantes.

    Args:
        texto (str): A string a ser analisada.

    Returns:
        tuple[int, int, int]: Uma tupla contendo (comprimento, vogais, consoantes).
    """
    comprimento = len(texto)
    vogais_count = 0
    consoantes_count = 0
    
    # Define as vogais para fácil verificação
    vogais_set = "aeiouAEIOU"

    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra do alfabeto
            if char in vogais_set:
                vogais_count += 1
            else:
                consoantes_count += 1
    
    return comprimento, vogais_count, consoantes_count

# Programa principal
frase = input()
comp, num_vogais, num_consoantes = analisar_string(frase)

print(f"Comprimento da string: {comp}")
print(f"Número de vogais: {num_vogais}")
print(f"Número de consoantes: {num_consoantes}")
