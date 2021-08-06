import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:

class PiCameraStreaming(object):
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera_res = (320, 240)
        self.camera_framerate = 24
        # self.camera_brightness = camera_brightness
        # self.camera_exposuremode = camera_exposure_mode

    def __del__(self):
        self.camera.close()
        self.video.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        camera.resolution = self.camera_res
        camera.framerate = self.camera_framerate
        image = np.empty((self.camera_res[0] * self.camera_res[1] * 3,), dtype=np.uint8)
        camera.capture(image, 'bgr')
        image = image.reshape((self.camera_res[0], self.camera_res[1], 3))
        ret,jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()


def get_picam(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


