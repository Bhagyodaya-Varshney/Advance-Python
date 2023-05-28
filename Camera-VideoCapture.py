import numpy as np
import cv2
# How to Load WebCam
cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    #Now I want Four Frames in My WebCam Screen
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    img = np.zeros(frame.shape,np.uint8)
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    img[:height//2,:width//2]= smaller_frame
    img[height//2:,:width//2]= smaller_frame
    img[:height//2,width//2:]= smaller_frame
    img[height//2:,width//2:]= smaller_frame
    cv2.imshow('Frame',img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()