from flask import Blueprint, render_template, request, send_file, jsonify, send_from_directory, Response, redirect
import uuid
from models_documents_analytics.pdf_controller import PDFController
from models_documents_analytics.image_controller import ImageController
from models_documents_analytics.zip_controller import ZipController
from models_documents_analytics.excel_controller import ExcelController
import os

calls = Blueprint('calls',__name__)

@calls.route('/pdf/leitura', methods=['POST'])
def pdf_reader():
    file = request.files['leitura_pdf']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.pdf')
    reader = PDFController(nome_pdf=process_code)
    content = reader.read_pdf()
    os.remove(f'./data_temp/{process_code}.pdf')
    return render_template('pdf/pdf_read_page.html', text_pdf=content['content_pages'])

@calls.route('/imagens/ler_arquivo', methods=['POST'])
def image_read_text():
    file = request.files['leitura_image']
    process_code = str(uuid.uuid4())
    type = ''
    if 'png' in file.content_type:
        file.save(f'./data_temp/{process_code}.png')
        type = 'png'
    elif 'jpg' in file.content_type or 'jpeg' in file.content_type:
        file.save(f'./data_temp/{process_code}.jpg')
        type = 'jpg'
    else:
        return render_template('image/image_read_page.html', text_image='Erro, tipo de arquivo inválido para este processo')
    
    image = ImageController(image_name=process_code, type=type)
    text = image.read_text()
    os.remove(f'./data_temp/{process_code}.{type}')
    return render_template('image/image_read_page.html', text_image=text)

@calls.route('/zip/zipar_arquivo')
def zip_file():
    file = request.files['file']
    process_code = str(uuid.uuid4())
    archive_type = file.content_type.replace('application/', '').replace('image/', '')
    file.save(f'./data_temp/{process_code}.{archive_type}')
    zip = ZipController(file_name=process_code, file_type=archive_type)
    zip.zipando_arquivo()
    # os.remove(f'./data_temp/{process_code}.{archive_type}')
    return send_file(f'./data_temp/ziped_archive.zip', mimetype='application/zip', as_attachment=True)

@calls.route('/zip/extranindo_arquivos_zipados', methods=['POST'])
def extracting_ziped_files():
    file = request.files['extraindo_arquivo_zipado']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.zip')
    zip = ZipController(file_name=process_code, file_type='zip')
    data = []
    data = zip.extraindo_arquivo_zipado()
    os.remove(f'./data_temp/{process_code}.zip')
    return render_template('zip/zip_extract_page.html', files_folders=data)

@calls.route('/zip/extraindo_arquivos_zipados')
def donwload_extracted_zip():
    return send_file()

@calls.route('/excel/ler_arquivo', methods=['POST'])
def read_excel_file():
    file = request.files['leitura_excel']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.xlsx')
    excel = ExcelController(archive_name=process_code)
    text_data = excel.returning_data_xlsx()
    os.remove(f'./data_temp/{process_code}.xlsx')
    return render_template('excel/excel_read_page.html', text_excel=text_data)