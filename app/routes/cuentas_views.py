from flask import render_template, request, redirect
from flask.helpers import url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import abort
from app.models.cuenta import Cuenta
from  app.models.sub_cuenta import Subcuenta
from app.models.tipo_cuenta import Tipo_Cuenta
from app.routes.decorator.decorators import admin_require
from app.routes import bp
from app.forms.cuentas import TipocuentaForm, CuentaForm

@bp.route('/admin/')
@login_required
@admin_require
def home():
    return render_template('admin/index.html')

@bp.route('/admin/newcuenta',methods=['GET','POST'])
@login_required
@admin_require
def new_cuenta():
    cuentas = Cuenta.get_all()
    tc = Tipo_Cuenta.get_all()
    form = CuentaForm()
    form.selector.choices=[(t.id_tipo_cuenta,t.nombre) for t in tc]

    if form.validate_on_submit():
        nombre = form.nombre.data
        info = form.descripcion.data
        id_tc = form.selector.data

        cuenta = Cuenta(nombre=nombre, descripcion=info, id_tipocuenta=id_tc)
        cuenta.save()
        return redirect(url_for('routes.new_cuenta'))      
    return render_template('admin/cuenta.html', form=form,cuentas=cuentas)

@bp.route('/admin/updatecuenta/<int:id_cuenta>', methods=['GET','POST',], )
@login_required
@admin_require
def update_cuenta(id_cuenta):
    cuentas = Cuenta.get_all()
    cuenta = Cuenta.get_by_id(id_cuenta)
    if cuenta is None:
        abort(404)
    tc = Tipo_Cuenta.get_all()
    form = CuentaForm(obj = cuenta)
    form.selector.choices=[(t.id_tipo_cuenta,t.nombre) for t in tc]
    if form.validate_on_submit():
        cuenta.nombre = form.nombre.data
        cuenta.descripcion = form.descripcion.data
        cuenta.id_tipocuenta = form.selector.data
        cuenta.save()
        return redirect(url_for('routes.new_cuenta'))
    return render_template('admin/cuenta.html',form=form, cuenta = cuenta,cuentas=cuentas)

@bp.route('/admin/deletecuenta/<int:id_cuenta>', methods=['POST',])
@login_required
@admin_require
def delete_cuenta(id_cuenta):
    cuenta = Cuenta.get_by_id(id_cuenta)
    if cuenta is None:
        abort(404)
    cuenta.delete()

    return redirect(url_for('routes.new_cuenta'))

#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#

@bp.route('/admin/newsubcuenta')
@login_required
@admin_require
def crud_subcuenta():
    return render_template('admin/subcuenta.html')

#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#

@bp.route('/admin/newtipocuenta', methods=['GET','POST',])
@login_required
@admin_require
def crud_tipocuenta():
    tipos_cuenta = Tipo_Cuenta.get_all()
    form = TipocuentaForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        info = form.descripcion.data
        saldo = form.saldo.data
        tipo_cuenta = Tipo_Cuenta(nombre=nombre, saldo=saldo)
        tipo_cuenta.save()
        return redirect(url_for('routes.crud_tipocuenta'))
    return render_template('admin/tipocuenta.html', form =form,tipos_cuenta=tipos_cuenta )

@bp.route('/admin/updatetipocuenta/<int:id_tipo_cuenta>', methods=['GET','POST',])
@login_required
@admin_require
def update_tipocuenta(id_tipo_cuenta):
    tipos_cuenta = Tipo_Cuenta.get_all()
    tipo_cuenta = Tipo_Cuenta.get_by_id(id_tipo_cuenta)
    if tipo_cuenta is None:
        abort(404)
    
    form = TipocuentaForm(obj = tipo_cuenta)
    if form.validate_on_submit():
        tipo_cuenta.nombre = form.nombre.data
        tipo_cuenta.descripcion = form.descripcion.data
        tipo_cuenta.saldo = form.saldo.data
        tipo_cuenta.save()
        return redirect(url_for('routes.home'))
    return render_template('admin/tipocuenta.html',form=form, tipo_cuenta = tipo_cuenta,tipos_cuenta=tipos_cuenta)

@bp.route('/admin/deletetipocuenta/<int:id_tipo_cuenta>', methods=['POST',])
@login_required
@admin_require
def delete_tipo_cuenta(id_tipo_cuenta):
    tipo_cuenta = Tipo_Cuenta.get_by_id(id_tipo_cuenta)
    if tipo_cuenta is None:
        abort(404)
    tipo_cuenta.delete()

    return redirect(url_for('routes.crud_tipocuenta'))