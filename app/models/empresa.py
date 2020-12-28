from app import db
from . import rubro
class Empresa(db.Model):

    id_empresa = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False )
    id_rubro = db.Column(db.Integer, db.ForeignKey('rubro.id_rubro', ondelete = 'set null'))

    def __repr__(self):
        return f'<Empresa {self.nombre}>'

    def save(self):
        if not self.id_empresa:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Empresa.query.all()

    @staticmethod
    def get_by_id(id):
        return Empresa.query.get(id)
    