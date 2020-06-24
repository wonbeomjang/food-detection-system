import cv2
import os
import picamera

def imgCap():
    if not os.path.exists('temp'):
        os.makedirs('temp')

    with picamera.PiCamera() as cam:
        cam.capture('temp/new.PNG')

    img = cv2.imread('temp/new.PNG', cv2.IMREAD_COLOR)

    content_type = 'image/PNG'
    headers = {'content-type': content_type}
    _, img_encoded = cv2.imencode('.PNG', img)

    return headers, img_encoded
