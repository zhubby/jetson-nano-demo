import cv2
import numpy as np
camera = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM),width=640, height=480, format=NV12, framerate=30/1 ! nvvidconv flip-method=0 ! videoconvert ! video/x-raw, format=BGR ! appsink")

fourcc=cv2.VideoWriter_fourcc(*'MPEG')
videoOut = cv2.VideoWriter('recorder.mp4',fourcc, 30.0, (640,480))
isRead, frame=camera.read() 
while isRead :
    videoOut.write(frame)
    cv2.imshow('显示',frame)
    if cv2.waitKey(30) == 27:
        break
    isRead, frame = camera.read()

camera.release()
videoOut.release()
cv2.destroyAllWindows()