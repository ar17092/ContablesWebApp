from app import db

class Cuenta(db.Model):
    id_cuenta = db.Column(db.INTEGER, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.String(200))
    id_tipocuenta = db.Column(db.INTEGER, db.ForeignKey('tipo_cuenta.id_tipo_cuenta', ondelete='set null'))

    def __repr__(self):
        return f'Cuenta {self.nombre}'

    def save(self):
        if not self.id_cuenta:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cuenta.query.all()

    @staticmethod
    def get_by_id(id):
        return Cuenta.query.get(id)

    @staticmethod
    def get_by_userName(nombre):
        return Cuenta.query.filter_by(nombre=nombre).first()