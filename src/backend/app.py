__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entity.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.Text)


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User')


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id', ondelete='CASCADE'))
    original_video_path = db.Column(db.String(255), unique=True)
    detected_video_path = db.Column(db.String(255), unique=True)

@app.before_first_request
def create_all():
    db.create_all(app=app)

@app.route('/')
def hello():
    return f'Hello, World!'


@app.route('/user/signup', methods=['GET', 'POST'])
def sign_up():
    data = request.get_json()
    email, password = data['email'], data['password']
    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id})

@app.route('/user/signin', methods=['POST'])
def sign_in():
    data = request.get_json()
    email, password = data['email'], data['password']
    entity = User.query.filter_by(email=email, password=password).first()

    if entity is not None:
        return jsonify({'code': 200, 'user_id': entity.id})
    else:
        return jsonify({'code': 400})

db.init_app(app)
app.run(host='0.0.0.0')