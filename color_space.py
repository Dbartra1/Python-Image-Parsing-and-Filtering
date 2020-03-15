#!/usr/bin/env python3

import cv2
import parsing


#make masks of all colors

#defining the range red
red_lower=np.array([136,87,111])
red_upper=np.array([180,255,255])
#defining the range blue
blue_lower=np.array([99,115,150])
blue_upper=np.array([110,255,255])
#defining the yellow range
yellow_lower=np.array([22,60,200])
yellow_upper=np.array([60,255,255])

