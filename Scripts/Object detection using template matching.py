import numpy as np
import cv2

#load in as greyscale
img = cv2.imread('assets/playingbasketball.jpg', 0)
img = cv2.resize(img, (0,0), fx=0.18,fy=0.18) #Reduced size as it was too big to see the full picture and identify the rectangle on basketball
template = cv2.imread('assets/shoe.png', 0)

h, w = template.shape   #Greyscale images aren't 3D, don't have channels

#Methods to do template matching
#Try using all the methods and pick the best one that worked
methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

#Perform every single method in methods array for template matching
for method in methods:
    img2 = img.copy()   #Draw the rectangle around the same object from the template on original image

    result = cv2.matchTemplate(img2, template, method)  #'Slides' template around base img and identify how close a match is
    #print(result)  #(W - w + 1, H - h + 1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  #Return min, max value of array & min, max location in array
    print(min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc  #Methods:TM_CCOEFF_NORMED, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED,

    #Draw rectangle at location in array
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 3)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()