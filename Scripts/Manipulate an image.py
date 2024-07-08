import cv2
import random

img = cv2.imread('assets/Picture1.jpeg', -1)

#print(img.shape) #Shape tells no. of rows (height), columns (width), channels of img

#Print out array of first row of img
#print(img[0] [45:400]) #Change the 0 to change the row you want to see. To see more specific, use a slice (:)

#Changing pixel colours
#Look at first 100 rows (any no. will do tho)
#for i in range(100): #100 columns
#    for j in range(img.shape[1]): #1 is entire width of img
#        #Make the colours specified to another colour
#        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] #Need to have a lower and upper bound (0,255)

#Copy part of the image = Copy part of the array
tag = img[50:70, 60:90] #copy columns 600-900 in rows 500-700
#Paste copied array - Has to be the same dimensions as copied array
img[10:30, 50:80] = tag

#Show img
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()