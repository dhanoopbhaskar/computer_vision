import cv2
import numpy as np

################
### FUNCTION ###
################

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,center=(x,y),radius=100,color=(0,255,0),thickness=-1)        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,center=(x,y),radius=100,color=(255,0,0),thickness=-1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

#################################
### SHOWING IMAGE WITH OPENCV ###
#################################

img = np.zeros((512,512,3),np.int8)

while True:
    cv2.imshow('my_drawing',img)
    # if we've waited at least 20ms and we've pressed the ESC
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()