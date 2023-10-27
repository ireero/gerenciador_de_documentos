import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer


class TratativaPDF:

    def __init__(self, nome_pdf) -> None:
        print(f'Nome do pdf -> {nome_pdf}')
        self.fd = open(nome_pdf, "rb")
        self.doc = PDFDocument(self.fd)
        self.all_pages = [p for p in self.doc.pages()]
        print(self.all_pages)
        print(len(self.all_pages))