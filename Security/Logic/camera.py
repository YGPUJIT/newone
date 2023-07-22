import numpy as np
from .ML.FaceRec import recognize_video
import cv2
import time


class Camera:
    def __init__(self):
        self.recoginze=None
        self.check=False

    
    def capture(self,data):
        self.recoginze=recognize_video.Recognize(data)
        _,black=cv2.imencode('.jpg',np.zeros((10,10),np.uint8))
        while True:
            if(self.check):
                frame=self.recoginze.capture_and_check()
                _,frame=cv2.imencode('.jpg',frame)
                yield(b'--frame\r\nContent-Type:image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')
            else:
                time.sleep(0.5)
                yield(b'--frame\r\nContent-Type:image/jpeg\r\n\r\n' + black.tobytes() + b'\r\n')
            

    def start(self):
        if(self.recoginze!=None):
            self.recoginze.start()
            self.check=True

    def stop(self):
        if(self.recoginze!=None):
            self.check=False
            self.recoginze.stop()

    def checkBoolean(self):
        return self.check

    def __del__(self):
        if(self.recoginze!=None):
            self.recoginze.stop()

    def details_offender(self):
        if(self.recoginze!=None):
            return self.recoginze.details_offender()
        else:
            return dict()

    
    def delete_details(self,pid):
        if(self.recoginze!=None):
            self.recoginze.delete_offender(pid)
        

