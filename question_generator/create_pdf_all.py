import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

class ExerciseListGenerator:
    def __init__(self, questions_folder, output_file="lista_exercicios.pdf"):
        self.questions_folder = questions_folder
        self.output_file = output_file
        self.exercises = []
        self._register_fonts()

    def _register_fonts(self):
        try:
            if not any(font[0] == 'Helvetica' for font in pdfmetrics.getRegisteredFontNames()):
                 pdfmetrics.registerFont(TTFont('Helvetica', 'Helvetica'))
                 pdfmetrics.registerFont(TTFont('Helvetica-Bold', 'Helvetica-Bold'))
            if not any(font[0] == 'Courier' for font in pdfmetrics.getRegisteredFontNames()):
                 pdfmetrics.registerFont(TTFont('Courier', 'Courier'))
            # print("Fontes registradas (ou padrão serão usadas).")
        except Exception as e:
            print(f"Aviso: Problema ao registrar fontes TTF: {e}. Usando fontes PDF padrão.")

    def extract_exercise_info(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            exercise_info = {
                'numero': self.extract_exercise_number(file_path),
                'enunciado': self.extract_enunciado(content),
                'testes': self.extract_testes(content)
            }
            return exercise_info
        except Exception as e:
            print(f"Erro ao processar {file_path}: {e}")
            return None

    def extract_exercise_number(self, file_path_or_name):
        match = re.search(r'ch\d+_(\d+)\.txt$', os.path.basename(file_path_or_name))
        return match.group(1) if match else "???"
    
    def extract_enunciado(self, content):
        # Pega tudo da seção "Enunciado" até o início de "Code Solução" ou "Testes"
        # ou "Entrada" (se for um formato antigo de arquivo)
        # Adicionado (?i) para case-insensitive no início do nome da seção
        match = re.search(r'(?s)#### (?i)Enunciado\s*\n?(.*?)(?=\n\s*#### ((?i)Code Solu|(?i)Testes)|\n\s*(?i)Entrada:|$)', content)
        if match:
            enunciado_text = match.group(1).strip()
            
            # Substituir **texto** por <b>texto</b> para Paragraph
            enunciado_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', enunciado_text)
            # Substituir `codigo` por <font name="Courier">codigo</font>
            enunciado_text = re.sub(r'`([^`]+)`', r'<font name="Courier">\1</font>', enunciado_text)
            # Substituir \n por <br/> para preservar quebras de linha no Paragraph
            enunciado_text = enunciado_text.replace('\n', '<br/>\n')
            return enunciado_text
        return "[Enunciado não encontrado]"

    def extract_testes(self, content):
        match = re.search(r'(?s)#### (?i)Testes\s*\n?(.*?)(?=\n\s*#### ((?i)Code Solu|(?i)Enunciado)|$)', content)
        if match:
            testes_text = match.group(1).strip()
            return testes_text
        return None

    def collect_exercises(self):
        txt_files = []
        for file in os.listdir(self.questions_folder):
            # Garantir que estamos pegando apenas arquivos que parecem ser de questões
            if file.startswith('question_ch') and file.endswith('.txt') and not file.endswith('_test.txt'):
                txt_files.append(file)
        
        txt_files.sort(key=lambda f: int(self.extract_exercise_number(f))
                                    if self.extract_exercise_number(f).isdigit()
                                    else float('inf'))
        
        # print(f"Encontrados {len(txt_files)} arquivos de exercícios.")
        
        for file in txt_files:
            file_path = os.path.join(self.questions_folder, file)
            # print(f"  Processando: {file}")
            exercise_info = self.extract_exercise_info(file_path)
            if exercise_info:
                self.exercises.append(exercise_info)
        
        # print(f"\nProcessados {len(self.exercises)} exercícios com sucesso.")

    def _setup_styles(self):
        styles = getSampleStyleSheet()
        
        styles.add(ParagraphStyle(name='MainTitle', parent=styles['h1'], fontName='Helvetica-Bold',
                                  fontSize=18, alignment=TA_CENTER, spaceAfter=0.3*inch, leading=22))

        styles.add(ParagraphStyle(name='ExerciseTitle', parent=styles['h2'], fontName='Helvetica-Bold',
                                  fontSize=16, spaceBefore=0.3*inch, spaceAfter=0.15*inch, leading=18))

        styles.add(ParagraphStyle(name='SectionHeader', fontName='Helvetica-Bold',
                                  fontSize=11, spaceBefore=0.15*inch, spaceAfter=0.08*inch,
                                  leftIndent=0, leading=14)) # Removido leftIndent aqui, será no conteúdo

        styles.add(ParagraphStyle(name='EnunciadoContent', parent=styles['Normal'], fontName='Helvetica',
                                  fontSize=10, leading=14, alignment=TA_JUSTIFY,
                                  leftIndent=0.2*inch, rightIndent=0.2*inch, spaceAfter=0.1*inch,
                                  firstLineIndent=0)) # Pode adicionar firstLineIndent se quiser parágrafos indentados

        styles.add(ParagraphStyle(name='TestLabel', fontName='Helvetica-Bold',
                                  fontSize=10, spaceBefore=0.15*inch, spaceAfter=0.05*inch,
                                  leftIndent=0.2*inch, leading=12))
        
        styles.add(ParagraphStyle(name='TestSubLabel', fontName='Helvetica',
                                  fontSize=10, spaceBefore=0.05*inch, spaceAfter=0.02*inch,
                                  leftIndent=0.3*inch, leading=12)) # Aumentei um pouco o leftIndent

        styles.add(ParagraphStyle(name='PreformattedCode', parent=styles['Code'], fontName='Courier',
                                  fontSize=9, leading=11,
                                  leftIndent=0.4*inch, # Indentação para o bloco de código
                                  spaceBefore=0.02*inch, # Reduzi espaço antes
                                  spaceAfter=0.1*inch,
                                  # backColor=colors.lightgrey, # Fundo cinza claro
                                  # borderPadding=3,
                                  # borderColor=colors.darkgrey,
                                  # borderWidth=0.5
                                  ))
        return styles

    def create_pdf(self):
        doc = SimpleDocTemplate(
            self.output_file,
            pagesize=A4,
            rightMargin=0.75*inch, leftMargin=0.75*inch,
            topMargin=0.75*inch, bottomMargin=0.75*inch
        )
        
        styles = self._setup_styles()
        story = [Paragraph("Lista de Exercícios de Programação", styles['MainTitle'])]

        for i, ex in enumerate(self.exercises):
            if i > 0: # Adiciona PageBreak antes de cada novo exercício, exceto o primeiro
                story.append(PageBreak())
            
            story.append(Paragraph(f"Exercício {ex['numero']}", styles['ExerciseTitle']))

            story.append(Paragraph("Enunciado:", styles['SectionHeader']))
            story.append(Paragraph(ex['enunciado'], styles['EnunciadoContent']))

            if ex.get('testes'):
                story.append(Paragraph("Testes", styles['SectionHeader']))
                
                test_blocks = re.split(r'(\*\*Teste\s*\d+\*\*)', ex['testes'])
                
                current_test_label_text = None
                buffer = ""

                for block_idx, block_content in enumerate(test_blocks):
                    if not block_content.strip():
                        continue

                    is_label_match = re.match(r'\*\*Teste\s*\d+\*\*', block_content)
                    if is_label_match:
                        if current_test_label_text and buffer.strip():
                            self._add_test_content_to_story(story, buffer, styles)
                            buffer = ""
                        
                        current_test_label_text = block_content.strip().replace('**', '') # Remove asteriscos
                        story.append(Paragraph(current_test_label_text, styles['TestLabel']))
                    elif current_test_label_text:
                        buffer += block_content
                    elif block_idx == 0 and not is_label_match : # Caso o primeiro bloco não seja um label
                        buffer += block_content


                if buffer.strip(): # Processa o último buffer acumulado
                    self._add_test_content_to_story(story, buffer, styles)
        try:
            doc.build(story)
            print(f"\nPDF gerado com sucesso: {self.output_file}")
        except Exception as e:
            print(f"\nErro ao construir o PDF: {e}")
            import traceback
            traceback.print_exc()

    def _add_test_content_to_story(self, story, test_content, styles):
        # Remove ```python e ``` se estiverem envolvendo todo o bloco de entrada/saída
        # Isso é comum se a entrada/saída foi copiada de um markdown
        def clean_code_block(text):
            text = text.strip()
            if text.startswith('```python'):
                text = text[len('```python'):].strip()
            elif text.startswith('```'):
                 text = text[len('```'):].strip()
            if text.endswith('```'):
                text = text[:-len('```')].strip()
            return text

        # Procura por blocos de Entrada e Saída
        # Ajustado para ser mais flexível com newlines e blocos ```
        entrada_match = re.search(r'(?i)Entrada:\s*\n?(.*?)(?=\n\s*(?i)Sa[ií]da:|$)', test_content, re.DOTALL)
        saida_match = re.search(r'(?i)Sa[ií]da:\s*\n?(.*?)(?=$)', test_content, re.DOTALL)

        if entrada_match:
            story.append(Paragraph("Entrada:", styles['TestSubLabel']))
            entrada_text = clean_code_block(entrada_match.group(1).strip())
            if entrada_text:
                 story.append(Preformatted(entrada_text, styles['PreformattedCode']))
            # else: # Opcional: adicionar [Vazio] se estiver vazio
            #      story.append(Paragraph("[Vazio]", styles['PreformattedCode']))

        if saida_match:
            story.append(Paragraph("Saída:", styles['TestSubLabel']))
            saida_text = clean_code_block(saida_match.group(1).strip())
            if saida_text:
                story.append(Preformatted(saida_text, styles['PreformattedCode']))
            # else: # Opcional
            #     story.append(Paragraph("[Vazio]", styles['PreformattedCode']))


    def generate(self):
        # print("Iniciando geração da lista de exercícios...")
        self.collect_exercises()
        if self.exercises:
            self.create_pdf()
        else:
            print("Nenhum exercício foi encontrado ou processado com sucesso.")

def main():
    QUESTIONS_FOLDER = "./" 
    ch_folder_name = "questions_ch5/passed"
    
    if os.path.isdir(ch_folder_name) and os.path.exists(ch_folder_name):
        QUESTIONS_FOLDER = ch_folder_name
        print(f"Usando pasta de questões: '{QUESTIONS_FOLDER}'")
    else:
        print(f"Pasta '{ch_folder_name}' não encontrada. Verificando pasta atual '{QUESTIONS_FOLDER}' para arquivos de questões.")
        found_in_current = any(f.startswith('question_ch') and f.endswith('.txt') and not f.endswith('_test.txt')
                               for f in os.listdir(QUESTIONS_FOLDER) if os.path.isfile(os.path.join(QUESTIONS_FOLDER, f)))
        if not found_in_current:
            print(f"Nenhum arquivo de questão ('question_ch*.txt') encontrado na pasta '{QUESTIONS_FOLDER}'.")
            print(f"Certifique-se de que a pasta contém os arquivos corretos ou ajuste o nome da pasta no script.")
            return

    OUTPUT_FILE = "lista_exercicios_final.pdf" # Nome do arquivo de saída
    
    generator = ExerciseListGenerator(QUESTIONS_FOLDER, OUTPUT_FILE)
    generator.generate()

if __name__ == "__main__":
    main()