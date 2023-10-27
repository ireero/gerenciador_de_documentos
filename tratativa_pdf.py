from PyPDF2 import PdfReader


class TratativaPDF:

    def __init__(self, nome_pdf) -> None:
        self.reader = PdfReader(nome_pdf)
        print(len(self.reader.pages))
        self.page = self.reader.pages[0]
        for i,page in enumerate(self.reader.pages):
            print(f'Início da página {i}')
            print(page.extract_text())
            print(f'Fim da página {i}')