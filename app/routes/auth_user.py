from flask import render_template,abort,request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app.models.usuario import User
from app.forms.resgistros import LoginForm, SignupForm
from . import bp

from app import login_manager

@bp.route('/signup', methods=['GET','POST'])
def signup_form():
    # form = SignupForm()
    error = None
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
            error= f'El username {username} ya esta siendo utilizado por otro usuario'
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
                return redirect(siguienteP)

    return render_template('auth/signup.html', error=error)

@bp.route('/login', methods=['GET', 'POST'])
def login():
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
            return redirect(siguientePag)
        else:
            return f'Username o contraseña incorretos'

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

#Obteniendo el id del usuario con sesión activa
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))
