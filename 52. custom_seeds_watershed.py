import cv2
import numpy as np
import matplotlib.pyplot as plt

road = cv2.imread('road_image.jpg')
road_copy = np.copy(road)

marker_image = np.zeros(road.shape[:2],dtype=np.int32)
segments = np.zeros(road.shape,dtype=np.uint8)

# COLOR MAPS
from matplotlib import cm

def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

colors = []
for i in range (10):
    colors.append(create_rgb(i))

###
# GLOBAL VARIABLES
# color choice
n_markers = 10 # 0-9
current_marker = 1
# markers updated by Watershed
marks_updated = False

# CALLBACK FUNCTION
def mouse_callback(event,x,y,flags,param):
    global marks_updated
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # markers passed on to the watershed algorithm
        cv2.circle(marker_image,(x,y),10,(current_marker),-1)
        # user sees on the road image
        cv2.circle(road_copy,(x,y),10,colors[current_marker],-1)
        
        marks_updated = True


cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image',mouse_callback)

while True:
    cv2.imshow('Watershed Segments',segments)
    cv2.imshow('Road Image',road_copy)
    
    # CLOSE ALL WINDOWS    
    k = cv2.waitKey(1)
    
    if k == 27:
        break
    # CLEARING ALL THE COLORS IF THE KEY 'c' IS PRESSED
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2],dtype=np.int32)
        segments = np.zeros(road.shape,dtype=np.uint8)
    # UPDATE COLOR CHOICE
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))    
    
    # UPDATE THE MARKINGS
    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road,marker_image_copy)
        
        segments = np.zeros(road.shape,dtype=np.uint8)
        
        for color_index in range(n_markers):
            # coloring the segments, numpy call
            segments[marker_image_copy==(color_index)] = colors[color_index]


cv2.destroyAllWindows()