__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


from mss import mss
from PIL import Image

import numpy as np
import io
import cv2

# TODO => 비디오 화면에 맞춰서 수정할 것.
mon = {'top': 160, 'left': 160, 'width': 100, 'height': 100}


def capture():
    while True:
        with mss() as sct:
            sct.get_pixels(mon)
            img = Image.frombuffer('RGB', (sct.width, sct.height), sct.image)

            np_img = np.array(img)
            encode_return_code, image_buffer = cv2.imencode('.jpg', np_img)
            io_buf = io.BytesIO(image_buffer)
            yield (b'--frame\r\n'
                   b'Content-Type: image/png\r\n\r\n' + io_buf.read() + b'\r\n')