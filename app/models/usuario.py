from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app import db


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(25), unique=True,nullable=False)
    password = db.Column(db.String(128),nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id_empresa', ondelete='set null'))
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
            return f'<User {self.username}>'

    #Encriptamos la password
    def set_password(self, password):
        self.password = generate_password_hash(password)

    #Función para comparar la password almacenada en la  db contra la ingresada por el usuario 
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_userName(username):
        return User.query.filter_by(username=username).first()