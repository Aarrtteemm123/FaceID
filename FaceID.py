import numpy as np
import cv2,time
from PIL import Image

class FaceID(object):
    @staticmethod
    def identify(path_to_templates):
        pass

    @staticmethod
    def create_person(save_folder,num_photo):
        camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        counter = 0
        index = 0
        pause_between_img = 10
        while True:
            # Capture frame-by-frame
            ret, frame = camera.read()
            # Our operations on the frame come here
            gray = cv2.cvtColor(cv2.UMat(frame), cv2.COLOR_BGR2GRAY)
            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q') or index == num_photo:
                break
            if counter==pause_between_img:
                counter = 0
                cv2.imwrite(save_folder+'cam'+str(index)+'.png', frame)
                index+=1
            counter+=1

        camera.release()
        cv2.destroyAllWindows()

