import cv2

capture = cv2.VideoCapture(0)

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# top-left corner
x = width // 2 # // to get integer result
y = height // 2

# width and height of the rectangle
w = width // 4
h = height // 4

# bottom-right corner x+w, y+h

while True:
    ret,frame = capture.read()
    cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=4)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
cv2.destroyAllWindows()