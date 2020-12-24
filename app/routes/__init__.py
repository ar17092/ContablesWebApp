from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import index_view, auth_user, registro_empresa_view, rubro_view, cuentas_views
