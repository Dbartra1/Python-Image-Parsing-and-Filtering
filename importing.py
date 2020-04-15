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
