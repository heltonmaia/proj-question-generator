"""Faça um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O IMC é calculado dividindo-se o peso da pessoa (em kg) pela sua altura (em metros) ao quadrado. O programa deve solicitar ao usuário o peso e a altura, e em seguida, imprimir o IMC calculado (formatado com duas casas decimais) e a classificação correspondente de acordo com a tabela abaixo:

| IMC          | Classificação       |
|--------------|---------------------|
| < 18.5       | Abaixo do peso      |
| 18.5 - 24.9  | Saudável            |
| 25.0 - 29.9  | Sobrepeso           |
| 30.0 - 34.9  | Obesidade grau I    |
| 35.0 - 39.9  | Obesidade grau II   |
| >= 40.0      | Obesidade grau III  |"""

peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

classificacao = ""
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Saudável"
elif 25.0 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30.0 <= imc < 34.9:
    classificacao = "Obesidade grau I"
elif 35.0 <= imc < 39.9:
    classificacao = "Obesidade grau II"
else: # imc >= 40.0
    classificacao = "Obesidade grau III"

print(f"Seu IMC é {imc:.2f} ({classificacao}).")
