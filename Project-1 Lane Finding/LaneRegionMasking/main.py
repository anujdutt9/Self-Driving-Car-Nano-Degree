# Region Masking i.e. looking only at the region of interest in an image and neglecting the rest of the things
# In the current Input Image, the thing of interest is the Lane Lines.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from matplotlib import style
style.use('ggplot')


# Plot Image Values
def plot_image(title,image):
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.set_title(title)
    ax.set_axis_off()
    plt.show()


# Read in the Image and print some stats
img = image.imread('test.jpg')
print('This image is of type: {0} and Shape: {1}'.format(type(img),img.shape))
plot_image('Input Image',img)


# Get the "x" and "y" values of an image: Size of Image
x = img.shape[1]
y = img.shape[0]
print('\nx: {0}, y: {1}'.format(x,y))


# Save a copy of original image
img_copy = np.copy(img)
print('copy of image: ',img_copy)
plot_image('Copied Image',img_copy)


# Define a triangle region of interest
# The co-ordinates for an image start from "Upper Left Corner" of an image.
# i.e. at upper left corner of image, x=0, y=0
# Right Answers
bottom_left = [0, 539]
bottom_right = [900, 539]
apex = [475, 320]


# Fit lines (y = Ax + B) to identify the 3 sided region of interest. i.e. find best values of A and B given "x" and "y"
# Find the coefficients for the Best Fit Line using inputs "x" and "y".
fit_left = np.polyfit((bottom_left[0],apex[0]),(bottom_left[1],apex[1]),1)
fit_right = np.polyfit((bottom_right[0],apex[0]),(bottom_right[1],apex[1]),1)
fit_bottom = np.polyfit((bottom_left[0],bottom_right[0]),(bottom_left[1],bottom_right[1]),1)
print('\nfit_left: ',fit_left)
print('\nfit_right: ',fit_right)
print('\nfit_bottom: ',fit_bottom)


# Find region inside the triangle
# Make a Mesh Grid in the image
xx, yy = np.meshgrid(np.arange(0,x),np.arange(0,y))
print('xx: \n',xx)
print('yy: \n',yy)


# Defines the region inside the Triangle [Region of Interest] formed by the best fit lines
region_threshold = (yy > (xx*fit_left[0] + fit_left[1])) & \
                   (yy > (xx*fit_right[0] + fit_right[1])) & \
                   (yy < (xx*fit_bottom[0] + fit_bottom[1]))
print('\nRegion Thresholds: ',region_threshold)

# Color pixels red which are inside the region of interest
img_copy[region_threshold] = [255, 0, 0]

# Display the image with Region of Interest
plot_image('Image with Region Masking',img_copy)

# Display the Region of Interest without Mask
x = [bottom_left[0], bottom_right[0], apex[0], bottom_left[0]]
y = [bottom_left[1], bottom_right[1], apex[1], bottom_left[1]]
fig, ax = plt.subplots()
ax.plot(x, y, 'b--', lw=4)
ax.imshow(img)
ax.set_axis_off()
ax.set_title('Image with Region of Interest')
plt.show()

# ---------------------- EOC -----------------------