from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import index_view, auth_user, cuentas_views, librodiario_view
