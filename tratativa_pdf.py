import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

from tika import parser


class TratativaPDF:

    def __init__(self, nome_pdf) -> None:
        self.raw = parser.from_file(nome_pdf)
        print(self.raw['content'])