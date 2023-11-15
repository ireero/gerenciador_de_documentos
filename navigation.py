from flask import Blueprint, render_template, request, send_file, jsonify, send_from_directory, Response

navigation = Blueprint('navigation',__name__)

@navigation.route('/')
def index():
    return render_template('index.html')

@navigation.route('/pdf_escolha')
def index_pdf():
    return render_template('pdf_page.html')