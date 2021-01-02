from app import db

class Partida(db.Model):
    id_partida = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    nombre = db.Column(db.String(200), nullable=False)
    valor_debe = db.Column(db.Float)
    valor_haber = db.Column(db.Float)
    id_ldiario = db.Column(db.Integer, db.ForeignKey('libro__diario.id_libro_diario', ondelete='cascade'))
    pconceptos=db.relationship('Partida_Concepto', backref='partida_concepto', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Partida {self.nombre}>'

    def save(self):
        if not self.id_partida:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Partida.query.all()

    @staticmethod
    def get_by_id(id):
        return Partida.query.get(id)

    @staticmethod
    def get_by_nombre(nombre):
        return Partida.query.filter_by(nombre=nombre).first()

    @staticmethod
    def get_by_id_ldiario(id_ldiario):
        return Partida.query.filter_by(id_ldiario=id_ldiario)
    