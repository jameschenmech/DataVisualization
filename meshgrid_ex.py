# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:09:28 2018

@author: James
"""
#I have somethings to say about you my friend
#you are guaranteed to succeed
#regardless of what happens you have to believe
#this course is the best course

import os
print(os.getcwd) 
#wdir='C:/Users/James/Documents/Python Data Science/Data Visualization')

import matplotlib.pyplot as plt

import numpy as np

u = np.linspace(-2,2,3)

v = np.linspace(-1,1,5)

X,Y = np.meshgrid(u,v)

Z = X**2/25 + Y**2/4*1

print('Z:\n', Z)

plt.figure()
plt.set_cmap('gray')
plt.pcolor(X, Y, Z)
plt.colorbar()
plt.show()


import pandas as pd

df  = pd.read_csv('auto-mpg.csv')

plt.figure()
plt.hist2d(df.hp, df.mpg, bins=(20, 20), range=((40,235),(8,48)))
plt.colorbar()
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot)')
plt.show()

plt.figure()
plt.hexbin(df.hp, df.mpg, gridsize=(25, 12), extent=(40,235,8,48))
plt.colorbar()
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot)')
plt.show()

plt.figure()
img = plt.imread('Astronaut-EVA.jpg')
print(img.shape)
plt.imshow(img)
plt.axis('off')
plt.show()


#compute the sume of the red, green, blue channels
intensity = img.sum(axis=2)
print(intensity.shape)

plt.figure()
plt.imshow(intensity, cmap='gray')
plt.colorbar()
plt.axis('off')
plt.show()


plt.figure()
# Specify the extent and aspect ratio of the top left subplot
plt.subplot(2,2,1)
plt.title('extent=(-1,1,-1,1),\naspect=0.5') 
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=0.5)

# Specify the extent and aspect ratio of the top right subplot
plt.subplot(2,2,2)
plt.title('extent=(-1,1,-1,1),\naspect=1')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=1.0)

# Specify the extent and aspect ratio of the bottom left subplot
plt.subplot(2,2,3)
plt.title('extent=(-1,1,-1,1),\naspect=2')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=2.0)

# Specify the extent and aspect ratio of the bottom right subplot
plt.subplot(2,2,4)
plt.title('extent=(-2,2,-1,1),\naspect=2')
plt.xticks([-2,-1,0,1,2])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-2,2,-1,1), aspect=2)

# Improve spacing and display the figure
plt.tight_layout()
plt.show()


#rescaling pixel intensity
# Load the image into an array: image
image = plt.imread('800px-Unequalized_Hawkes_Bay_NZ.jpg')

# Extract minimum and maximum values from the image: pmin, pmax
pmin, pmax = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))

# Rescale the pixels: rescaled_image
rescaled_image = 256*(image-pmin)/(pmax-pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." % 
      (rescaled_image.min(), rescaled_image.max()))

# Display the original image in the top subplot
plt.figure()
plt.subplot(2,1,1)
plt.title('original image')
plt.axis('off')
plt.imshow(image)

# Display the rescaled image in the bottom subplot
plt.subplot(2,1,2)
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image)

plt.show()
