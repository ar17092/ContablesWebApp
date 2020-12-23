from flask import render_template,abort,request, url_for
from app.models.rubro import Rubro
from . import bp

@bp.route('/add_rubro')
def add_rubro():
    return render_template('add_rubro.html')