from tkinter.constants import TRUE
import cv2 as cv
from keyboard import*
import numpy as np
import datetime
import time
import screen_brightness_control as sbc




def face_detection():
    
    t_end = time.time() + 60 * 1 #this takes the current time and adds 1 min on it
    
    capture = cv.VideoCapture(0)
    
    face_cascade = cv.CascadeClassifier("Cascades\data\haarcascade_frontalface_alt2.xml")

    while time.time() < t_end:

        isTrue,frame = capture.read()

        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray , scaleFactor=1.5, minNeighbors=5)

        if not isinstance(faces,tuple):
            capture.release() 
            return True


def brightness_control(f_d):
    x = datetime.datetime.now()
    if f_d == True:
        if x.hour >= 20:
            sbc.fade_brightness(65)
        else:
            sbc.fade_brightness(100)
    else:
        sbc.fade_brightness(25)

            

def command_A():
    while True:
        b_f_d = face_detection()
        brightness_control(b_f_d)
        time.sleep(25)


if __name__ == '__main__':
    print("program starting")
    command_A()
