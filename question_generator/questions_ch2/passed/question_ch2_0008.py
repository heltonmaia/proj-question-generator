"""Crie um programa que solicite ao usuário que digite uma frase. O programa deve então analisar essa frase e exibir uma mensagem específica com base em certas condições. As condições devem ser verificadas na seguinte ordem de prioridade:

1.  **Prioridade Alta:** Se a frase começar com a letra 'P' (maiúscula ou minúscula) E terminar com a letra 'N' (maiúscula ou minúscula), o programa deve imprimir: "A frase é um exemplo de boa prática em Python!".
2.  **Prioridade Média:** Caso a condição anterior não seja atendida, mas a frase contiver a palavra "Python" (ignorando maiúsculas e minúsculas em sua busca), o programa deve imprimir: "A frase menciona a linguagem Python!".
3.  **Prioridade Baixa:** Caso nenhuma das condições anteriores seja atendida e a frase for vazia (ou seja, o usuário não digitou nada), o programa deve imprimir: "A frase está vazia.".
4.  **Caso Padrão:** Se nenhuma das condições acima for verdadeira, o programa deve imprimir: "A frase não se encaixa nas categorias especiais.".

Certifique-se de que a análise de letras (P/N) e a busca pela palavra "Python" sejam case-insensitive."""

frase = input()
frase_lower = frase.lower()

# 1. Prioridade Alta: Começa com 'P' e termina com 'N'
if frase and frase_lower.startswith('p') and frase_lower.endswith('n'):
    print("A frase é um exemplo de boa prática em Python!")
# 2. Prioridade Média: Contém a palavra "Python"
elif "python" in frase_lower:
    print("A frase menciona a linguagem Python!")
# 3. Prioridade Baixa: Frase vazia
elif not frase:
    print("A frase está vazia.")
# 4. Caso Padrão
else:
    print("A frase não se encaixa nas categorias especiais.")
