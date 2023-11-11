from flask import Blueprint, render_template, request, send_file, jsonify
import uuid
from models_documents_analitics.tratativa_pdf import TratativaPDF
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