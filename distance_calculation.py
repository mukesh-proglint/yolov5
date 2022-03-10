# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:47:04 2022

@author: PLAP033
"""

from imutils import paths
import numpy as np
import imutils
import cv2

def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)

	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)

image=cv2.imread(r"C:\Users\PLAP033\Pictures\Camera Roll\WIN_20220221_10_26_18_Pro.jpg")

print(find_marker(image))

cv2.waitKey(0)

cv2.destroyAllWindows()