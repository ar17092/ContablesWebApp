from app import db

class Libro_Diario(db.Model):
    id_libro_diario= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200),nullable=False, unique=True)
    descripcion = db.Column(db.String(200))
    id_user= db.Column(db.INTEGER, db.ForeignKey('user.id', ondelete='set null'))

    def __repr__(self):
        return f'Libro_Diario {self.nombre}'

    def save(self):
        if not self.id_libro_diario:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Libro_Diario.query.all()

    @staticmethod
    def get_by_id(id):
        return Libro_Diario.query.get(id)

    @staticmethod
    def get_by_nombre(nombre):
        return Libro_Diario.query.filter_by(nombre=nombre).first()
