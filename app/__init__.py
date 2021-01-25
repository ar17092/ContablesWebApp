from flask_migrate import Migrate
import logging
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr

login_manager = LoginManager()
toastr = Toastr()
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

    login_manager.init_app(app)
    login_manager.login_view = "routes.login"

    #Iniciamos la db
    db.init_app(app)
    toastr.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp
    app.register_blueprint(bp)

    register_error_handlers(app)

    return app

def register_error_handlers(app):
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('errorHandler/500.html'), 500

    @app.errorhandler(404)
    def user_404_handler(e):
        return render_template('errorHandler/404.html'), 404

    @app.errorhandler(401)
    def user_401_handler(e):
        return render_template('errorHandler/401.html'), 401