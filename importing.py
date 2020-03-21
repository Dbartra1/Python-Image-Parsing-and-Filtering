#!/usr/bin/env python3
#Importing libraries needed to read in an image
import cv2
import os
import sys 


def get_file():
    while True:
        image_path = input("Please Enter an image file path to begin: ")                #Request File path and provide paramters
        if image_path.casefold().endswith(('.png', '.jpg', '.jpeg')):                   #Ensuring image is one of three possible file extensions
            if os.path.exists(image_path):                                              #Ensuring filepath to image is valid
                break                                                                   #Break out of loop when successful
            else:
                print("\nInvalid Valid Filename or Extension. Try Again.")              #Catch 2 - Loop back to beginning
        else:
            print("\nFile or Directory not Found. Try Again.")                          #Catch 1 - Loop back to beginning
    return image_path

def conv_image(image_path):
    image = cv2.imread(image_path)                                                      #Reading image from verified file path
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)                                      #Converting image to RGB
    return image

def get_parseImage(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                     #Using the read in image apply gray scale
    while True:
        w, h = image.shape                                                              #Extracting two variables from a tuple
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

    cv2.imshow("Gray Image", image)                                                    #Display image to screen with window named Gray Scale
    cv2.waitKey(0)                                                                     #Once image is closed, wait till any key is pressed
    return image
