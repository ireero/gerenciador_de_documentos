from zipfile import ZipFile
from leitor_de_pastas import LeitorDePastas

class TratativaDeZipagem:

    def __init__(self) -> None:
        print('Opções de zipagem:\n1 - Zipar arquivo\n2 - Descompactar arquivo')
        escolha = input('Escolha a ação que você deseja efetuar: ')
        if escolha == '1':
            l = LeitorDePastas()
            l.ler_pastas()
            for index,arquivo in enumerate(l.pastas):
                print(index+1,' - ',arquivo)
            index_escolhido = int(input("Arquivo que deseja zipar: "))
            nome_zipagem = str(input('Escolha um nome para o arquivo zipado: '))
            self.zipando_arquivo(nome_da_zipagem=nome_zipagem, arquivo_para_zipar=l.pastas[index_escolhido - 1])
        else:
            print('Escolha ainda não implementada')

    def zipando_arquivo(self, nome_da_zipagem, arquivo_para_zipar):
        with ZipFile(f'{nome_da_zipagem}.zip', 'w') as zip:
            zip.write(arquivo_para_zipar)
        print('Pronto! arquivo zipado com sucesso.')