from leitor_de_pastas import LeitorDePastas
from tratativa_de_zipagem import TratativaDeZipagem

continua = True

def escolha():
    print('Ações disponíveis: \n1 - Leitura de arquivo\n2 - Zipagem de arquivo\n3 - Substituição de texto\n4 - Leitura de texto em imagens')
    escolha = input('Digite a opção que você deseja: ')
    if escolha == '1':
        l = LeitorDePastas()
        l.escolha_de_arquivo_para_leitura()
        continuar = input('Deseja continuar a leitura de arquivos? (s -> Sim, n -> Não) ')
        return continuar
    elif escolha == '2':
        z = TratativaDeZipagem()
        
    else:
        print('Ação não implementada')
        return 's'

while continua:

    resp = escolha()

    if resp == 's':
        continua = True
    else:
        continua = False