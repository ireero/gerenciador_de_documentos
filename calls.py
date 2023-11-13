from flask import Blueprint, render_template, request, send_file, jsonify, send_from_directory, Response
import uuid
from models_documents_analitics.tratativa_pdf import TratativaPDF
from models_documents_analitics.tratativa_de_imagens import TratativaDeImagens
from models_documents_analitics.tratativa_de_zipagem import TratativaDeZipagem
from models_documents_analitics.tratativa_xlsx import TratativaXLSX
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
        file.save(f'./data_temp/{process_code}.jpg')
        type = 'jpg'
    else:
        return 'Erro, tipo de arquivo inválido para este processo'
    
    image = TratativaDeImagens(image_name=process_code, type=type)
    text = image.read_text()
    os.remove(f'./data_temp/{process_code}.{type}')
    return {
        'texto_da_imagem': text
    }

@calls.route('/zip/zipar_arquivo')
def zip_file():
    file = request.files['file']
    process_code = str(uuid.uuid4())
    archive_type = file.content_type.replace('application/', '').replace('image/', '')
    file.save(f'./data_temp/{process_code}.{archive_type}')
    zip = TratativaDeZipagem(file_name=process_code, file_type=archive_type)
    zip.zipando_arquivo()
    # os.remove(f'./data_temp/{process_code}.{archive_type}')
    return send_file(f'./data_temp/ziped_archive.zip', mimetype='application/zip', as_attachment=True)

@calls.route('/zip/extranindo_arquivos_zipados')
def extracting_ziped_files():
    file = request.files['file']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.zip')
    zip = TratativaDeZipagem(file_name=process_code, file_type='zip')
    data = zip.extraindo_arquivo_zipado()
    os.remove(f'./data_temp/{process_code}.zip')
    return data

@calls.route('/excel/ler_arquivo')
def read_excel_file():
    file = request.files['file']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.xlsx')
    excel = TratativaXLSX(archive_name=process_code)
    text_data = excel.returning_data_xlsx()
    os.remove(f'./data_temp/{process_code}.xlsx')
    return str(text_data)