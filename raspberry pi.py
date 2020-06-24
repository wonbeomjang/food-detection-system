import requests
from imgCap import imgCap
from config.config import get_config
from time import sleep
import os
import cv2
import numpy as np
from time import time

config = get_config()

id = {}
check = ""
URL = 'http://192.168.118.1:5000/'
id[config.user_id_name] = '223322'
detect_URL = URL + 'detect/' + id[config.user_id_name]
login_URL = URL + "login"
command_URL = URL + 'check_command'
ras_URL = URL + 'detect_ras'

# wire raspberry pi on server
response = requests.post(login_URL, json=id)
_time = 0


def cap_img(URL):
    start_time = time()
    # Transmit image
    headers, img_encoded = imgCap()
    response = requests.post(URL, data=img_encoded.tostring(), headers=headers)
    nparr = np.fromstring(response.content, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print('[*] send %s image to %s' % ("new.PNG", URL))
    print('    duration : %f' % (time() - start_time))
    return img_np
#    open(os.path.join('temp', 'google.PNG'), 'wb').write(response.content)


while True:
    _time = _time + 1
    # check command of raspberry pi
    check = requests.post(command_URL, json=id)
    if str(check.text) == id[config.user_id_name]:
        cap_img(detect_URL)

    if _time % (5 * 100) == 0:
        cap_img(detect_URL)

    print(_time)
    img = cap_img(ras_URL)
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
