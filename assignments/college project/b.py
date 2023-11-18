# system libraries
import os
import warnings

# ignoring all the warnings
warnings.simplefilter('ignore')

# import data handling libraries
import numpy as np
import pandas as pd

# importing data visualisation libraries
import matplotlib.pyplot as plt


# import image processing library
from skimage.io import imread, imshow
from skimage.transform import resize

#------------------------------------------------------------------------------------------------------------#

r = os.listdir(r"C:\Users\HP\Desktop\do not open\assignments\college project\Bag Classes\r")
# This is the path to the image folder

v = os.listdir(r"C:\Users\HP\Desktop\do not open\assignments\college project\Bag Classes\v")
d = os.listdir(r"C:\Users\HP\Desktop\do not open\assignments\college project\Bag Classes\d")

print(r[0:10])

#------------r--------------------------------------------------------------------------------------------------#

limit = 1500
# Creating the list of blank spaces that can potentially hold data:
ra_images = [None]*limit

# Creating loop variables:
i, j = 0, 0

# This part of the code loops over all the images
# in the list "r" and reads it into the jth element
# of the array we made in line 2.
for i in r:
	if(j<limit):
		ra_images[j] = imread(r"C:\Users\HP\Desktop\do not open\assignments\college project\Bag Classes\r\\" + i)
		j+= 1
	else:
		break
	
# Similarly, we will fill up the data into the other 2 arrays
va_images = [None]*limit

#-----------------------------------------------------------------------------------------------------------------------------------#

limit =1500
# Creating the list of blank spaces that can potentially hold data:
ra_images = [None]*limit

# Creating loop variables:
i, j = 0, 0

# This part of the code loops over all the images
# in the list "r" and reads it into the jth element
# of the array we made in line 2.
for i in v:
	if(j<limit):
		ra_images[j] = imread(r"C:\Users\HP\Desktop\do not open\assignments\college project\Bag Classes\v\\" + i)
		j+= 1
	else:
		break
	
#--------------------------------------------------------------------------------------------------------------------------


limit = 1500
# Creating the list of blank spaces that can potentially hold data:
ra_images = [None]*limit

# Creating loop variables:
i, j = 0, 0

# This part of the code loops over all the images
# in the list "r" and reads it into the jth element
# of the array we made in line 2.
for i in d:
	if(j<limit):
		ra_images[j] = imread(r"C:\Users\HP\Desktop\do not open\assignments\college project\Bag Classes\d\\" + i)
		j+= 1
	else:
		break
	

    # Finding out the number of columns per image in our dataset.
# We will use the shape function on any one image in our array
# and use the dimensions we get as the number of columns in row.
number_of_columns = ra_grey[1].shape[0] * ra_grey[1].shape[1]
print(number_of_columns)

# This means we will be using this many columns
# per row in our dataset.
# Our dataset has 300 images, so:
# Our dataset will be an array of dimensions
# 784 x 300 => 300 images of 784 pixels each.
