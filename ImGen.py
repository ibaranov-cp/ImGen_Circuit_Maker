#!/usr/bin/env python

#BSD 3-Clause License
#Copyright (c) 2017, Ilia Baranov

#############################################
# CHANGE THESE VARS AS NEEDED

size = 10 #size of squares in mils
invert = False #Color invert the image
image_name = "test.png" #name of the image, can be BMP, PNG or JPG

#############################################


from PIL import Image
import numpy as np
im = Image.open(image_name)
im.load()
im = im.convert('1')
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

print height, width

def format_csv(i,x,y):
	cv.write("\""+str(i)+"\",")
	cv.write("\""+str(x*size)+"\",")
	cv.write("\""+str((height - y - 1) *size)+"\",")
	cv.write("\"\"\n")

with open(image_name[:-3]+"csv", 'w') as cv:
	cv.write("\"Index\",\"X (mil)\",\"Y (mil)\",\"Arc Angle (Neg = CW)\"\n")
	cv.write("\"0\",\"0\",\"0\",\"\"\n")
	i = 1
 
	comp = 0
	if (invert): comp = 255
	for y in range (0,height):
		#print pixels[:][y] #For Debugging
		for x in range (0,width):
			if (pixels[y][x] == comp):
				format_csv(i,x,y)
				i+=1
				format_csv(i,x,y-1)
				i+=1
				format_csv(i,x+1,y-1)
				i+=1
				format_csv(i,x+1,y)
				i+=1
				format_csv(i,x,y)
				i+=1
				cv.write("\""+str(i)+"\",")
				cv.write("\"0\",\"0\",\"\"\n")
				i+=1
	