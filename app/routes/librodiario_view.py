from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from werkzeug.exceptions import abort
from . import bp
from app.models.libro_diario import Libro_Diario
from app.models.usuario import User
from app.models.empresa import Empresa
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
        flash("Libro diario agregado con éxito", 'success')
        return redirect(url_for('routes.librodiario'))

    empresa = Empresa.get_by_id(current_user.empresa_id)
    nombreE = empresa.nombre
    form2=PartidaForm()
    if form2.validate_on_submit():
        ldiario_user = Libro_Diario.get_by_id_user(current_user.id)
        id_ldiario =ldiario_user.id_libro_diario
        nombre_partida = slugify(nombreE+"-"+form2.nombre.data)
        fecha = request.form['fecha']
        partida = Partida(fecha=fecha,nombre = nombre_partida,valor_debe=0,valor_haber=0, id_ldiario=id_ldiario)
        partida.save()
        flash("Partida creada",'info')
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
        flash("Ok", 'success')
        return redirect(url_for('routes.add_partida', nombre=partida.nombre ))

    return render_template('user/partidas.html',partida=partida, form=form)

@bp.route('/librodiario/update/<int:id>', methods=['GET','POST'])
@login_required
def update_c_partida(id):
    partida_concepto = Partida_Concepto.get_by_id(id)
    partida = Partida.get_by_id(partida_concepto.id_partida)
    cuentas = Cuenta.get_all()
    if partida_concepto is None:
        abort(404)

    if partida_concepto.cargo_abono:
        partida.valor_debe -=partida_concepto.valor_parcial
    else:
        partida.valor_haber -=partida_concepto.valor_parcial
    
    form=PConceptoForm(obj=partida_concepto)
    form.id_cuenta.choices=[(c.id_cuenta, c.nombre) for c in cuentas]
    if form.validate_on_submit():
        partida_concepto.valor_parcial = form.valor_parcial.data
        partida_concepto.cargo_abono=form.cargo_abono.data
        partida_concepto.id_cuenta=form.id_cuenta.data

        if form.cargo_abono.data:
            partida.valor_debe += form.valor_parcial.data
        else:
            partida.valor_haber += form.valor_parcial.data
        partida_concepto.save()
        partida.save()
        flash("Ok", 'success')
        return redirect(url_for('routes.add_partida', nombre=partida.nombre ))


    return render_template('user/partidas.html',partida=partida, form=form, partida_concepto=partida_concepto)

@bp.route('/librodiario/delete/<int:id_partida_concepto>', methods=['POST',])
@login_required
def delete_partida_concepto(id_partida_concepto):
    partida_concepto=Partida_Concepto.get_by_id(id_partida_concepto)
    if partida_concepto is None:
        abort(404)
    id_p=partida_concepto.id_partida
    parcial= partida_concepto.valor_parcial
    partida = Partida.get_by_id(id_p)
    if partida_concepto.cargo_abono:
        partida.valor_debe -=parcial
    else:
        partida.valor_haber -=parcial
    partida_concepto.delete()
    partida.save()
    flash("Ok", 'info')
    return redirect(url_for('routes.add_partida', nombre=partida.nombre))