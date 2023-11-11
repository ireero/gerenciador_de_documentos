from zipfile import ZipFile
from leitor_de_pastas import LeitorDePastas
import os

class TratativaDeZipagem:

    def __init__(self) -> None:
        print('Opções de zipagem:\n1 - Zipar arquivo\n2 - Descompactar arquivo')
        escolha = input('Escolha a ação que você deseja efetuar: ')
        if escolha == '1':
            l = LeitorDePastas()
            for index,arquivo in enumerate(l.pastas, start=1):
                print(index,' - ',arquivo)
            index_escolhido = int(input("Arquivo que deseja zipar: ")) - 1
            nome_zipagem = str(input('Escolha um nome para o arquivo zipado: '))
            self.zipando_arquivo(nome_da_zipagem=nome_zipagem, arquivo_para_zipar=l.pastas[index_escolhido])
        elif escolha == '2':
            l = LeitorDePastas()
            for index,arquivo in enumerate(l.pastas, start=1):
                print(index,' - ',arquivo)
            index_escolhido = int(input("Arquivo que deseja zipar: ")) - 1
            if '.zip' in l.pastas[index_escolhido]:
                self.extraindo_arquivo_zipado(nome_do_arquivo=l.pastas[index_escolhido])
            else:
                print('Este arquivo não é um arquivo zipado')

    def zipando_arquivo(self, nome_da_zipagem, arquivo_para_zipar):
        with ZipFile(f'{nome_da_zipagem}.zip', 'w') as zip:
            zip.write(arquivo_para_zipar)
        print('Pronto! arquivo zipado com sucesso.')
    
    def extraindo_arquivo_zipado(self, nome_do_arquivo):
        with ZipFile(nome_do_arquivo, 'r') as zip:
            zip.extractall()
        print('Pronto! arquivo descompactado com sucesso')
        print('Deseja excluir o arquivo zipado? ')
        excluir = input('Digite s para Sim e n para Não: ')
        if excluir == 's':
            os.remove(nome_do_arquivo)
            print('Pronto! arquivo removido com sucesso')
        elif excluir == 'n':
            print('OK! processo finalizado.')
        else:
            print('Por favor digite um valor válido')