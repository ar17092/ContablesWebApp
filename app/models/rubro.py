from app import db

class Rubro(db.Model):
    id_rubro = db.Column(db.Integer, primary_key=True)
    rubro = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f'<Rubro {self.rubro}>'

    def save(self):
        if not self.id_rubro:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Rubro.query.all()

    @staticmethod
    def get_by_id(id):
        return Rubro.query.get(id)