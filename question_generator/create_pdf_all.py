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
    """
    A class to generate PDF exercise lists from text files containing programming exercises.
    """
    
    def __init__(self, questions_folder, output_file="lista_exercicios.pdf"):
        """
        Initialize the ExerciseListGenerator with folder path and output file name.
        
        Args:
            questions_folder (str): Path to the folder containing exercise text files
            output_file (str): Name of the output PDF file
        """
        self.questions_folder = questions_folder
        self.output_file = output_file
        self.exercises = []
        self._register_fonts()

    def _register_fonts(self):
        """
        Register TTF fonts for the PDF document, using default PDF fonts as fallback.
        """
        try:
            if not any(font[0] == 'Helvetica' for font in pdfmetrics.getRegisteredFontNames()):
                 pdfmetrics.registerFont(TTFont('Helvetica', 'Helvetica'))
                 pdfmetrics.registerFont(TTFont('Helvetica-Bold', 'Helvetica-Bold'))
            if not any(font[0] == 'Courier' for font in pdfmetrics.getRegisteredFontNames()):
                 pdfmetrics.registerFont(TTFont('Courier', 'Courier'))
            # print("Fonts registered (or default ones will be used).")
        except Exception as e:
            print(f"Warning: Problem registering TTF fonts: {e}. Using default PDF fonts.")

    def extract_exercise_info(self, file_path):
        """
        Extract exercise information from a text file including number, statement, and tests.
        
        Args:
            file_path (str): Path to the exercise text file
            
        Returns:
            dict: Dictionary containing exercise number, statement, and tests, or None if error
        """
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
            print(f"Error processing {file_path}: {e}")
            return None

    def extract_exercise_number(self, file_path_or_name):
        """
        Extract exercise number from filename using regex pattern.
        
        Args:
            file_path_or_name (str): File path or filename
            
        Returns:
            str: Exercise number or "???" if not found
        """
        match = re.search(r'ch\d+_(\d+)\.txt$', os.path.basename(file_path_or_name))
        return match.group(1) if match else "???"
    
    def extract_enunciado(self, content):
        """
        Extract the exercise statement from file content, converting markdown formatting to HTML.
        
        Args:
            content (str): Full content of the exercise file
            
        Returns:
            str: Formatted exercise statement with HTML tags
        """
        # Get everything from "Enunciado" section until "Code Solution" or "Tests" begins
        # or "Entrada" (if using old file format)
        # Added (?i) for case-insensitive matching at section name start
        match = re.search(r'(?s)#### (?i)Enunciado\s*\n?(.*?)(?=\n\s*#### ((?i)Code Solu|(?i)Testes)|\n\s*(?i)Entrada:|$)', content)
        if match:
            enunciado_text = match.group(1).strip()
            
            # Replace **text** with <b>text</b> for Paragraph
            enunciado_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', enunciado_text)
            # Replace `code` with <font name="Courier">code</font>
            enunciado_text = re.sub(r'`([^`]+)`', r'<font name="Courier">\1</font>', enunciado_text)
            # Replace \n with <br/> to preserve line breaks in Paragraph
            enunciado_text = enunciado_text.replace('\n', '<br/>\n')
            return enunciado_text
        return "[Statement not found]"

    def extract_testes(self, content):
        """
        Extract test cases from file content.
        
        Args:
            content (str): Full content of the exercise file
            
        Returns:
            str: Test cases content or None if not found
        """
        match = re.search(r'(?s)#### (?i)Testes\s*\n?(.*?)(?=\n\s*#### ((?i)Code Solu|(?i)Enunciado)|$)', content)
        if match:
            testes_text = match.group(1).strip()
            return testes_text
        return None

    def collect_exercises(self):
        """
        Collect and sort exercise files from the questions folder.
        """
        txt_files = []
        for file in os.listdir(self.questions_folder):
            # Ensure we're only getting files that appear to be exercise questions
            if file.startswith('question_ch') and file.endswith('.txt') and not file.endswith('_test.txt'):
                txt_files.append(file)
        
        txt_files.sort(key=lambda f: int(self.extract_exercise_number(f))
                                    if self.extract_exercise_number(f).isdigit()
                                    else float('inf'))
        
        # print(f"Found {len(txt_files)} exercise files.")
        
        for file in txt_files:
            file_path = os.path.join(self.questions_folder, file)
            # print(f"  Processing: {file}")
            exercise_info = self.extract_exercise_info(file_path)
            if exercise_info:
                self.exercises.append(exercise_info)
        
        # print(f"\nProcessed {len(self.exercises)} exercises successfully.")

    def _setup_styles(self):
        """
        Setup paragraph styles for the PDF document.
        
        Returns:
            StyleSheet1: ReportLab stylesheet with custom styles
        """
        styles = getSampleStyleSheet()
        
        styles.add(ParagraphStyle(name='MainTitle', parent=styles['h1'], fontName='Helvetica-Bold',
                                  fontSize=18, alignment=TA_CENTER, spaceAfter=0.3*inch, leading=22))

        styles.add(ParagraphStyle(name='ExerciseTitle', parent=styles['h2'], fontName='Helvetica-Bold',
                                  fontSize=16, spaceBefore=0.3*inch, spaceAfter=0.15*inch, leading=18))

        styles.add(ParagraphStyle(name='SectionHeader', fontName='Helvetica-Bold',
                                  fontSize=11, spaceBefore=0.15*inch, spaceAfter=0.08*inch,
                                  leftIndent=0, leading=14)) # Removed leftIndent here, will be in content

        styles.add(ParagraphStyle(name='EnunciadoContent', parent=styles['Normal'], fontName='Helvetica',
                                  fontSize=10, leading=14, alignment=TA_JUSTIFY,
                                  leftIndent=0.2*inch, rightIndent=0.2*inch, spaceAfter=0.1*inch,
                                  firstLineIndent=0)) # Can add firstLineIndent if you want indented paragraphs

        styles.add(ParagraphStyle(name='TestLabel', fontName='Helvetica-Bold',
                                  fontSize=10, spaceBefore=0.15*inch, spaceAfter=0.05*inch,
                                  leftIndent=0.2*inch, leading=12))
        
        styles.add(ParagraphStyle(name='TestSubLabel', fontName='Helvetica',
                                  fontSize=10, spaceBefore=0.05*inch, spaceAfter=0.02*inch,
                                  leftIndent=0.3*inch, leading=12)) # Increased leftIndent slightly

        styles.add(ParagraphStyle(name='PreformattedCode', parent=styles['Code'], fontName='Courier',
                                  fontSize=9, leading=11,
                                  leftIndent=0.4*inch, # Indentation for code block
                                  spaceBefore=0.02*inch, # Reduced space before
                                  spaceAfter=0.1*inch,
                                  # backColor=colors.lightgrey, # Light gray background
                                  # borderPadding=3,
                                  # borderColor=colors.darkgrey,
                                  # borderWidth=0.5
                                  ))
        return styles

    def create_pdf(self):
        """
        Create the PDF document with all collected exercises.
        """
        doc = SimpleDocTemplate(
            self.output_file,
            pagesize=A4,
            rightMargin=0.75*inch, leftMargin=0.75*inch,
            topMargin=0.75*inch, bottomMargin=0.75*inch
        )
        
        styles = self._setup_styles()
        story = [Paragraph("Lista de Exercícios de Programação", styles['MainTitle'])]

        for i, ex in enumerate(self.exercises):
            if i > 0: # Add PageBreak before each new exercise, except the first
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
                        
                        current_test_label_text = block_content.strip().replace('**', '') # Remove asterisks
                        story.append(Paragraph(current_test_label_text, styles['TestLabel']))
                    elif current_test_label_text:
                        buffer += block_content
                    elif block_idx == 0 and not is_label_match : # Case where first block is not a label
                        buffer += block_content

                if buffer.strip(): # Process the last accumulated buffer
                    self._add_test_content_to_story(story, buffer, styles)
        try:
            doc.build(story)
            print(f"\nPDF generated successfully: {self.output_file}")
        except Exception as e:
            print(f"\nError building PDF: {e}")
            import traceback
            traceback.print_exc()

    def _add_test_content_to_story(self, story, test_content, styles):
        """
        Add test content (input/output) to the PDF story with proper formatting.
        
        Args:
            story (list): ReportLab story list to append content to
            test_content (str): Raw test content to process
            styles (StyleSheet1): ReportLab styles for formatting
        """
        # Remove ```python and ``` if they're wrapping the entire input/output block
        # This is common if the input/output was copied from markdown
        def clean_code_block(text):
            text = text.strip()
            if text.startswith('```python'):
                text = text[len('```python'):].strip()
            elif text.startswith('```'):
                 text = text[len('```'):].strip()
            if text.endswith('```'):
                text = text[:-len('```')].strip()
            return text

        # Search for Input and Output blocks
        # Adjusted to be more flexible with newlines and ``` blocks
        entrada_match = re.search(r'(?i)Entrada:\s*\n?(.*?)(?=\n\s*(?i)Sa[ií]da:|$)', test_content, re.DOTALL)
        saida_match = re.search(r'(?i)Sa[ií]da:\s*\n?(.*?)(?=$)', test_content, re.DOTALL)

        if entrada_match:
            story.append(Paragraph("Entrada:", styles['TestSubLabel']))
            entrada_text = clean_code_block(entrada_match.group(1).strip())
            if entrada_text:
                 story.append(Preformatted(entrada_text, styles['PreformattedCode']))
            # else: # Optional: add [Empty] if empty
            #      story.append(Paragraph("[Empty]", styles['PreformattedCode']))

        if saida_match:
            story.append(Paragraph("Saída:", styles['TestSubLabel']))
            saida_text = clean_code_block(saida_match.group(1).strip())
            if saida_text:
                story.append(Preformatted(saida_text, styles['PreformattedCode']))
            # else: # Optional
            #     story.append(Paragraph("[Empty]", styles['PreformattedCode']))

    def generate(self):
        """
        Main method to generate the complete exercise list PDF.
        """
        # print("Starting exercise list generation...")
        self.collect_exercises()
        if self.exercises:
            self.create_pdf()
        else:
            print("No exercises were found or processed successfully.")

def main():
    """
    Main function to execute the PDF generation process.
    """
    QUESTIONS_FOLDER = "./" 
    ch_folder_name = "questions_ch5/passed"
    
    if os.path.isdir(ch_folder_name) and os.path.exists(ch_folder_name):
        QUESTIONS_FOLDER = ch_folder_name
        print(f"Using questions folder: '{QUESTIONS_FOLDER}'")
    else:
        print(f"Folder '{ch_folder_name}' not found. Checking current folder '{QUESTIONS_FOLDER}' for question files.")
        found_in_current = any(f.startswith('question_ch') and f.endswith('.txt') and not f.endswith('_test.txt')
                               for f in os.listdir(QUESTIONS_FOLDER) if os.path.isfile(os.path.join(QUESTIONS_FOLDER, f)))
        if not found_in_current:
            print(f"No question files ('question_ch*.txt') found in folder '{QUESTIONS_FOLDER}'.")
            print(f"Make sure the folder contains the correct files or adjust the folder name in the script.")
            return

    OUTPUT_FILE = "lista_exercicios_final.pdf" # Output file name
    
    generator = ExerciseListGenerator(QUESTIONS_FOLDER, OUTPUT_FILE)
    generator.generate()

if __name__ == "__main__":
    main()