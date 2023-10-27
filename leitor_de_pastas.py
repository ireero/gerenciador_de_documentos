import os
from tratativa_pdf import TratativaPDF
from tratativa_xlsx import TratativaXLSX

class LeitorDePastas:

    def __init__(self) -> None:
        self.pasta = '.'
        self.pastas = []  
        self.ler_pastas()

    def ler_pastas(self):
        for diretorio, subpastas, arquivos in os.walk(self.pasta):
            for arquivo in arquivos:
                if 'git' not in os.path.join(diretorio, arquivo) and 'pycache' not in os.path.join(diretorio, arquivo):
                    self.pastas.append(os.path.join(diretorio, arquivo).replace('./', '').replace('.\\', ''))
    

    def escolha_de_arquivo_para_leitura(self):
        print('Escolha o arquivo que deseja ler: ')
        for index,p in enumerate(self.pastas):
            print(index+1,' - ',p)
        print(len(self.pastas) + 1,' - ','Ler tudo')

        index_escolhido = int(input("Arquivo que deseja ler: "))

        if index_escolhido == len(self.pastas) + 1:
            self.ler_todos_os_arquivos()
        elif '.pdf' in self.pastas[index_escolhido - 1]:
            pdf = TratativaPDF(nome_pdf=self.pastas[index_escolhido - 1])
        elif '.xlsx' in self.pastas[index_escolhido - 1]:
            xlsx = TratativaXLSX(nome_arquivo=self.pastas[index_escolhido - 1])
        else:

            opcao_escolhida = self.pastas[index_escolhido - 1]

            arq = open(opcao_escolhida)

            linhas = arq.readlines()
            print('#### Início do arquivo ####\n')
            for linha in linhas:
                print(linha)
            print('\n#### Fim do arquivo ####')
    
    def ler_todos_os_arquivos(self):
        for arquivo in self.pastas:
            print(f'NOVO ARQUIVO: {arquivo}\n')
            if '.pdf' in arquivo:
                pdf = TratativaPDF(nome_pdf=arquivo)
            elif '.xlsx' in arquivo:
                xlsx = TratativaXLSX(nome_arquivo=arquivo)
            else:
                ar = open(arquivo)
                for index,l in enumerate(ar.readlines()):
                    print(index+1,' - ',l)
            print(f'\nFIM ARQUIVO: {arquivo}\n')