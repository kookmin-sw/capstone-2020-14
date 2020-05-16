__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

@app.before_first_request
def create_all():
    db.create_all(app=app)

@app.route('/')
def hello():
    return f'Hello, World!'


db.init_app(app)
app.run()