from flask import render_template,abort,request, url_for
from flask_login import login_required
from app.models.empresa import Empresa
from . import bp

@bp.route('/signup_company')
@login_required
def signup_company():
    return render_template('company_register.html')