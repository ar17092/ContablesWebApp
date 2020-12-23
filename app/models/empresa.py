from app import db
from . import rubro
class Empresa(db.Model):

    id_empresa = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False )
    id_rubro = db.Column(db.Integer, db.ForeignKey('rubro.id_rubro', ondelete = 'set null'))

    def __repr__(self):
        return f'<Empresa {self.nombre}>'