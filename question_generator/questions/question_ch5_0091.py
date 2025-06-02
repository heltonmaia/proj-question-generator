def ler_dados() -> tuple[float, float]:
    """
    Solicita ao usuário que insira o peso e a altura.
    
    Retorna:
        Uma tupla contendo o peso (float) e a altura (float).
    """
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    return peso, altura

def calcular_imc(peso: float, altura: float) -> float | None:
    """
    Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso (float): Peso da pessoa em quilogramas.
        altura (float): Altura da pessoa em metros.

    Retorna:
        float: O valor do IMC, ou None se o peso/altura for inválido.
    """
    if peso <= 0 or altura <= 0:
        return None
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    """
    Classifica o IMC de acordo com as faixas padrão.

    Args:
        imc (float): O valor do Índice de Massa Corporal.

    Retorna:
        str: A classificação correspondente ao IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    elif imc < 35.0:
        return "Obesidade grau 1"
    elif imc < 40.0:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

# Programa principal
if __name__ == "__main__":
    peso, altura = ler_dados()
    imc = calcular_imc(peso, altura)

    if imc is not None:
        classificacao = classificar_imc(imc)
        print(f"Seu IMC é {imc:.2f} - Classificação: {classificacao}")
    else:
        print("Não foi possível calcular o IMC. Peso e altura devem ser valores positivos.")
