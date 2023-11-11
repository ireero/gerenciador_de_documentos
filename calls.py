from flask import Blueprint, render_template, request, send_file, jsonify
import uuid
from models_documents_analitics.tratativa_pdf import TratativaPDF
from models_documents_analitics.tratativa_de_imagens import TratativaDeImagens
import os

calls = Blueprint('calls',__name__)

@calls.route('/')
def index():
    return render_template('index.html')

@calls.route('/pdf/leitura')
def pdf_reader():
    file = request.files['file']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.pdf')
    reader = TratativaPDF(nome_pdf=process_code)
    content = reader.read_pdf()
    os.remove(f'./data_temp/{process_code}.pdf')
    return jsonify(content)

@calls.route('/imagens/retirar_texto')
def image_read_text():
    file = request.files['file']
    process_code = str(uuid.uuid4())
    type = ''
    if 'png' in file.content_type:
        file.save(f'./data_temp/{process_code}.png')
        type = 'png'
    elif 'jpg' in file.content_type or 'jpeg' in file.content_type:
        file.save(f'./data_temp/{process_code}.jpeg')
        type = 'jpg'
    else:
        return 'Erro, tipo de arquivo inválido para este processo'
    
    image = TratativaDeImagens(image_name=process_code, type=type)
    text = image.read_text()
    os.remove(f'./data_temp/{process_code}.{type}')
    return {
        'texto_da_imagem': text
    }
