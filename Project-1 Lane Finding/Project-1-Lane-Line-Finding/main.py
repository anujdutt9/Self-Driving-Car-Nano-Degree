# Project-1: Finding Lane Lines in Images and Videos

# Import Dependencies
import os
from sys import argv
import time
import cv2
import glob
import numpy as np
from utils import *
from moviepy.editor import VideoFileClip
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib import style
style.use('ggplot')



# Create Directory for Output Images and Videos
imageOutDir = './OutputImages/'
videoOutDir = './OutputVideos/'

if not os.path.exists(imageOutDir):
    os.makedirs(imageOutDir)

if not os.path.exists(videoOutDir):
    os.makedirs(videoOutDir)


# Process Image function for Videos
def process_image(image):
    # NOTE: The output you return should be a color image (3 channel) for processing video below
    # TODO: put your pipeline here,
    # you should return the final output (image with lines are drawn on lanes)
    result = LaneLinesPipeline(image,name=None,arg='videos')
    return result



# Check all Files in the Directory
print('List of all Test Images in Folder',os.listdir('test_images/'))



# Build the Pipeline
# 1. Read in the Image
# 2. Convert to Grayscale
# 3. Apply Gaussian Blur
# 4. Use Canny Edge to find Edges
# 5. Find Polynomial Region of Interest (ROI) and select Lane Lines.
# 6. Apply Hough Transform and Filter it for Lane Lines
# 7. Plot the Lane Lines on Actual Image

# Pipeline to draw Lane Lines
def LaneLinesPipeline(img,name=None,arg=None):

    start = time.time()

    x = img.shape[1]
    y = img.shape[0]
    # print('\nThe image is of type: {0} and shape: {1}'.format(type(read_image),read_image.shape))

    # Step-2: Convert to Grayscale
    gray_image = grayscale(img)

    # Step-3: Apply Gaussian Blur
    kernel_size = 5
    gaussian_image = gaussian_blur(gray_image,kernel_size)

    # Step-4: Apply Canny Edge Detection
    low_threshold = 50
    high_threshold = 150
    canny_edge = cannyEdge(gaussian_image,low_threshold,high_threshold)
    canny_edge = cv2.bitwise_or(canny_edge, yellow_mask(img))

    # Step-5: Find Polynomial Region of Interest (ROI) and select Lane Lines.
    border = 0
    imshape = img.shape
    # Here, "x" and "y" are the dimensions of the Input Image
    vertices = np.array([[(int(0.11*x), y), (int(0.44*x),int(0.6*y)), (int(0.56*x),int(0.6*y)), (int(0.95*x),y)]], dtype=np.int32)
    image_roi = region_of_interest(canny_edge, vertices)

    # Step-6: Apply Hough Transform and Filter Image
    rho = 1
    theta = np.pi / 180
    threshold = 15
    min_line_len = 60
    max_line_gap = 30
    hough_transformed_image = hough_lines(image_roi, rho, theta, threshold, min_line_len, max_line_gap)

    # Step-7: Plot Lane Lines on Actual Image
    filtered_image = weighted_img(hough_transformed_image,img,α=0.6, β=1., λ=0.)
    end = time.time()

    print('Time Taken for whole Process is {} ms'.format((end - start) * 100))

    if arg == 'images':
        arr = [['Greyscale & Gaussian Blurring','Edge Detection'],
               ['Region of Interest', 'Hough Transform']]

        arr1 = [[gaussian_image,canny_edge],
                [image_roi, hough_transformed_image]]

        # Plot the Final Output with Outputs of Process Followed
        fig,ax = plt.subplots(nrows=2,ncols=2)

        for i in range(0,2):
            for j in range(0,2):
                ax[i,j].imshow(arr1[i][j],cmap='gray')
                ax[i,j].set_axis_off()
                ax[i,j].set_title(arr[i][j])
                ax[i,j].set_aspect('equal')

        figName = imageOutDir+name+'_Process.jpg'
        fig.savefig(figName)

        fig1,ax1 = plt.subplots()
        ax1.imshow(filtered_image)
        ax1.set_axis_off()
        ax1.set_title('Final Image')
        path = imageOutDir+name+'_Final.jpg'
        fig1.savefig(path)

        plt.show()

    return filtered_image




# Main Function
if __name__ == '__main__':
    if argv[1] == 'images':
        for image in glob.glob('test_images/*.jpg'):
            img = imread(image)
            name = os.path.splitext(image)[0][12:]
            LaneLinesPipeline(img,name,arg='images')

    elif argv[1] == 'videos':
        # Process White Lane Lines Video
        print('Processing Video: solidWhiteRight.mp4')
        whiteLanesOut = 'OutputVideos/solidWhiteRightOut.mp4'
        clip1 = VideoFileClip('test_videos/solidWhiteRight.mp4')
        whiteLanesOutClip = clip1.fl_image(process_image)
        whiteLanesOutClip.write_videofile(whiteLanesOut, audio=False)

        # Process Yellow Lane Lines Video
        print('\nProcessing Video: solidYellowLeft.mp4')
        yellowLanes_output = 'OutputVideos/solidYellowLeftOut.mp4'
        clip2 = VideoFileClip('test_videos/solidYellowLeft.mp4')
        yellowLanes_clip = clip2.fl_image(process_image)
        yellowLanes_clip.write_videofile(yellowLanes_output, audio=False)

    elif argv[1] == 'help':
        print('1. To Process Images, Use:  python main.py images')
        print('2. To Process Videos, Use:  python main.py videos')

    else:
        print('\nPlease Enter Correct Argument !!!')
        print('\nUse:\npython main.py help \nfor help ')

# --------------------------- EOC ---------------------------