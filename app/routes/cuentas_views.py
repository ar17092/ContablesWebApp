from flask import render_template, request, redirect
from flask.helpers import url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import abort
from app.models.cuenta import Cuenta
from  app.models.sub_cuenta import Subcuenta
from app.models.tipo_cuenta import Tipo_Cuenta
from app.routes.decorator.decorators import admin_require
from app.routes import bp
from app.forms.cuentas import TipocuentaForm, CuentaForm, SubcuentaForm

@bp.route('/admin/')
@login_required
@admin_require
def home():
    return render_template('admin/index.html')

#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------CRUD CUENTA FUNCIONAL---------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#

@bp.route('/admin/newcuenta',methods=['GET','POST'])
@login_required
@admin_require
def new_cuenta():
    cuentas = Cuenta.get_all()
    tc = Tipo_Cuenta.get_all()
    form = CuentaForm()
    form.id_tipocuenta.choices=[(t.id_tipo_cuenta,t.nombre) for t in tc]

    if form.validate_on_submit():
        nombre = form.nombre.data
        info = form.descripcion.data
        id_tc = form.id_tipocuenta.data

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
    form.id_tipocuenta.choices=[(t.id_tipo_cuenta,t.nombre) for t in tc]
    if form.validate_on_submit():
        cuenta.nombre = form.nombre.data
        cuenta.descripcion = form.descripcion.data
        cuenta.id_tipocuenta = form.id_tipocuenta.data
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
#-----------------------------------------CRUD SUBCUENTA FUNCIONAL--------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------#

@bp.route('/admin/newsubcuenta',methods=['GET','POST'])
@login_required
@admin_require
def new_subcuenta():
    subcuentas = Subcuenta.get_all()
    c = Cuenta.get_all()
    form = SubcuentaForm()
    form.id_cuenta.choices=[(sc.id_cuenta,sc.nombre) for sc in c]

    if form.validate_on_submit():
        nombre = form.nombre.data
        info = form.descripcion.data
        id_c = form.id_cuenta.data

        subcuenta = Subcuenta(nombre=nombre, descripcion=info, id_cuenta=id_c)
        subcuenta.save()
        return redirect(url_for('routes.new_subcuenta'))      
    return render_template('admin/subcuenta.html', form=form,subcuentas=subcuentas)

@bp.route('/admin/updatesubcuenta/<int:id_subcuenta>', methods=['GET','POST',], )
@login_required
@admin_require
def update_subcuenta(id_subcuenta):
    subcuentas = Subcuenta.get_all()
    subcuenta = Subcuenta.get_by_id(id_subcuenta)
    if subcuenta is None:
        abort(404)
    c = Cuenta.get_all()
    form = SubcuentaForm(obj = subcuenta)
    form.id_cuenta.choices=[(sc.id_cuenta,sc.nombre) for sc in c]
    if form.validate_on_submit():
        subcuenta.nombre = form.nombre.data
        subcuenta.descripcion = form.descripcion.data
        subcuenta.id_tipocuenta = form.id_cuenta.data
        subcuenta.save()
        return redirect(url_for('routes.new_subcuenta'))
    return render_template('admin/subcuenta.html',form=form, subcuenta = subcuenta,subcuentas=subcuentas)

@bp.route('/admin/deletesubcuenta/<int:id_subcuenta>', methods=['POST',])
@login_required
@admin_require
def delete_subcuenta(id_subcuenta):
    subcuenta = Subcuenta.get_by_id(id_subcuenta)
    if subcuenta is None:
        abort(404)
    subcuenta.delete()

    return redirect(url_for('routes.new_subcuenta'))

#-------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------CRUD TIPOCUENTA FUNCIONAL-----------------------------------------------------------------#
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