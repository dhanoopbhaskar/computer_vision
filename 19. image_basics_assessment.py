import cv2
import numpy as np

################
### FUNCTION ###
################

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,center=(x,y),radius=100,color=(0,0,255),thickness=10) #BGR

#################################
### SHOWING IMAGE WITH OPENCV ###
#################################

img = cv2.imread('dog_backpack.jpg')

cv2.namedWindow(winname='dog')
cv2.setMouseCallback('dog',draw_circle)

while True:
    cv2.imshow('dog',img)
    # if we've waited at least 20ms and we've pressed the ESC
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()