"""Crie um programa Python que utilize funções para processar dois números decimais. O programa deve solicitar ao usuário que insira dois números de ponto flutuante.

Em seguida, implemente uma função chamada `analisar_numeros` que receba esses dois números como parâmetros e retorne **três valores distintos**:
1.  A soma dos dois números.
2.  O produto dos dois números.
3.  O maior valor entre os dois números.

No programa principal, após obter a entrada do usuário, chame a função `analisar_numeros` e desempacote os resultados em variáveis separadas. Por fim, exiba a soma, o produto e o maior número de forma clara e formatada com duas casas decimais."""

def analisar_numeros(num1, num2):
    """
    Calcula a soma, o produto e encontra o maior entre dois números.

    Retorna uma tupla contendo (soma, produto, maior_numero).
    """
    soma = num1 + num2
    produto = num1 * num2
    
    if num1 >= num2:
        maior_numero = num1
    else:
        maior_numero = num2
        
    return soma, produto, maior_numero

# Leitura dos números de ponto flutuante
n1 = float(input())
n2 = float(input())

# Chamada da função e desempacotamento dos resultados
soma_resultado, produto_resultado, maior_resultado = analisar_numeros(n1, n2)

# Exibição dos resultados formatados
print(f"Soma: {soma_resultado:.2f}")
print(f"Produto: {produto_resultado:.2f}")
print(f"Maior número: {maior_resultado:.2f}")
