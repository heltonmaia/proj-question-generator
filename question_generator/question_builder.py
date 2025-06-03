import os
import google.generativeai as genai
import logging
import yaml
import requests
import re
from bs4 import BeautifulSoup
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_file=None):
    """
    Loads configuration from the config.yml file.
    Args:
        config_file (str, optional): Optional path to the config file.
                                     If None, tries to load from ../config.yml.
    Returns:
        dict: Dictionary containing configuration settings.
    Raises:
        FileNotFoundError: If the configuration file is not found.
    """
    config_path = Path(config_file) if config_file else Path(__file__).parent.parent / "config.yml"
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        logger.info(f"Configuration successfully loaded from {config_path}")
        return config or {}

def load_prompt_template():
    """
    Loads the contents of prompt.md, which contains the base prompt for the LLM.
    Returns:
        str: The content of the prompt template.
    Raises:
        FileNotFoundError: If the prompt.md file is not found.
    """
    prompt_path = Path(__file__).parent / "prompt.md"
    if not prompt_path.exists():
        raise FileNotFoundError(f"prompt.md file not found at {prompt_path}")

    with open(prompt_path, 'r', encoding='utf-8') as f:
        content = f.read()
        logger.info(f"Prompt template successfully loaded from {prompt_path}")
        return content

def fetch_material_from_url(url):
    """
    Fetches and extracts text content from a given URL.
    Args:
        url (str): The URL of the study material.
    Returns:
        str: Extracted visible text from the web page.
    Raises:
        RuntimeError: If there's an error while fetching or processing the URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n")
        logger.info(f"Content successfully extracted from URL: {url} (first 200 chars: {text[:200]})")
        return text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request error while fetching content from {url}: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error while processing content from {url}: {e}")

def save_question_to_txt(question_text, base_filename=None):
    """
    Saves the generated question text into a .txt file under the 'questions' directory.
    Args:
        question_text (str): The full text of the question to be saved.
        base_filename (str, optional): Base name of the file (without extension).
                                       Defaults to "questao.txt" if None.
    Returns:
        Path: The full path to the saved file.
    Raises:
        Exception: If there's an error while writing the file.
    """
    try:
        questions_dir = Path(__file__).parent / "questions"
        questions_dir.mkdir(exist_ok=True)

        if base_filename is None:
            base_filename = "questao"

        txt_filename = questions_dir / f"{base_filename}.txt"
        with open(txt_filename, "w", encoding="utf-8") as f:
            f.write(question_text)

        logger.info(f"Question saved to {txt_filename}")
        print(f"Question saved to: {txt_filename}")
        return txt_filename

    except Exception as e:
        logger.error(f"Error while saving file: {e}")
        raise

def generate_question_from_url(url, output_file=None):
    """
    Generates a Python programming question from online study material.
    Args:
        url (str): The URL of the study material.
        output_file (str, optional): Base name for the output file.
                                     Defaults to "questao.txt" if None.
    Returns:
        str: The generated question text.
    Raises:
        ValueError: If the Gemini API key is missing.
        RuntimeError: If generation fails after multiple attempts or critical errors occur.
    """
    logger.info(f"=== Generating question from URL: {url} ===")

    try:
        config = load_config()
        api_key = config.get('gemini', {}).get('api_key')

        if not api_key:
            raise ValueError("Gemini API key not found in configuration file.")

        genai.configure(api_key=api_key)
        model_name = config.get('gemini', {}).get('model', 'gemini-2.5-flash-preview-05-20')
        model = genai.GenerativeModel(model_name)

        prompt_template = load_prompt_template()
        material = fetch_material_from_url(url)

        if "{learning_material_content}" in prompt_template:
            prompt = prompt_template.replace("{learning_material_content}", material)
        else:
            logger.warning("Placeholder {learning_material_content} not found in prompt.md. Appending material at the end.")
            prompt = f"{prompt_template.strip()}\n\n{material}"

        for attempt in range(3):
            logger.info(f"Generating question (attempt {attempt + 1})")
            try:
                response = model.generate_content(prompt)
                question_text = response.text.strip()

                txt_file = save_question_to_txt(question_text, output_file)

                print("="*60)
                print("QUESTION SUCCESSFULLY GENERATED:")
                print("="*60)
                print(question_text)
                print("="*60)

                return question_text

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt == 2:
                    raise RuntimeError(f"Failed to generate question after 3 attempts: {e}")

    except Exception as e:
        logger.error(f"Execution error: {e}")
        print(f"Error: {e}")
        raise

if __name__ == "__main__":         
    url = "https://heltonmaia.com/pythonbook/chapters/ch5/ch5.html"
    num_questions_to_generate = 130

    for i in range(126, num_questions_to_generate + 1):
        try:
            output_filename = f"question_ch5_{i:04d}"
            print(f"\n--- Generating question {i}/{num_questions_to_generate} ---")
            generate_question_from_url(url, output_file=output_filename)
        except Exception as e:
            print(f"Error generating question {i}: {e}")
