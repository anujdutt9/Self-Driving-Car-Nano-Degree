## Advanced Lane Finding
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

***This repository contains the fourth project i.e. Advanced Lane Finding for Udacity SDCND.***

# Requirements

**1.** Python 3.5+

**2.** OpenCV

**3.** Matplotlib


# Usage

Just go through the iPython Notebook for complete details of the code and its working.

# Pipeline

**1. Camera Caliberation:**

The first step in this project was the Camera Caliberation. For doing this three steps were followed:

**a). Find Chessboard Corners**

The Chessboard images were used for camera caliberation. So the first step was to find the corners of the chessboard from the images.

**b). Draw Chessboard Corners**

Once the chessboard corners were found they were drawn onto to see that the corners re correctly recognized. From 20 images, 17 images were correctly identified for their corners. So, the overall Percentage of Caliberation Images used is 85.0 %.

![Chessboard Corners](output_images/ChessboardCorners.png?raw=true "Chessboard Corners")    

**c). Do Camera Caliberation**

To do this, the openCV function "cv2.calibrateCamera()" is used. This was tested on chessboard and road images.

![Undistorted Chessboard](output_images/UndistortedCheckboard.png?raw=true "Undistorted Chessboard")   

![Undistorted Road](output_images/download.png?raw=true "Undistorted Road") 

**2. Finding Region of Interest:**

The next step was to find the region of interest on the road. This is the region of the lanes in which the car is currently driving. We want to concentrate in this region only.

![Region of Interest](output_images/ROI.png?raw=true "Region of Interest") 

**3. Apply Color and Gradient Threshold:**

The next step is to explore the color and gradient thresholds so as to correctly and robustly identify the lane lines and their colors namely yellow and white in all conditions.

**a). RGB Colorspace:**

![RGB Colorspace](output_images/rgb.png?raw=true "RGB Colorspace") 

**b). HSV Colorspace:**

![HSV Colorspace](output_images/hsv.png?raw=true "HSV Colorspace") 

**c). HLS Colorspace:**

![HLS Colorspace](output_images/hls.png?raw=true "HLS Colorspace") 

**d). Lab Colorspace:**

![Lab Colorspace](output_images/Lab.png?raw=true "Lab Colorspace") 

A lot of options were tried in this pursuit and finally I was settled on using a thresholded combination of "R + G" from RGB Colorspace for Yellow lane detection, S-Colorspace from HSV and L-Colorspace from HLS colorspace for variations in lighting conditions.

**4. Gradient Thresholding Methods Tested:**

The three thresholding methods were teste for images namely Sobel Threshold, Sobel Gradient Magnitude and Sobel Gradient Direction.

![Sobel Gradient Threshold](output_images/SobelGradient.png?raw=true "Sobel Gradient Threshold")

![Sobel Gradient Magnitude](output_images/sobelMag.png?raw=true "Sobel Gradient Magnitude")

![Sobel Direction](output_images/sobelDirection.png?raw=true "Sobel Direction")


**5. Combine Color and Gradient Thresholds**

After testing the different combinations for the above thresholds and colorspaces, we combined the selected colorspaces and thresholds together to get the final image.

For the sobel thresholds, the Sobel Threshold and the Magnitude was thresholded and combined together with the colorspaces to get the final lane lines image as shown below.

![Threshold + Magnitude](output_images/threshMag.png?raw=true "Threshold + Magnitude")

**6. Image Warping**

Once, we got the image that depicted the lane lines petty clearly, it was time to get a new perspective. So, using the getPerspective function from OpenCV, I was able to get tht "Bird's Eye View" of the lanes.

![Warped Image](output_images/warpedImage.png?raw=true "Warped Image")

**7. Lane Finding using Histogram**

To get robust lane values, we used the histogram technique. We plotted the histogram for the warped lane line image and got the two peaks that correctly depict the lane lines and no other noise.

![Histogram](output_images/histogram.png?raw=true "Histogram")

**8. Using Sliding Window Method to Fit a Polynomial**

Once the lane lines were recognized robustly using the histogram for the warped image, we used the sliding window method to find the lane lines and draw a box around the lane lines and fit a line to the lane lines.

**9. Search for Lanes in the Margins and Visualize them**

Once we got the lane lines and the windows around them, we get the left and right lane values that we can use. So, next step is to look for lane lines in the margins computed and visualize them.

![Lane Lines](output_images/lanes.png?raw=true "Lane Lines")

**10. Measure Radius of Curvature**

Once we got the accurate measurements for the lane lines and drew them, then I computed the radius of curvature for the lane lines along with the curvature. This code is inspired by Udacity's lectures.

The Output for this looks like this:

```
Radius of curvature: 837.44 m
Center offset: 0.15 m
```

**11. Fill in the Lane Lines**

Once we got the lane lines recognized, we fill the lane lines in between to show the current lane as filled up.

![Filled Lane Lines](output_images/lanesFill.png?raw=true "Filled Lane Lines")

**12. Final Pipeline**

The Final Pipeline was a combination of all the functions and steps described above.

# Results

# Pipeline on Images

![Test Image 2](output_images/final2.png?raw=true "Test Image 2")

![Test Image 3](output_images/final3.png?raw=true "Test Image 3")

![Test Image 6](output_images/final6.png?raw=true "Test Image 6")


# Pipeline on Videos

**Project Video**

[![Project Video](https://img.youtube.com/vi/jldqNPbB524/0.jpg)](https://www.youtube.com/watch?v=jldqNPbB524)


**Challenge Video**

[![Challenge Video](https://img.youtube.com/vi/rrzXkqcglok/0.jpg)](https://www.youtube.com/watch?v=rrzXkqcglok)

**Harder Challenge Video**

[![Challenge Video](https://img.youtube.com/vi/Eqcj78Y4cbs/0.jpg)](https://www.youtube.com/watch?v=Eqcj78Y4cbs)

**NOTE: The current pipeline failed on this video. Still working on the current Piepline to get this video right.**

# Potential Shortcomings of Current Pipeline

The following are the shortcoming of the current pipeline:

**1.** This pipeline is not able to work well when the image or video have a shadow. As can be seen in the challenge video, at one point when it get a bit of shadow for a very small amount of time, it behave wieredly but the comes back to the track. This behavior is also noticed in the Harder Challenge Video output as well.

**2.** This piepline has a hard time looking for the lane lines when the brightness is pretty high or the cameras get a high brightness image as input due to the Sun. To avoid this and reduce the effect of this, I tried using Histogram Normalization and also tried playinng with the Gamma values of the Image. But unfortunately, that didn't worked out that well as expected.

**3.** In the harder video, the pipeline has a hard time recognizing the lane lines. One issue with the pipeline is that it looks for a bit longer section of the lane. This works pretty well for the project and the challenge videos but proves out to be a complete disaster for the Harder Challenge Video.

# Possible Improvements

**1.** One aproach that might help useful can be the dynamica selection of threshold parameters based on the resulting number of activated pixels rather than hard coding them. 

**2.** I can try to average over a small number of frames and using those to get the next predictions for the lane lines. How this might help is where we have lanes that are very curvy like the ones in the mountains.

**3.** The other approach would prove useful even for the car when it is driving on a plain road and hence the performance will not be affected in the plains.

# References

**1.** Udacity Lectures

**2.** OpenCV Documentation & Examples
