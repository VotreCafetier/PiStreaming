# import picamera
import numpy as np
import cv2

class SplitFrames(object):
    def __init__(self):
        self.frame_num = 0
        self.output = None

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # Start of new frame; close the old one (if any) and
            # open a new output
            if self.output:
                self.output.close()
            self.frame_num += 1
            self.output = io.open('image%02d.jpg' % self.frame_num, 'wb')
        self.output.write(buf)

class PiCameraStreaming(object):
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera_res = (320, 240)
        self.camera_framerate = 24
        # self.camera_brightness = camera_brightness
        # self.camera_exposuremode = camera_exposure_mode

    def __del__(self):
        self.camera.close()
        cv2.destroyAllWindows()

    def get_frame(self):
        self.camera.resolution = self.camera_res
        self.camera.framerate = self.camera_framerate
        image = np.empty((self.camera_res[1] * self.camera_res[0] * 3,), dtype=np.uint8)
        self.camera.capture(image, 'jpeg')
        print(image)
        return image.tobytes()

    def get_viframe(self):
        with picamera.PiCamera(resolution='720p', framerate=30) as camera:
            camera.start_preview()
            output = SplitFrames()
            camera.start_recording(output, format='mjpeg')
            camera.wait_recording(2)
            camera.stop_recording()
            return output.tobytes()


def get_picam(camera):
    while True:
        frame = camera.get_viframe()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')