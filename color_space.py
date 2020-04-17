#!/usr/bin/env python3
import importing as imp
import cv2
import numpy as np

def modifyImageSize(image_path):

    image = cv2.imread(image_path)                                                          #Reading image from verified file path

    while True:
            w, h, c = image.shape                                                           #Extracting two variables from a tuple
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
    #Initializing variables 
    w, h, c = image.shape
    inputs = []

    while True:
        try:
            #Retrieve user input 
            blue = int(input("Filter perctange of Blue (0 to 255): "))
            green = int(input("Filter perctange of Green (0 to 255): "))
            red = int(input("Filter perctange of Red (0 to 255): "))
            opacityPercent = float(input("Enter percentage of opacity (.001 to 1.0): "))

            #Ensure user input is valid before it is put into the list for records
            if blue >= 0 and green >= 0 and red >= 0 and opacityPercent >= .001 and blue <= 255 and green <= 255 and red <= 255 and opacityPercent <= 1.0:

                #Change Integer values into String values & append to master list
                sBlue = str(blue)
                sPrefixBlue = "Blue = "
                bCombined = sPrefixBlue + sBlue
                inputs.append(bCombined)

                sGreen = str(green)
                gPrefixGreen = "Green = "
                gCombined = gPrefixGreen + sGreen
                inputs.append(gCombined)

                sRed = str(red)
                sPrefixRed = "Red = "
                rCombined = sPrefixRed + sRed
                inputs.append(rCombined)

                sOpacity = str(opacityPercent)
                sPrefixOpacity = "Opacity = "
                oCombined = sPrefixOpacity + sOpacity
                inputs.append(oCombined)  
                break

            else:
                print("Invalid Input, Try again\n")
                continue

        except ValueError:
            print("Invalid Input, Try again\n") 

    #Creating filtered image through user assigned variables.
    filteredImage =  np.full((w, h, c), (blue, green, red), np.uint8)                            
    finalImage = cv2.addWeighted(image, 1, filteredImage, opacityPercent, 0)
    
    #Naming window variables.
    origImageWinName = "Original Image (Resized)"
    filteredImageWinName = "Filtered Image"
    comparisonImageWinName = "Comparison"
    
    #Numpy's concatenate combines two images - will be used for side by side comparison.
    sideBySide = np.concatenate((finalImage, image), axis = 1)

    #Use of a loop to determine how to present the filtered image.
    while True:
        choice = input("\nHow would you like to view your filtered image?"  + 
                       " (compared to original (1) or by itself (2): ")
        if choice == "1":
            cv2.imshow(comparisonImageWinName, sideBySide)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
        elif choice == "2":
            cv2.imshow(filteredImageWinName,  finalImage)                                                       
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
        else:
            print("Invalid Input, Try again\n")
            continue
        

    return inputs
