from app import db

class Rubro(db.Model):
    id_rubro = db.Column(db.Integer, primary_key=True)
    rubro = db.Column(db.String(100), nullable = False)
    