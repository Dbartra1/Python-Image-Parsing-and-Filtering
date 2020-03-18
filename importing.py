#!/usr/bin/env python3
#Importing libraries needed to read in an image
import cv2
import os
import sys 


def get_file():
    while True:
        image_path = input("Please Enter an image file path to begin: ")                #Request File path and provide paramters
        if image_path.casefold().endswith(('.png', '.jpg', '.jpeg')):                   #Ensuring image is one of three possible file extensions
            if os.path.exists(image_path):                                                #Ensuring filepath to image is valid
                break                                                                   #Break out of loop when successful
            else:
                print("\nInvalid Valid Filename or Extension. Try Again.")                #Catch 2 - Loop back to beginning
        else:
            print("\nFile or Directory not Found. Try Again.")                            #Catch 1 - Loop back to beginning
    return image_path

def conv_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)                                                         #display image
    return image


def get_parseImage(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    while True:
        w, h = image.shape
        choice = "y"
        while True:
            scale_percent = int(input("Enter a value between 1 and 200:  ")) # percent of original size
            try:
                scaleAtPercent = int(scale_percent) 
                if scaleAtPercent <= 0: #ensuring value entered is > than 0
                    print("Invalid Input, Try again")
                    continue
                elif scaleAtPercent > 200:
                    continue
                else:
                    break
            except ValueError: #Using try/except to catch errors
                print("Invalid Input, Try again")
        w = int(image.shape[1] * scale_percent / 100)
        h = int(image.shape[0] * scale_percent / 100)
        image = cv2.resize(image, (w, h), interpolation = cv2.INTER_AREA)
        print(w , "x" , h)
        break

    cv2.imshow("gray image", image)
    cv2.waitKey(0)
    return image
