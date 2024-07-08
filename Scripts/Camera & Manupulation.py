import numpy as np
import cv2

#Capturing using webcam but video file is possiblt cv2.VideoCapture('Video file name')
cap = cv2.VideoCapture(0) #0 is one of the camers, 1 is 2 camers, 2 is 3 cameras, etc.

while True: #loop infinitely
    ret , frame = cap.read() #ret: if camera actually works, cap.read(): output Frame arrays
    
    #Get width & height of image
    width = int(cap.get(3)) #3 = width of img
    height = int(cap.get(4)) #4 = height of img

    #Mirror videos multiple times
    image = np.zeros(frame.shape, np.uint8)  #Create empty numpy array to put frame array inside numpy array

    #Shrink frame
    smaller_frame = cv2.resize(frame,(0,0), fx = 0.5, fy = 0.5) #Half original size

    #Copy & paste x times
    #Has to be 180 as height & width when rotated 90 doesn't match as height becomes longer & width becomes shorter aka cannot fit into image frame
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)    #Top left, rotate 180
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)    #Bottom left, rotate 180
    image[:height//2, width//2:] = smaller_frame    #Top right
    image[height//2:, width//2:] = smaller_frame    #Bottom right

    #Display video
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): #.waitkey(1) = 1fps. Else, if a key is pressed (e.g. q), ASCII of q is taken and if it matches in if condition, stop window
        break

cap.release()   #Release camera for other uses if needed
cv2.destroyAllWindows