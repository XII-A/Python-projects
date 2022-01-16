import cv2 as cv
import numpy as np

#reading vids

face_cascade = cv.CascadeClassifier("Facereog/Cascades/data/haarcascade_frontalface_alt2.xml")#cascade is basiclly an algorithem to recog face that was built via machone learning and this one requires the image to be gray


capture = cv.VideoCapture(0)

while True:
    fl = False
    isTrue,frame = capture.read() #the func capture.read returns a frame and a boolean wether the frame was succefully read or not
    

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) #we turn the farme to gray here cuz thats what the cascade needs

    faces = face_cascade.detectMultiScale(gray , scaleFactor=1.5, minNeighbors=5) #here we detect the face
    
    for(x,y,w,h) in faces: #here we give the cords of where the face is
        print(x,y,w,h)
        roi_gray = gray[y:y+h,x:x+w] #our region of interst its basiclly where our face is exactly on the gray frame
        roi_color = frame[y:y+h,x:x+w]
        # img_item = 'my-image.png'                                                                                            #my asumption on how this works is we proplly only iterate once inside the for loop where once we get the x y w h we print them make the rect then go to imshow
        # cv.imwrite(img_item,roi_color)
        color = (255,0,0)
        stroke = 2
        end_cordx = x+w
        end_cordy = y+h
        cv.rectangle(frame,(x,y),(end_cordx,end_cordy),color,stroke) #we draw the rectangle via this

    
    cv.imshow("Video",frame) #we show the video via this frame by frame 
    fl = True
    if fl:
        print(type(faces))
    if cv.waitKey(20) & 0xFF==ord('d'): #to stop the vid from playing forever --> this means if the letter d is pressed close the vid
        break                           #this if condation has a bitwise operation where once the hexdecm num is equal to d we do an and operation on it and tbh idk how is it considered true

capture.release() #we release the capture pointer
cv.destroyAllWindows() #we detroy all windows


