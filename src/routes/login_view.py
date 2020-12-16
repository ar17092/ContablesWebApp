from flask import render_template,abort,request, url_for
from . import bp

@bp.route('/login')
def login():
    return render_template('login.html')