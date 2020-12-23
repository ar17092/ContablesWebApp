from flask import render_template,abort,request, url_for
from app.models.empresa import Empresa
from . import bp

@bp.route('/signup_company')
def signup_company():
    return render_template('company_register.html')