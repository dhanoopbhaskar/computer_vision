import cv2

capture = cv2.VideoCapture(0)

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Linux or MAC-OS --> *'XVID'
# Windows --> *'DIVX'
writer = cv2.VideoWriter('mysupervideo.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(width,height)) 

while True:
    ret,frame = capture.read()

    # OPERATIONS (DRAWING)
    writer.write(frame)
    
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()