__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from app import app


@app.route('/device', methods=['POST', 'GET'])
def fetch_or_register_device_info():
    pass