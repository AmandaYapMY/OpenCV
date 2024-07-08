import numpy as np
import cv2

#Capturing using webcam but video file is possiblt cv2.VideoCapture('Video file name')
cap = cv2.VideoCapture(0) #0 is one of the camers, 1 is 2 camers, 2 is 3 cameras, etc.

while True: #loop infinitely
    ret , frame = cap.read() #ret: if camera actually works, cap.read(): output Frame arrays
    
    #Get width & height of image
    width = int(cap.get(3)) #3 = width of img
    height = int(cap.get(4)) #4 = height of img

    #Drawing a line
    #cv2.line(variable, (starting point), (ending point), (BGR colour), thickness of line)
    img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10) #Starting & Ending coordinates of line on frame. (0,0) to (width,height) is from top left to bottom right
    img = cv2.line(img, (0,height), (width,0), (255,0,0), 10)   #Top right to bottom left

    #Drawing a rectangle cv2.rectangle(variable (top left), (bottom right), (colour), thickness)
    img = cv2.rectangle(img, (200,200), (400,400), (0,255,0), 5) #Negative number fills rectangle

    #Drawing a circle
    #cv2.circle(variable (centre), radius, (colour), thickness)
    img = cv2.circle(img, (300,300), 20, (0,0,255), -1)#Negative number fills shape

    #Drawing a text
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    #cv2.putText(variable, text, bottom left corner of text, font, font size, colour, thickness, line type)
    img = cv2.putText(img, 'Clown nose', (100,height - 10), font, 3, (0,0,255), 5, cv2.LINE_AA)

    #Display video
    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): #.waitkey(1) = 1fps. Else, if a key is pressed (e.g. q), ASCII of q is taken and if it matches in if condition, stop window
        break

cap.release()   #Release camera for other uses if needed
cv2.destroyAllWindows