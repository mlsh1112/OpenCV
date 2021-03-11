import numpy as np
import cv2

def showvideo():
    try:
         pirnt('카메라를 구동합니다.')
         cap=cv2.VideoCapture('video.mov')
    except:
           print('카메라 구동 실패')
           return
    
    cap.set(3, 480) #frame 크기
    cap.set(4, 320)
    
    while True:
         ret, frame=cap.read()
         
         if not ret:
             print('비디오 읽기 오류')
             break
             
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video',gray)
        
    cap.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showvideo()
