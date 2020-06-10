from flask import Flask
from flask_mail import Mail, Message
from matplotlib import pyplot as plt




app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mh9716@kookmin.ac.kr'
app.config['MAIL_PASSWORD'] = '!_!'
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)

with app.app_context():
    msg = Message('Hello', sender = 'mh9716@kookmin.ac.kr', recipients = ['park.jude.96@gmail.com'])
    msg.body = "This is the email body"
    plt.plot([1,2,3], [110,130,120])
    plt.savefig('test.png')
    
    with app.open_resource("test.png") as fp:
        msg.attach("test.png", "image/png", fp.read())
 
    mail.send(msg)


