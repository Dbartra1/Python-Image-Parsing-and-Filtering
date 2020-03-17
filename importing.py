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
                print("Invalid Valid Filename or Extension. Try Again.")                #Catch 2 - Loop back to beginning
        else:
            print("File or Directory not Found. Try Again.")                            #Catch 1 - Loop back to beginning
    return image_path

def conv_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print("here")                                                          #display image
    return image

def get_parseImage(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray image", gray_image)

    print("Here")

#temporary

def main():
    get_file()
    image_path = get_file()
    conv_image(image_path)
    image = conv_image(image_path)
    get_parseImage(image)

if __name__ == "__main__":
    main()
