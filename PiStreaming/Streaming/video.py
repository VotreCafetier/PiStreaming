import cv2

class livefeed:
    def init(self,camera):
        self.camera = cv2.VideoCapture(self.camera)

    def update(self):
        if not self.camera.isOpened():
            print("Cannot open camera")
            exit()
        # Capture frame-by-frame
        ret, frame = self.camera.read()
        return frame

    def stop(self):
        self.camera.release()
        cv2.destroyAllWindows()