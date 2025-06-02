import os
import google.generativeai as genai
import logging
import yaml
import requests
import re
from bs4 import BeautifulSoup
from pathlib import Path

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_file=None):
    """
    Carrega a configuração do arquivo config.yml.
    Args:
        config_file (str, optional): Caminho opcional para o arquivo de configuração.
                                     Se None, tenta carregar de ../config.yml.
    Returns:
        dict: Dicionário contendo a configuração.
    Raises:
        FileNotFoundError: Se o arquivo de configuração não for encontrado.
    """
    config_path = Path(config_file) if config_file else Path(__file__).parent.parent / "config.yml"
    if not config_path.exists():
        raise FileNotFoundError(f"Arquivo de configuração não encontrado em {config_path}")

    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        logger.info(f"Configuração carregada com sucesso de {config_path}")
        return config or {}

def load_prompt_template():
    """
    Carrega o conteúdo do arquivo prompt.md que contém o template do prompt para o LLM.
    Returns:
        str: Conteúdo do prompt template.
    Raises:
        FileNotFoundError: Se o arquivo prompt.md não for encontrado.
    """
    prompt_path = Path(__file__).parent / "prompt.md"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Arquivo prompt.md não encontrado em {prompt_path}")

    with open(prompt_path, 'r', encoding='utf-8') as f:
        content = f.read()
        logger.info(f"Prompt template carregado com sucesso de {prompt_path}")
        return content

def fetch_material_from_url(url):
    """
    Busca e extrai o texto de uma URL.
    Args:
        url (str): A URL do material de estudo.
    Returns:
        str: O texto extraído da página web.
    Raises:
        RuntimeError: Se houver um erro ao obter ou processar o conteúdo da URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para erros HTTP (4xx ou 5xx)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n") # Extrai todo o texto visível, separando por quebras de linha
        logger.info(f"Conteúdo extraído com sucesso da URL: {url} (primeiros 200 chars: {text[:200]})")
        return text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erro de requisição ao obter conteúdo da URL {url}: {e}")
    except Exception as e:
        raise RuntimeError(f"Erro inesperado ao processar conteúdo da URL {url}: {e}")

def save_question_to_txt(question_text, base_filename=None):
    """
    Salva o texto da questão gerada em um arquivo .txt dentro da pasta 'questions'.
    Args:
        question_text (str): O texto completo da questão a ser salva.
        base_filename (str, optional): O nome base do arquivo (sem extensão).
                                        Se None, o nome padrão será "questao.txt".
    Returns:
        Path: O caminho completo para o arquivo salvo.
    Raises:
        Exception: Se houver um erro ao salvar o arquivo.
    """
    try:
        questions_dir = Path(__file__).parent / "questions"
        questions_dir.mkdir(exist_ok=True) # Cria o diretório 'questions' se ele não existir

        if base_filename is None:
            base_filename = "questao"

        txt_filename = questions_dir / f"{base_filename}.txt"
        with open(txt_filename, "w", encoding="utf-8") as f:
            # REMOVIDAS AS LINHAS QUE ADICIONAVAM O CABEÇALHO E INSTRUÇÕES DO PROMPT
            f.write(question_text) # Escreve apenas o texto da questão gerada

        logger.info(f"Questão salva em {txt_filename}")
        print(f"Questão salva em: {txt_filename}")
        return txt_filename

    except Exception as e:
        logger.error(f"Erro ao salvar arquivo: {e}")
        raise

def generate_question_from_url(url, output_file=None):
    """
    Gera uma questão de programação Python a partir de um material de estudo online.
    Args:
        url (str): A URL do material de estudo.
        output_file (str, optional): O nome base do arquivo de saída para a questão.
                                     Se None, o nome padrão será "questao.txt".
    Returns:
        str: O texto da questão gerada.
    Raises:
        ValueError: Se a API Key do Gemini não for encontrada.
        RuntimeError: Se houver falha ao gerar a questão após múltiplas tentativas
                      ou outros erros críticos.
    """
    logger.info(f"=== Gerando questão a partir da URL: {url} ===")

    try:
        # Carrega a configuração da API do Gemini
        config = load_config()
        api_key = config.get('gemini', {}).get('api_key')

        if not api_key:
            raise ValueError("API key do Gemini não encontrada no arquivo de configuração.")

        genai.configure(api_key=api_key)
        # Define o modelo a ser usado, com um fallback padrão
        model_name = config.get('gemini', {}).get('model', 'gemini-2.5-flash-preview-05-20')
        model = genai.GenerativeModel(model_name)

        # Carrega o template do prompt e o material da URL
        prompt_template = load_prompt_template()
        material = fetch_material_from_url(url)

        # Prepara o prompt com o material de aprendizado
        if "{learning_material_content}" in prompt_template:
            prompt = prompt_template.replace("{learning_material_content}", material)
        else:
            logger.warning("Placeholder {learning_material_content} não encontrado no prompt.md. Adicionando material ao final.")
            prompt = f"{prompt_template.strip()}\n\n{material}"

        # Tenta gerar a questão até 3 vezes
        for attempt in range(3):
            logger.info(f"Gerando questão (tentativa {attempt + 1})")
            try:
                response = model.generate_content(prompt)
                question_text = response.text.strip()

                # Salva a questão gerada no arquivo
                txt_file = save_question_to_txt(question_text, output_file)

                # Imprime a questão gerada no console para feedback imediato
                print("="*60)
                print("QUESTÃO GERADA COM SUCESSO:")
                print("="*60)
                print(question_text)
                print("="*60)

                return question_text

            except Exception as e:
                logger.warning(f"Tentativa {attempt + 1} falhou: {e}")
                if attempt == 2: # Se for a última tentativa e ainda falhou, lança o erro
                    raise RuntimeError(f"Falha ao gerar questão após 3 tentativas: {e}")

    except Exception as e:
        logger.error(f"Erro na execução: {e}")
        print(f"Erro: {e}")
        raise

if __name__ == "__main__":         
            
    # Define a URL do material de estudo
    url = "https://heltonmaia.com/pythonbook/chapters/ch5/ch5.html"
    
    # Define a quantidade de questões que você deseja gerar
    num_questions_to_generate = 100 

    for i in range(100, num_questions_to_generate + 1): # Loop de 1 até o número desejado de questões
        try:
            # Formata o nome do arquivo de saída com um contador (ex: "question_ch2_0001", "question_ch2_0002", etc.)
            # O f-string com :04d garante que o número terá pelo menos 4 dígitos, preenchidos com zeros à esquerda
            output_filename = f"question_ch5_{i:04d}" 
            
            print(f"\n--- Gerando questão {i}/{num_questions_to_generate} ---")
            generate_question_from_url(url, output_file=output_filename)
        except Exception as e:
            print(f"Erro ao gerar questão {i}: {e}")