from app import db

class Tipo_Cuenta(db.Model):

    __tablename__ = 'tipo_cuenta'

    id_tipo_cuenta = db.Column(db.INTEGER, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.String(200))
    saldo = db.Column(db.BOOLEAN, default=False)#True = Acreedor, False = Deudor

    def __repr__(self):
        return f'Tipo_Cuenta {self.nombre}'

    def save(self):
        if not self.id_tipo_cuenta:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Tipo_Cuenta.query.all()

    @staticmethod
    def get_by_id(id):
        return Tipo_Cuenta.query.get(id)

    @staticmethod
    def get_by_userName(nombre):
        return Tipo_Cuenta.query.filter_by(nombre=nombre).first()