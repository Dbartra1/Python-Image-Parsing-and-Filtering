#!/usr/bin/env python3
import importing as imp
import cv2
import numpy as np

def modifyImageSize(image_path):

    image = cv2.imread(image_path)                                                      #Reading image from verified file path

    while True:
            w, h, c = image.shape                                                              #Extracting two variables from a tuple
            while True:
                scale_percent = int(input("Enter a value between 1 and 200:  "))            #Percent of Original size / Dimensions
                try:
                    scaleAtPercent = int(scale_percent)                                     #Ensuring value is an integer
                    if scaleAtPercent <= 0: #ensuring value entered is > than 0
                        print("Invalid Input, Try again")
                        continue
                    elif scaleAtPercent > 200:
                        continue
                    else:
                        break
                except ValueError:                                                         #Catching non-integer values
                    print("Invalid Input, Try again")
            w = int(image.shape[1] * scale_percent / 100)                                  #Applying the width dimension
            h = int(image.shape[0] * scale_percent / 100)                                  #Applying the height dimension
            image = cv2.resize(image, (w, h), interpolation = cv2.INTER_AREA)              #Resising image based upon entered value size.
            print(w , "x" , h)                                                             #Printing in standard W X H format
            break
    return image

def modifyImageColor(image):
    w, h, c = image.shape

    red = int(input("Do you want red? enter 255 or 0 if no"))
    blue = int(input("Do you want blue? enter 255 or 0 if no"))
    green = int(input("Do you want green? enter 255 or 0 if no"))
    
    redImage =  np.full((w, h, c), (blue, green, red), np.uint8)                            #the scale size must be known. the color also has to change
    fusedImage = cv2.addWeighted(image, 1, redImage, .5, 0)
    

    cv2.imshow("default",  fusedImage)                                                    #Display image to screen with window named Gray Scale
    cv2.waitKey(0)
    cv2.destroyWindow("default")
    print(np.shape(image))
