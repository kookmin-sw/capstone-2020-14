__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from app import app


@app.route('/user/signup', methods=['POST'])
def sign_up():
    pass


@app.route('/user/signin', methods=['POST'])
def sign_in():
    pass