import cv2

## callback function to draw rectangle
def draw_rectangle(event,x,y,flags,param):
    global pt1,pt2,topLeft_clicked,bottomRight_clicked    
    if event == cv2.EVENT_LBUTTONDOWN:
        # reset the rectangle (checks if the rectangle is there)
        if topLeft_clicked and bottomRight_clicked:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            bottomRight_clicked = False
        
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
        elif bottomRight_clicked == False:
            pt2 = (x,y)
            bottomRight_clicked = True


## global variables
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
bottomRight_clicked = False

## connect to the callback
capture = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)


while True:
    ret,frame = capture.read()
    
    # drawing based on the global variables
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=3,color=(0,0,255),thickness=-1)
    
    if topLeft_clicked and bottomRight_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)
    
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


capture.release()
cv2.destroyAllWindows()