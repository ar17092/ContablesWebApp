from flask import render_template,abort,request, url_for
from . import bp

@bp.route('/signup')
def signup_form():
    return render_template('signup.html')