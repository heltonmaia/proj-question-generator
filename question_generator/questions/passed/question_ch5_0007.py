"""Você foi contratado para desenvolver um sistema de cálculo de bonificações para atletas olímpicos. Seu programa deve:

1.  **Ler as entradas:**
    *   Primeiro, o programa deve ler uma linha que contém os tipos de medalhas conquistadas pelo atleta, separados por vírgulas (ex: `"ouro,prata,bronze"`). Se o atleta não tiver conquistado nenhuma medalha, a linha será vazia.
    *   Em seguida, o programa deve ler uma string indicando se o atleta quebrou um recorde mundial (`"Sim"` ou `"Nao"`).
    *   Por último, o programa deve ler uma string indicando se a medalha conquistada (ou uma delas, se houver múltiplas) foi a primeira do país naquela modalidade (`"Sim"` ou `"Nao"`).

2.  **Calcular a bonificação usando uma função:** Crie uma função Python chamada `calcular_bonificacao_atleta` que receba os seguintes parâmetros:
    *   `medalhas`: Uma lista de strings (`list[str]`), onde cada string representa o tipo de medalha conquistada ("ouro", "prata", "bronze").
    *   `quebrou_recorde_mundial`: Um valor booleano (`bool`) que é `True` se o atleta quebrou um recorde mundial, `False` caso contrário.
    *   `primeira_medalha_pais_modalidade`: Um valor booleano (`bool`) que é `True` se a medalha foi a primeira do país naquela modalidade, `False` caso contrário.

    A função deve retornar o valor total da bonificação do atleta.

As regras de bonificação são:
*   **Bonificação base por medalha:**
    *   **Ouro**: R$ 50.000
    *   **Prata**: R$ 30.000
    *   **Bronze**: R$ 10.000
*   **Bônus adicionais:**
    *   Se `quebrou_recorde_mundial` for `True`: +R$ 100.000
    *   Se `primeira_medalha_pais_modalidade` for `True`: +R$ 50.000

3.  **Imprimir o resultado:** O programa deve imprimir o valor total da bonificação calculado pela função, formatado como um número de ponto flutuante com uma casa decimal (Ex: `150000.0`).

**Exemplo:** Se as entradas forem "ouro", "Sim", "Nao", a bonificação total seria R$ 50.000 (ouro) + R$ 100.000 (recorde) = R$ 150.000.

Sua função deve ser robusta, calculando corretamente a soma de todas as bonificações aplicáveis."""

def calcular_bonificacao_atleta(medalhas: list[str], quebrou_recorde_mundial: bool, primeira_medalha_pais_modalidade: bool) -> float:
    """
    Calcula a bonificação total de um atleta olímpico com base em suas medalhas e bônus.

    Args:
        medalhas (list[str]): Lista de strings representando as medalhas ("ouro", "prata", "bronze").
        quebrou_recorde_mundial (bool): True se o atleta quebrou um recorde mundial, False caso contrário.
        primeira_medalha_pais_modalidade (bool): True se foi a primeira medalha do país na modalidade, False caso contrário.

    Returns:
        float: O valor total da bonificação do atleta.
    """
    total_bonificacao = 0.0

    # Bonificação por medalhas
    for medalha in medalhas:
        medalha_lower = medalha.lower()
        if medalha_lower == "ouro":
            total_bonificacao += 50000.0
        elif medalha_lower == "prata":
            total_bonificacao += 30000.0
        elif medalha_lower == "bronze":
            total_bonificacao += 10000.0
        # Outras strings de medalha são ignoradas e não contribuem para a bonificação.

    # Bônus adicionais
    if quebrou_recorde_mundial:
        total_bonificacao += 100000.0

    if primeira_medalha_pais_modalidade:
        total_bonificacao += 50000.0

    return total_bonificacao

# --- Leitura de Entradas e Chamada da Função Principal ---

# Leitura das medalhas (string separada por vírgulas)
medalhas_input_str = input()
if medalhas_input_str: # Verifica se a string não está vazia
    lista_medalhas = [m.strip() for m in medalhas_input_str.split(',')]
else:
    lista_medalhas = [] # Lista vazia se não houver medalhas

# Leitura do status de recorde mundial
recorde_mundial_str = input()
quebrou_recorde_mundial_bool = (recorde_mundial_str.lower() == "sim")

# Leitura do status de primeira medalha do país na modalidade
primeira_medalha_str = input()
primeira_medalha_pais_modalidade_bool = (primeira_medalha_str.lower() == "sim")

# Calcula a bonificação final
bonificacao_final = calcular_bonificacao_atleta(
    lista_medalhas,
    quebrou_recorde_mundial_bool,
    primeira_medalha_pais_modalidade_bool
)

# Imprime o resultado formatado
print(f"{bonificacao_final:.1f}")
