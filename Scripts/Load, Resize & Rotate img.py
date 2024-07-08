import cv2

#CV loads imgs in BGR (Blue, Green, Red)
img = cv2.imread('assets/playingbasketball.jpg', 1) #Make sure file type is correct

#-1, cv2.IMREAD_COLOR #Default, Loads a colour image. Any transparency of image will be neglected. 
#0, cv2.IMREAD_GRAYSCALE #loads image in grayscale
#1, cv2.IMREAD_UNCHANGED #Loads image, including alpha channel

#Resize img
#img = cv2.resize(img, (400,400))    #Resize to 400 by 400 pixels
img = cv2.resize(img, (0,0), fx=0.2,fy=0.2) #Load image to half its size (Good if don't know specific pixel size) 0.5 for half, 2 for double, etc.

#Rotate img
#img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

#Save an img
cv2.imwrite('new_Picture1.jpeg', img) #Able to change to differnt img types (png, jpg, etc.) not svg

cv2.imshow('Image', img)    #Display image
cv2.waitKey(0)  #Wait until a key is pressed (0 = wait an infinite amt of time, e.g. 5 = if no key is pressed in 5 secs, move on to destroy)
cv2.destroyAllWindows() #Closes ('Destroy') window