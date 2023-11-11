from leitor_de_pastas import LeitorDePastas
from tratativa_de_zipagem import TratativaDeZipagem
from tratativa_de_imagens import TratativaDeImagens
import os


continua = True

def escolha():
    print('Ações disponíveis: \n1 - Leitura de arquivo\n2 - Zipagem de arquivo\n3 - Substituição de texto\n4 - Leitura de texto em imagens\n5 - Deletar arquivo')
    escolha = input('Digite a opção que você deseja: ')
    if escolha == '1':
        l = LeitorDePastas()
        l.escolha_de_arquivo_para_leitura()
        continuar = input('Deseja continuar a leitura de arquivos? (s -> Sim, n -> Não) ')
        return continuar
    elif escolha == '2':
        z = TratativaDeZipagem()
    elif escolha == '4':
        i = TratativaDeImagens()
    elif escolha == '5':
        l = LeitorDePastas()
        for index,arquivo in enumerate(l.pastas, start=1):
            print(index,' - ',arquivo)
        index = int(input('Arquivo que deseja apagar: ')) - 1
        os.remove(l.pastas[index])
        print('Pronto! arquivo removido com sucesso')
    else:
        print('Ação não implementada')
        return 's'

while continua:

    resp = escolha()

    if resp == 's':
        continua = True
    else:
        continua = False