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
        for index,p in enumerate(self.pastas, start=1):
            print(index,' - ',p)
        print(len(self.pastas),' - ','Ler tudo')

        index_escolhido = int(input("Arquivo que deseja ler: ")) - 1

        if index_escolhido == len(self.pastas):
            self.ler_todos_os_arquivos()
        elif '.pdf' in self.pastas[index_escolhido]:
            pdf = TratativaPDF(nome_pdf=self.pastas[index_escolhido])
        elif '.xlsx' in self.pastas[index_escolhido]:
            xlsx = TratativaXLSX(nome_arquivo=self.pastas[index_escolhido])
        else:

            opcao_escolhida = self.pastas[index_escolhido]

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
                for index,l in enumerate(ar.readlines(), start=1):
                    print(index,' - ',l)
            print(f'\nFIM ARQUIVO: {arquivo}\n')