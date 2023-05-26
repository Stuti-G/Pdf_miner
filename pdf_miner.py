from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import ftfy

def extract_text_from_pdf(pdf_file):
    resource_manager = PDFResourceManager()
    string_io = StringIO()
    device = TextConverter(resource_manager, string_io,  laparams=LAParams())
    interpreter = PDFPageInterpreter(resource_manager, device)

    with open(pdf_file, 'rb') as file:
        for page in PDFPage.get_pages(file, set()):
            interpreter.process_page(page)

    text = string_io.getvalue()
    device.close()
    string_io.close()
    return text

pdf_file = 'example.pdf'
text = extract_text_from_pdf(pdf_file)
print(text)

text_output = open('img_1.csv', 'w', encoding='utf-8')
text_output.write(text)
text_output.close()
 
    
file = open('img_1.csv', 'r', encoding='utf-8')
text = file.read()
text = ftfy.fix_text(text)
text = ftfy.fix_encoding(text)
