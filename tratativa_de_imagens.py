
import pytesseract
import cv2
from leitor_de_pastas import LeitorDePastas
from PIL import Image


class TratativaDeImagens:

    def __init__(self) -> None:
        print('Opções de tratativa de imagem: \n1 - Recuperar texto dentro da imagem\n2 - Criar pdf com imagem')
        escolha = input('Opção que deseja utilizar: ')
        if escolha == '1':
            l = LeitorDePastas()
            print('Escolha a imagem que deseja utilizar: ')
            for index,arquivo in enumerate(l.pastas, start=1):
                print(index,' - ',arquivo)
            index = int(input('Imagem que deseja realizar a leitura: ')) - 1
            if '.jpg' in l.pastas[index] or '.jpeg' in l.pastas[index] or '.png' in l.pastas[index] :
                imagem = cv2.imread(l.pastas[index])
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                texto = pytesseract.image_to_string(imagem)
                print('################ INICIO DE TEXTO DA IMAGEM ################\n')
                print(texto)
                print('################ FIM DE TEXTO DA IMAGEM ################')
            else:
                print('Tipo de arquivo não suportado')
        else:
            print('Função ainda não implementada')