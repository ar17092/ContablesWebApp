from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.core import SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired,Length

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

class EmpresaForm(FlaskForm):
    name = StringField('Nombre empresa', validators=[DataRequired(), Length(max=64)], render_kw={ "type":"text" ,"class":"form-control" ,"id":"formGroupExampleInput",'required':''})
    id_rubro = SelectField('Rubro', choices=[], render_kw={'class':'custom-select'})

class RubroForm(FlaskForm):
    name = StringField('Rubro', validators=[DataRequired(), Length(max=64)], render_kw={ "type":"text" ,"class":"form-control" ,"id":"formGroupExampleInput",'required':''})
    submit= SubmitField('Agregar')

class LDiarioForm(FlaskForm):
    name = name = StringField('Nombre Libro Diario', validators=[DataRequired(), Length(max=200)], render_kw={ "type":"text" ,"class":"form-control" ,"id":"ldiarioform",'required':''})
    descripcion = TextAreaField('Descripción', render_kw={'class':'form-control'})
