__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from flask import Flask, request, jsonify, Response, render_template, url_for, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from capture_utils import capture
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entity.sqlite'
db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mh9716@kookmin.ac.kr'
app.config['MAIL_PASSWORD'] = '!_!'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


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
    # user = User(email="judepark@kookmin.ac.kr", password="weknownothing")
    # db.session.add(user)
    # db.session.commit()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/record')
def record():
    return render_template('record.html')

@app.route('/user/signin', methods=['POST'])
def sign_in():
    data = request.form
    email, password = data['email'], data['password']
    entity = User.query.filter_by(email=email, password=password).first()

    if entity is not None:
        return redirect(url_for('main'))
    else:
        # TODO: In honestly we need to add alert function.
        return jsonify({'code': 400})

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(
        capture(app, mail),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

db.init_app(app)
app.run(host='0.0.0.0')