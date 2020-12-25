from app import db

class Subcuenta(db.Model):
    id_subcuenta = db.Column(db.INTEGER, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.String(200))
    id_cuenta = db.Column(db.INTEGER, db.ForeignKey('cuenta.id_cuenta', ondelete='set null'))
    cuenta = db.relationship('Cuenta', backref='subcuenta', lazy=True)

    def __repr__(self):
        return f'Subcuenta {self.nombre}'

    def save(self):
        if not self.id_subcuenta:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Subcuenta.query.all()

    @staticmethod
    def get_by_id(id):
        return Subcuenta.query.get(id)

    @staticmethod
    def get_by_userName(nombre):
        return Subcuenta.query.filter_by(nombre=nombre).first()