from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)

    #seteamos las configuraciones
    app.config.from_object(settings_module)

    #Cargamos las configuraciones establecidas para nuestra app
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)

    configure_logging(app)

    #Indicamos donde debe hacer login
    login_manager.init_app(app)
    login_manager.login_view("routes.login")

    #Iniciamos la db
    db.init_app(app)
    
