import os
from flask import Blueprint, request, jsonify, make_response, render_template, render_template_string, url_for, redirect, json
from flask_login import login_required, current_user
from app import db
from flask_jwt_extended import jwt_required
from forms import NewQuote
from api.quotation_api import NewPricing
from werkzeug.utils import secure_filename
from datetime import datetime
import markdown
import gzip
import subprocess


provider = Blueprint('provider', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def my_renderer(text):
    """Inject markdown renderering into jinja template"""
    rendered_body = render_template_string(text)
    pygmented_body = markdown.markdown(rendered_body, extensions=['codehilite', 'fenced_code'])
    return pygmented_body

@provider.route('/new_quote', methods = ['POST', 'GET'])
def new_quote():
    form = NewQuote()
    #pricing = NewPricing().run()
    return render_template("new_quote.html", form=form)

@provider.route('/view_quote')
def view_quote():
    form = NewQuote()
    return render_template("new_quote.html", form=form)