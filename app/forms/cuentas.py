from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField,TextAreaField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length


class TipocuentaForm(FlaskForm):
    nombre = StringField('Nombre Tipo cuenta', validators=[DataRequired(), Length(max=128)], render_kw={"type":"text","class":"form-control"})
    saldo = BooleanField('Saldo')
    descripcion = TextAreaField('Descripción', render_kw={'class':'form-control'})
    submit = SubmitField('Añadir', render_kw={"class":"btn btn-success"})

class CuentaForm(FlaskForm):
    nombre = StringField('Nombre cuenta', validators=[DataRequired(), Length(max=200)], render_kw={"type":"text","class":"form-control"})
    descripcion = TextAreaField('Descripción', render_kw={'class':'form-control'})
    id_tipocuenta = SelectField('Tipo cuenta', choices=[], render_kw={'class':'custom-select'})
    submit = SubmitField('Agregar', render_kw={"class":"btn btn-success"})

class SubcuentaForm(FlaskForm):
    nombre = StringField('Nombre subcuenta', validators=[DataRequired(), Length(max=200)], render_kw={"type":"text","class":"form-control"})
    descripcion = TextAreaField('Detalle', render_kw={'class':'form-control'})
    id_cuenta = SelectField('Cuenta', choices=[], render_kw={'class':'custom-select'})
    submit = SubmitField('Agregar', render_kw={"class":"btn btn-success"})