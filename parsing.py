#!/usr/bin/env python3
import numpy as np
import cv2
import color_space

 #def parse_image():
image = importing.get_file()  #get the file from importing.
_, frame = image.read() #read the image

#resize to make make process faster so less pixels for program to solve
modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert colours to Hue Saturation Value

#As I don't yet know how to get the pointer to select a specific hue, the user will manually enter the color until later on in the project. Prototype 1
#Gets the upper bound of the desired colour(s)
#user_choice_upperbound_r = np.array([int(input("Put the higher red value here (1-255)")), int(input("Put the higher green value here (1-255)")), int(input("Put the higher blue value here (1-255)"))])
#Gets the lower bound of the desired colour(s)
#user_choice_lowerbound_r = np.array([int(input("Put the lower red value here (1-255)")), int(input("Put the lower green value here (1-255)")), int(input("Put the lower blue value here (1-255)"))])



#masks anything not the desired colour(s)
mask_r = cv2.inRange(hsv, red_lower, red_upper)
res_r = cv2.bitwise_and(frame, frame, mask_r = mask_r)
mask_b = cv2.inRange(hsv, blue_lower, blue_upper)
res_b = cv2.bitwise_and(frame, frame, mask_b = mask_b)
mask_y = cv2.inRange(hsv, yellow_lower, yellow_upper)
res_y = cv2.bitwise_and(frame, frame, mask_y = mask_y)
