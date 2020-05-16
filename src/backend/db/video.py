__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from app import db


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_video_path = db.Column(db.String(255), unique=True)
    detected_video_path = db.Column(db.String(255), unique=True)
