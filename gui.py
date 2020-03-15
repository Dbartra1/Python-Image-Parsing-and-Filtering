#!/usr/bin/env python3

# importing libraries 
import cv2
import numby
import tkinter
import color_space

windowName ="Open CV Color Palette"

# window name 
cv2.namedWindow(windowName)  
       
# Used to open the window 
cv2.imshow(windowName, image) 

button_red = tkk.Button(frame, text="Red", command=click_red)
button_blue = tkk.Button(frame, text="Blue", command=click_blue)
button_green = tkk.Button(frame, text="Green", command=click_yellow)

def click_red():
    cv2.imshow(res_r)

def click_blue():
    cv2.imshow(res_b)

def click_yellow():
    cv2.imshow(res_y)
