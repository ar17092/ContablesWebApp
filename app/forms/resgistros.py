from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)], render_kw={ "type":"text" ,"class":"form-control" ,"id":"formGroupExampleInput", "placeholder":"Nombre/Apellido",'required':''})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"type":"password", "class":"form-control", "id":"exampleInputPassword1", "placeholder":"Password"})
    password2 = PasswordField('Password', validators=[DataRequired()], render_kw={"type":"password", "class":"form-control", "id":"exampleInputPassword1", "placeholder":"Password"})
    username = StringField('Username', validators=[DataRequired()],render_kw={"type":"email", "class":"form-control", "id":"exampleInputEmail1", "placeholder":"example@mail.com", "aria-describedby":"emailHelp"})
    submit = SubmitField('Registrar',render_kw={"type":"submit" ,"class":"btn btn-secondary"})

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()],render_kw={"type":"text" ,"class":"form-control" ,"id":"exampleInputEmail1"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"type":"password","class":"form-control", "id":"exampleInputPassword1"})
    remember_me = BooleanField('Recuérdame',render_kw={})

class CompanyForm(FlaskForm):
    pass

class RubroFom(FlaskForm):
    pass

