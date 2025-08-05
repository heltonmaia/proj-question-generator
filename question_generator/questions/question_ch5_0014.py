# Funções de Operação
def dobrar(numero: int) -> int:
    """Retorna o dobro de um número."""
    return numero * 2

def quadrado(numero: int) -> int:
    """Retorna o quadrado de um número."""
    return numero ** 2

# Função lambda para triplicar
triplicar_lambda = lambda x: x * 3

def transformar_lista(lista_numeros: list[int], operacao) -> list[int]:
    """
    Aplica uma operação a cada elemento de uma lista de números.

    Args:
        lista_numeros (list[int]): A lista de números a ser transformada.
        operacao (function): A função a ser aplicada a cada número.

    Returns:
        list[int]: Uma nova lista com os resultados da operação.
    """
    return [operacao(num) for num in lista_numeros]

# Definição da lista original
numeros_originais = [1, 2, 3, 4, 5]

# Loop principal para o menu
while True:
    print("\n--- Transformador de Listas Numéricas ---")
    print(f"Lista original: {numeros_originais}")
    print("Escolha uma operação:")
    print("1 - Dobrar números")
    print("2 - Calcular o quadrado dos números")
    print("3 - Triplicar números")
    print("4 - Sair")
    
    escolha = input("Digite sua opção: ")
    
    if escolha == '1':
        lista_transformada = transformar_lista(numeros_originais, dobrar)
        print(f"Lista dobrada: {lista_transformada}")
    elif escolha == '2':
        lista_transformada = transformar_lista(numeros_originais, quadrado)
        print(f"Lista com quadrados: {lista_transformada}")
    elif escolha == '3':
        lista_transformada = transformar_lista(numeros_originais, triplicar_lambda)
        print(f"Lista triplicada: {lista_transformada}")
    elif escolha == '4':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
