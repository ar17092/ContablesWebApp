from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from . import bp
from app.models.libro_diario import Libro_Diario
from app.models.usuario import User
from app.forms.resgistros import LDiarioForm, PartidaForm
from app.models.partida import Partida
from app.models.partida_concepto import Partida_Concepto
from slugify import slugify
from app.forms.resgistros import PConceptoForm
from app.models.cuenta import Cuenta

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
        nombre_partida = slugify(form2.nombre.data)
        fecha = request.form['fecha']
        partida = Partida(fecha=fecha,nombre = nombre_partida,valor_debe=0,valor_haber=0, id_ldiario=id_ldiario)
        partida.save()
        return redirect(url_for('routes.librodiario'))
    libro = Libro_Diario.get_by_id_user(current_user.id)

    return render_template('user/empresa.html', form=form, form2=form2, libro=libro)

@bp.route('/librodiario/<string:nombre>', methods=['GET','POST'])
@login_required
def add_partida(nombre):
    cuentas = Cuenta.get_all()
    partida = Partida.get_by_nombre(nombre)
    id_p=partida.id_partida
    form = PConceptoForm()
    form.id_cuenta.choices=[(c.id_cuenta, c.nombre) for c in cuentas]
    if form.validate_on_submit():
        id_cuenta=form.id_cuenta.data
        parcial=form.valor_parcial.data
        c_a=form.cargo_abono.data

        if c_a:
            partida.valor_debe +=parcial
            partida.save()
        else:
            partida.valor_haber += parcial
            partida.save()

        pc=Partida_Concepto(valor_parcial=parcial,id_cuenta=id_cuenta,id_partida=id_p,cargo_abono=c_a)
        pc.save()

        print("NUMERO FLOTANTE",parcial)
        return redirect(url_for('routes.librodiario'))

    return render_template('user/partidas.html',partida=partida, form=form)

@bp.route('/librodiario/update/<int:id>', methods=['GET','POST'])
@login_required
def update_partida(id):
    return render_template('user/partidas.html')