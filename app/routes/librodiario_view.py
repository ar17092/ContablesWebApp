from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import bp
from app.models.libro_diario import Libro_Diario
from app.models.usuario import User
from app.forms.resgistros import LDiarioForm
from app.models.partida import Partida
from app.models.partida_concepto import Partida_Concepto

@bp.route('/librodiario',methods=['GET','POST'])
@login_required
def librodiario():
    ldiario = None
    id_usuario = current_user.id
    form = LDiarioForm()
    if form.validate_on_submit():
        name = form.name.data
        info = form.descripcion.data
        
        ldiario = Libro_Diario(nombre=name, descripcion = info, id_user = id_usuario)
        ldiario.save()

        return redirect(url_for('routes.librodiario'))

    return render_template('user/empresa.html', form=form)