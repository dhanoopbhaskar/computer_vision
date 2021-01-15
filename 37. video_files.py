import cv2
import time

capture = cv2.VideoCapture('mysupervideo.mp4')

if capture.isOpened() == False:
    print('ERROR: FILE NOT FOUND OR WRONG CODEC USED!')

while capture.isOpened():
    ret,frame = capture.read()
    if ret == True:
        # VideoWriter (in previous script) used 20fps
        time.sleep(1/20) # sleep added to slow down the video while displaying
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()