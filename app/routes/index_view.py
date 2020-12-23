from flask import render_template,abort,request, url_for
from . import bp

@bp.route('/')
def index():
    return render_template('index.html')
