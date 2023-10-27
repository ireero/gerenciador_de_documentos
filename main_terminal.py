from leitor_de_pastas import LeitosDePastas

l = LeitosDePastas()
continua = True

while continua:

    l.escolha_de_arquivo_para_leitura()
    
    resp = input('Deseja continuar a leitura de arquivos? (s -> Sim, n -> Não) ')

    if resp == 's':
        continua = True
    else:
        continua = False