from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import index_view,login_view,signup_view
