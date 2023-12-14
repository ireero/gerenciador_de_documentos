from flask import Blueprint, render_template, request, send_file, jsonify, send_from_directory, Response

navigation = Blueprint('navigation',__name__)

@navigation.route('/')
def index():
    return render_template('index.html')

# PDF
@navigation.route('/pdf_escolha')
def index_pdf():
    return render_template('pdf/pdf_page.html')

@navigation.route('/pdf_escolha/leitura')
def read_pdf_page():
    return render_template('pdf/pdf_read_page.html')

# Excel
@navigation.route('/excel_escolha')
def index_excel():
    return render_template('excel/excel_page.html')

@navigation.route('/excel_escolha/leitura')
def read_excel_page():
    return render_template('excel/excel_read_page.html')

# Zip
@navigation.route('/zip_escolha')
def index_zip():
    return render_template('zip/zip_page.html')

@navigation.route('/zip_escolha/zipar')
def zip_archive_page():
    return render_template('zip/zip_ziping_file_page.html')

@navigation.route('/zip_escolha/extrair')
def extract_zip_file():
    return render_template('zip/zip_extract_page.html')

# Image
@navigation.route('/imagem_escolha')
def index_image():
    return render_template('image/image_page.html')

@navigation.route('/imagem_escolha/leitura')
def read_image_page():
    return render_template('image/image_read_page.html')

@navigation.route('/testing')
def teste():
    return render_template('auth/login.html')