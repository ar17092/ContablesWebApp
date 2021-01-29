from flask import render_template,abort,request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models.usuario import User
from app.models.empresa import Empresa
from app.models.rubro import Rubro
from app.forms.resgistros import EmpresaForm, RubroForm
from . import bp

from app import login_manager

@bp.route('/signup', methods=['GET','POST'])
def signup_form():
    # form = SignupForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        username = request.form['username']
        contrasenia = request.form['contrasenia1']
        nombrecompleto= nombre+' '+apellido
    
        user = User.get_by_userName(username)
        if user is not None:
            flash("El username {usernombre} ya esta registrado".format(usernombre=username), 'error')
        else:
                #Agregamos al usuario
                #user.check_password(password)
                user = User(nombre = nombrecompleto, username=username)
                user.set_password(contrasenia)
                user.save()

                login_user(user, remember=True)
                siguienteP= request.args.get('next', None)
                if not siguienteP or url_parse(siguienteP).netloc != '':
                    siguienteP = url_for('routes.index')
                flash("Welcome {nombre}".format(nombre=user.nombre), 'success')
                return redirect(siguienteP)

    return render_template('auth/signup.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))

    #form = LoginForm()#Objeto del que haremos uso en su respectivo template
    if request.method == 'POST':
        username = request.form['username']
        user = User.get_by_userName(username)
        #print(user.nombre)
        if user is not None and user.check_password(request.form['contrasenia']):
          #  print('Nombre usuario',username)
            login_user(user)
            siguientePag= request.args.get('next')

            if not siguientePag or url_parse(siguientePag).netloc != '':
                siguientePag= url_for('routes.index')
            flash("Welcome {usuario}".format(usuario=user.nombre),'success')
            return redirect(siguientePag)
        else:
            flash("Username o contraseña incorrectos",'error')

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    logout_user()
    flash("Adios, vuelve pronto",'info')
    return redirect(url_for('routes.login'))

#Obteniendo el id del usuario con sesión activa
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


@bp.route('/<string:username>/', methods=["GET","POST"])
@login_required
def profile(username):
    print('Entre')
    empresa=None
    user = User.get_by_userName(username)
    #miempresa = Empresa.get_by_id(id=user.empresa_id)
    rb = Rubro.get_all()
    form1 = EmpresaForm()
    form1.id_rubro.choices=[(r.id_rubro, r.rubro) for r in rb]
    form2 = RubroForm()
    if form1.validate_on_submit():
        nombre_empresa = form1.name.data
        id_rb = form1.id_rubro.data

        empresa = Empresa(nombre=nombre_empresa,id_rubro=id_rb)
        empresa.save()
        user.empresa_id = empresa.id_empresa
        user.save()
        flash("Empresa agregada exitosamente",'success')
        return redirect(url_for('routes.profile', username=current_user.username))
        
    if form2.validate_on_submit():
        nombre_rubro = form2.name.data
        rubro = Rubro(rubro=nombre_rubro)
        rubro.save()
        flash("Rubro agregado",'info')
        return redirect(url_for('routes.profile', username = user.username))

    return render_template('user/profile.html',user=user,form1=form1, form2=form2,empresa=empresa)

# @bp.route('/addrubro', methods=["GET","POST"])
# @login_required
# def add_rubro():
#     return 'hola'
# #@bp.route('/<string:username>/', methods=["GET","POST"])
# #@login_required
