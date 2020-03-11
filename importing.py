#!/usr/bin/env python3
#Importing libraries needed to read in an image
import cv2
import os
import sys 

#def get_file():
while True:
    filepath = input("Please Enter an image file path to begin: ")                  #Request File path and provide paramters
    if filepath.casefold().endswith(('.png', '.jpg', '.jpeg')):                     #Ensuring image is one of three possible file extensions
        if os.path.exists(filepath):                                                #Ensuring filepath to image is valid
            image = cv2.imread(filepath)                                            #Read image
            cv2.imshow("image",image)                                               #display image
            cv2.waitKey(0)                                                          #Wait for user to input any value to quit.
            break                                                                   #Break out of loop when successful
        else:
            print("Invalid Valid Filename or Extension. Try Again.")                #Catch 2 - Loop back to beginning
    else:
        print("File or Directory not Found. Try Again.")                            #Catch 1 - Loop back to beginning