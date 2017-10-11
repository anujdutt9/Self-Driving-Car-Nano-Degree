# Canny Edge Detection in Images
# Used when we have lane lines of multiple color i.e. Yellow and White.
# In this case using Canny Edge Detection solves our purpose.

import cv2
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
plot_image('Input Image',img)


image = np.copy(img)

# Convert Color to Grayscale
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img,cmap='gray')
plt.axis('off')
plt.title('Color to Grayscale Image')
plt.show()


# Gaussian Blurring
# We'll also include Gaussian smoothing, before running Canny, which is essentially a way of suppressing noise and spurious gradients by averaging.
# cv2.Canny() actually applies Gaussian smoothing internally, but we include it here because you can get a different result by applying further smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray_img,(kernel_size,kernel_size),0)
plt.imshow(blur_gray,cmap='gray')
plt.axis('off')
plt.title('Image after Gaussian Blur')


# Canny Edge Detector
# In this case, you are applying Canny to the image gray and your output will be another image called edges.
# low_threshold and high_threshold are your thresholds for edge detection.
# The algorithm will first detect strong edge (strong gradient) pixels above the high_threshold, and reject pixels below the low_threshold.
# Next, pixels with values between the low_threshold and high_threshold will be included as long as they are connected to strong edges.
low_threshold = 50
high_threshold = 150
canny_img = cv2.Canny(blur_gray,low_threshold, high_threshold)
plt.imshow(canny_img,cmap='Greys_r')
plt.axis('off')
plt.title('Image with Canny Edge Detection')
plt.show()

# ---------------------- EOC --------------------------
