from flask import Blueprint, render_template, request, send_file, jsonify

calls = Blueprint('calls',__name__)

@calls.route('/')
def index():
    return render_template('index.html')