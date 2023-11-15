from zipfile import ZipFile
import os

class ZipController:

    def __init__(self, file_name, file_type) -> None:
        self.file_name = file_name
        self.file_type = file_type

    def zipando_arquivo(self):
        with ZipFile(f'./data_temp/ziped_archive.zip', 'w') as zip:
            zip.write(f'./data_temp/{self.file_name}.{self.file_type}')
    
    def extraindo_arquivo_zipado(self):
        with ZipFile(f'./data_temp_{self.file_name}.{self.file_type}', 'r') as zip:
            data = zip.extractall()
        return data