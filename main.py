import cv2
from gstreamer import *
from proc import *


camera = cv2.VideoCapture(0)
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
    frame = cv2.flip(frame, 180)
    invert = colors(frame)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
 
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
