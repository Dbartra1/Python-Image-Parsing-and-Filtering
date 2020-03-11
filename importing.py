#!/usr/bin/env python3
#Importing libraries needed to read in an image
import cv2


#def get_file():
value = input("Please Enter a Image File to Begin: ")      #Request File path and provide paramters 
image = cv2.imread(value)                                                   #Read image
cv2.imshow("image",image)                                                   #display image
cv2.waitKey(0)                                                              #Wait for user to input any value to quit.