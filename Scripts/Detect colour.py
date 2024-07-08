import numpy as np
import cv2

#Capturing using webcam but video file is possiblt cv2.VideoCapture('Video file name')
cap = cv2.VideoCapture(0) #0 is one of the camers, 1 is 2 camers, 2 is 3 cameras, etc.

while True: #loop infinitely
    ret , frame = cap.read() #ret: if camera actually works, cap.read(): output Frame arrays
    
    #Get width & height of image
    width = int(cap.get(3)) #3 = width of img
    height = int(cap.get(4)) #4 = height of img

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    #Convert frame BGR colour to HSV values
    #Colour we want to pick
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue) #Return a new image with only the lower & upper blues (or colours specified) existing

    #Apply mask to original image
    result = cv2.bitwise_and(frame, frame, mask=mask)   #Takes a src img and another image, then blend them tgt using mask

    #Display video
    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'): #.waitkey(1) = 1fps. Else, if a key is pressed (e.g. q), ASCII of q is taken and if it matches in if condition, stop window
        break

cap.release()   #Release camera for other uses if needed
cv2.destroyAllWindows