"""Desenvolva um programa Python que demonstre o conceito de passar funções como argumentos para outras funções, um recurso poderoso para criar código flexível e reutilizável.

Para isso, você deve criar uma função principal chamada `processar_lista_strings` que aceite dois parâmetros:
1. `lista_de_strings`: Uma lista de strings que será processada.
2. `operacao`: Uma função que será aplicada a cada string da lista.

A função `processar_lista_strings` deve iterar sobre cada elemento da `lista_de_strings`, aplicar a `operacao` fornecida a cada string e retornar uma **nova lista** contendo os resultados dessas operações. A lista original não deve ser modificada.

Em seguida, demonstre o uso da função `processar_lista_strings` criando e utilizando as seguintes `operacao` funções:

1.  Uma função nomeada `converter_para_maiusculas` que recebe uma string e a retorna em letras maiúsculas.
2.  Uma função anônima (lambda) que recebe uma string e a retorna prefixada com a string `"ITEM: "`.
3.  Uma função anônima (lambda) que recebe uma string e retorna o seu comprimento (número de caracteres).

O programa principal deve inicializar uma lista de strings de exemplo e, em seguida, usar a função `processar_lista_strings` com cada uma das operações definidas. Finalmente, deve imprimir a lista original e as três novas listas resultantes das operações, cada uma com uma descrição clara para facilitar a compreensão.

**Considerações:**
- Utilize `type hints` para indicar os tipos esperados dos parâmetros e retornos das suas funções.
- Inclua `docstrings` para explicar o propósito de cada função, seus argumentos e o valor de retorno."""

from typing import List, Callable, Any

def processar_lista_strings(lista_de_strings: List[str], operacao: Callable[[str], Any]) -> List[Any]:
    """
    Aplica uma função de operação a cada string em uma lista e retorna uma nova lista com os resultados.

    Args:
        lista_de_strings: Uma lista de strings a ser processada.
        operacao: Uma função (callable) que aceita uma string como argumento e retorna um valor.

    Returns:
        Uma nova lista com os resultados da aplicação da operação a cada string.
    """
    return [operacao(s) for s in lista_de_strings]

def converter_para_maiusculas(texto: str) -> str:
    """
    Converte uma string para letras maiúsculas.

    Args:
        texto: A string a ser convertida.

    Returns:
        A string em letras maiúsculas.
    """
    return texto.upper()

# Funções anônimas (lambda) para operações específicas
adicionar_prefixo = lambda s: f"ITEM: {s}"
obter_comprimento = lambda s: len(s)

# Lista de strings de exemplo para demonstração
minha_lista_exemplo = ["python", "programacao", "funcoes", "lambda", "modularizacao"]

# Imprime a lista original
print(f"Lista Original: {minha_lista_exemplo}\n")

# Demonstração 1: Converter para maiúsculas (usando função nomeada)
lista_maiusculas = processar_lista_strings(minha_lista_exemplo, converter_para_maiusculas)
print(f"Lista em Maiúsculas: {lista_maiusculas}")

# Demonstração 2: Adicionar prefixo (usando função lambda)
lista_com_prefixo = processar_lista_strings(minha_lista_exemplo, adicionar_prefixo)
print(f"Lista com Prefixo: {lista_com_prefixo}")

# Demonstração 3: Obter comprimento (usando função lambda)
lista_comprimentos = processar_lista_strings(minha_lista_exemplo, obter_comprimento)
print(f"Lista de Comprimentos: {lista_comprimentos}")
