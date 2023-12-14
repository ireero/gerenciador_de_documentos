from zipfile import ZipFile
from .folders_reader import FolderReader
import shutil

class ZipController:

    def __init__(self, file_name, file_type) -> None:
        self.file_name = file_name
        self.file_type = file_type

    def zipando_arquivo(self):
        with ZipFile(f'./data_temp/ziped_archive.zip', 'w') as zip:
            zip.write(f'./data_temp/{self.file_name}.{self.file_type}')
    
    def extraindo_arquivo_zipado(self):
        with ZipFile(f'./data_temp/{self.file_name}.{self.file_type}', 'r') as zip:
            zip.extractall(path=f'./data_temp')
        
        reader_f = FolderReader(folder='./data_temp')
        reader_f.read_folders()
        second_folder = ''
        for p in reader_f.folders:
            if p.count('\\') == 2:
                index = p.index('\\')
                second_index = self.findnth(haystack=p, needle='\\', n=1)
                second_folder = p[index+1:second_index]
                print(f'second_folder -> {second_folder}')
                break
        if second_folder != '':
            shutil.rmtree(f'./data_temp/{second_folder}')
        
        final_list_response = []
        for f in reader_f.folders:
            final_list_response.append(f.replace('data_temp\\', ''))
        return final_list_response
    
    def findnth(self,haystack, needle, n):
        parts= haystack.split(needle, n+1)
        if len(parts)<=n+1:
            return -1
        return len(haystack)-len(parts[-1])-len(needle)