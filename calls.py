from flask import Blueprint, render_template, request, send_file, jsonify

calls = Blueprint('calls',__name__)