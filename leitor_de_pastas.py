import os

class LeitosDePastas:

    def __init__(self) -> None:
        self.pasta = '.'
        self.pastas = []  
        self.ler_pastas()

    def ler_pastas(self):
        for diretorio, subpastas, arquivos in os.walk(self.pasta):
            for arquivo in arquivos:
                if 'git' not in os.path.join(diretorio, arquivo):
                    self.pastas.append(os.path.join(diretorio, arquivo).replace('./', ''))


l = LeitosDePastas()
print(l.pastas)