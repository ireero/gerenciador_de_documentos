import os

class FolderReader:

    def __init__(self, folder) -> None:
        self.folder = folder
        self.folders = [] 
    
    def read_folders(self):
        for diretorio, subpastas, arquivos in os.walk(self.folder):
            for arquivo in arquivos:
                if 'git' not in os.path.join(diretorio, arquivo) and 'pycache' not in os.path.join(diretorio, arquivo):
                    self.folders.append(os.path.join(diretorio, arquivo).replace('./', '').replace('.\\', ''))