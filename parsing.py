#!/usr/bin/env python3
import numpy as np
import cv2

 #def parse_image():
image = importing.get_file()  #get the file from importing.
_, frame = image.read() #read the image
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert colours to Hue Saturation Value

 
#As I don't yet know how to get the pointer to select a specific hue, the user will manually enter the color until later on in the project. Prototype 1
#Gets the upper bound of the desired colour(s)
user_choice_upperbound = np.array([int(input("Put the higher red value here (1-255)")), int(input("Put the higher green value here (1-255)")), int(input("Put the higher blue value here (1-255)"))])
#Gets the lower bound of the desired colour(s)
user_choice_lowerbound = np.array([int(input("Put the lower red value here (1-255)")), int(input("Put the lower green value here (1-255)")), int(input("Put the lower blue value here (1-255)"))])

 

#masks anything not the desired colour(s)
mask = cv2.inRange(hsv, user_choice_lowerbound, user_choice_upperbound)
res = cv2.bitwise_and(frame, frame, mask = mask)