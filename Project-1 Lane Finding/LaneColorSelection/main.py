# Code to Retain as much of Lane Data as Possible in Image

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib import style
style.use('ggplot')


# Plot Image Values
def plot_image(title,image):
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.set_title(title)
    ax.set_axis_off()
    plt.show()


# Read in the Image
img = imread('test.jpg')
print('This image is of type: {0} and Shape: {1}'.format(type(img),img.shape))
plot_image('Input Image',img)

# Get the X and Y Values of the image
x = img.shape[1]
y = img.shape[0]
print('\nx: {0}, y: {1}'.format(x,y))

# Make a Copy of Original Image Values
img_copy = np.copy(img)
print('copy of image: ',img_copy)
plot_image('Copied Image',img_copy)

# Define RGB Threshold Values
red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold,green_threshold,blue_threshold]

# Set all Values less than the Threshold Value to "0"
# If values less than threshold exist, a "True" appears else "False".
thresholds = (img[:,:,0] < rgb_threshold[0]) \
            | (img[:,:,1] < rgb_threshold[1]) \
            | (img[:,:,2] < rgb_threshold[2])
print('Thresholds: ',thresholds)

# Select these threshold values and apply to original image
img_copy[thresholds] = [0,0,0]
plot_image('Image with Maximum Amount of Lane Data Retained',img_copy)

# ---------------------- EOC ----------------------------