import numpy as np
import cv2, os, time
from PIL import Image


class FaceID(object):
    @staticmethod
    def identify(path_to_templates,accuracy):
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        user_img_lst = [cv2.imread(path_to_templates + '/' + img_name) for img_name in os.listdir(path_to_templates)]
        gray_img_lst = [cv2.cvtColor(user_img, cv2.COLOR_BGR2GRAY) for user_img in user_img_lst]
        while True:
            ret, frame = cam.read() # Capture frame-by-frame
            cv2.imshow('frame', frame) # Display the resulting frame
            cv2.imwrite('last_img.png', frame) # open the template
            template = cv2.imread('last_img.png', 0)
            # match the template using cv2.matchTemplate
            correlation_lst = [cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED) for gray_img in gray_img_lst]
            print(max(correlation_lst))
            if cv2.waitKey(1) & 0xFF == ord('q') or max(correlation_lst)>=accuracy:
                break
        cam.release()
        cv2.destroyAllWindows()

    @staticmethod
    def create_person(save_folder, num_photo):
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        counter = 0
        index = 0
        pause_between_img = 10
        while True:
            # Capture frame-by-frame
            ret, frame = camera.read()
            # Our operations on the frame come here
            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or index == num_photo:
                break
            if counter == pause_between_img:
                counter = 0
                cv2.imwrite(save_folder + 'cam' + str(index) + '.png', frame)
                index += 1
            counter += 1

        camera.release()
        cv2.destroyAllWindows()


#FaceID.identify('users/username9',0.8)
