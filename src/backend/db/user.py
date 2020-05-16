__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.Text)

