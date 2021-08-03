import picamera
import time

class PiCameraStreaming(object):
    def __init__(self, camera_res, camera_framerate, camera_brightness, camera_exposure_mode):
        self.camera = PiCamera()
        self.camera_res = camera_res
        self.camera_framerate = camera_framerate
        self.camera_brightness = camera_brightness
        self.camera_exposuremode = camera_exposure_mode

    def __del__(self):
        self.camera.close()

    def get_frame(self):
        with picamera.PiCamera() as camera:
            camera.start_preview()
            # Camera warm-up time
            time.sleep(2)
            return camera.capture(my_stream, 'jpeg')


def get_picam(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


