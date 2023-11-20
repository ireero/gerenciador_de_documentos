from PyPDF2 import PdfReader


class PDFController:

    def __init__(self, nome_pdf) -> None:
        self.reader = PdfReader(f'./data_temp/{nome_pdf}.pdf')
        self.number_of_pages = len(self.reader.pages)
        self.page = self.reader.pages[0]
    
    def read_pdf(self):
        text = ''
        for i,page in enumerate(self.reader.pages, start=1):
            text += f'\n ----------------------------------------------------------- Início da página {i} ----------------------------------------------------------- \n'
            text += page.extract_text()
            text += f'\n\n ----------------------------------------------------------- Fim da página {i} -----------------------------------------------------------\n'
        
        return {
            'number_of_pages': self.number_of_pages,
            'content_pages': text
        }