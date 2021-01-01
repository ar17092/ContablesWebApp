from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from . import bp
from app.models.libro_diario import Libro_Diario
from app.models.usuario import User
from app.forms.resgistros import LDiarioForm, PartidaForm
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
    
    form2=PartidaForm()
    if form2.validate_on_submit():
        ldiario_user = Libro_Diario.get_by_id_user(current_user.id)
        id_ldiario =ldiario_user.id_libro_diario
        nombre_partida = form2.nombre.data
        fecha = request.form['fecha']
        partida = Partida(fecha=fecha,nombre = nombre_partida,valor_debe=0,valor_haber=0, id_ldiario=id_ldiario)
        partida.save()
        return redirect(url_for('routes.librodiario'))
    libro = Libro_Diario.get_by_id_user(current_user.id)

    return render_template('user/empresa.html', form=form, form2=form2, libro=libro)

# @bp.route('/librodiario/addpartida', methods=['GET','POST'])
# @login_required
# def add_partida():
