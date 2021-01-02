from app import db

class Partida_Concepto(db.Model):
    __tablename__='partida_concepto'

    id_pconcepto = db.Column(db.Integer, primary_key=True)
    valor_parcial=db.Column(db.Float)
    id_cuenta = db.Column(db.Integer, db.ForeignKey('cuenta.id_cuenta', ondelete='set null'))
    id_partida = db.Column(db.Integer, db.ForeignKey('partida.id_partida', ondelete='set null'))
    cargo_abono = db.Column(db.BOOLEAN, default=False) #True =debe; False =haber
    cuenta = db.relationship('Cuenta', backref='cuenta', lazy=True)

    def __repr__(self):
        return f'Partida_Concepto {self.id_pconcepto}'

    def save(self):
        if not self.id_pconcepto:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Partida_Concepto.query.all()

    @staticmethod
    def get_by_id(id):
        return Partida_Concepto.query.get(id)

    @staticmethod
    def get_by_idpartida(id_partida):
        return Partida_Concepto.query.filter_by(id_partida=id_partida).first()
