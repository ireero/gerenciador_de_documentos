from flask import Blueprint, render_template, request, send_file, jsonify, send_from_directory, Response, redirect
import uuid
from models_documents_analytics.pdf_controller import PDFController
from models_documents_analytics.image_controller import ImageController
from models_documents_analytics.zip_controller import ZipController
from models_documents_analytics.excel_controller import ExcelController
from database import BaseDeDados
import os
from datetime import datetime
import time


calls = Blueprint('calls',__name__)
mongo_db = BaseDeDados()

@calls.route('/pdf/leitura', methods=['POST'])
def pdf_reader():
    time_init = time.time()
    date_hour_init = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file = request.files['leitura_pdf']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.pdf')
    reader = PDFController(nome_pdf=process_code)
    content = reader.read_pdf()
    os.remove(f'./data_temp/{process_code}.pdf')
    requisition = {"type": "pdf", "action": "read", "date_and_hour_init": date_hour_init, 'date_and_hour_created': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'time_process': time_process_manipulation(time_init=time_init, time_end=time.time())}
    mongo_db.insert_document(requisition)
    return render_template('pdf/pdf_read_page.html', text_pdf=content['content_pages'])

@calls.route('/imagens/ler_arquivo', methods=['POST'])
def image_read_text():
    time_init = time.time()
    date_hour_init = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
    requisition = {"type": "imagem", "action": "read",'date_and_hour_init': date_hour_init, 'date_and_hour_created': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'time_process': time_process_manipulation(time_init=time_init, time_end=time.time())}
    mongo_db.insert_document(requisition)
    os.remove(f'./data_temp/{process_code}.{type}')
    return render_template('image/image_read_page.html', text_image=text)

@calls.route('/zip/zipar_arquivo', methods=['POST'])
def zip_file():
    time_init = time.time()
    date_hour_init = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file = request.files['zipando_arquivo']
    process_code = str(uuid.uuid4())
    archive_type = file.content_type.replace('application/', '').replace('image/', '')
    if archive_type == 'text/plain':
        archive_type = 'txt'
    file.save(f'./data_temp/{process_code}.{archive_type}')
    zip = ZipController(file_name=process_code, file_type=archive_type)
    zip.zipando_arquivo()
    os.remove(f'./data_temp/{process_code}.{archive_type}')
    requisition = {"type": "zip", "action": "ziping", 'date_and_hour_init': date_hour_init, 'date_and_hour_created': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'time_process': time_process_manipulation(time_init=time_init, time_end=time.time())}
    mongo_db.insert_document(requisition)
    return render_template('zip/zip_ziping_file_page.html', download=True)

@calls.route('/zip/baixar_arquivo_zipado')
def donwload_ziped_file():
    return send_file(f'./data_temp/ziped_archive.zip', mimetype='application/zip', as_attachment=True)

@calls.route('/zip/extraindo_arquivos_zipados', methods=['POST'])
def extracting_ziped_files():
    time_init = time.time()
    date_hour_init = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file = request.files['extraindo_arquivo_zipado']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.zip')
    zip = ZipController(file_name=process_code, file_type='zip')
    data = []
    data = zip.extraindo_arquivo_zipado()
    os.remove(f'./data_temp/{process_code}.zip')
    requisition = {"type": "zip", "action": "extracting", 'date_and_hour_init': date_hour_init, 'date_and_hour_created': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'time_process': time_process_manipulation(time_init=time_init, time_end=time.time())}
    mongo_db.insert_document(requisition)
    return render_template('zip/zip_extract_page.html', files_folders=data)


@calls.route('/excel/ler_arquivo', methods=['POST'])
def read_excel_file():
    time_init = time.time()
    date_hour_init = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file = request.files['leitura_excel']
    process_code = str(uuid.uuid4())
    file.save(f'./data_temp/{process_code}.xlsx')
    excel = ExcelController(archive_name=process_code)
    text_data = excel.returning_data_xlsx()
    os.remove(f'./data_temp/{process_code}.xlsx')
    requisition = {"type": "excel", "action": "read", 'date_and_hour_init': date_hour_init, 'date_and_hour_created': datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'time_process': time_process_manipulation(time_init=time_init, time_end=time.time())}
    mongo_db.insert_document(requisition)
    return render_template('excel/excel_read_page.html', text_excel=text_data)


def time_process_manipulation(time_init, time_end):
    seconds = int(time_end - time_init)

    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60   
    
    return "%d:%02d:%02d" % (hour, minutes, seconds)