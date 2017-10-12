# Project-1 Lane Finding

***This repository contains the code for the first project in the Self Driving Cars Nanodegree which is Lane Finding.***

Lane finding is the very basic part of a self driving car as it has to maintain its path, keep a track of which lane it's driving in and also keep a track of what lane it can make a change into. So, before diving into the main project, we have some basic parts to learn for lane rcognition which are as follows:

|S.No.|            Name          |                      Description               |      Status     |
| --- | ------------------------ | ---------------------------------------------- | --------------- |
|  1. | Lane Color Selection     | Tells how to select only the lane lines and neglect the rest of the surroundings |  Completed |
|  2. | Lane Region Masking      | Further reducing the surroundings and masking the region in which the lane lines are present | Completed |
|  3. | Lane Color and Region Masking | Combining the Knowledge from first two projects and coloring the lane lines only |  Completed |
|  4. |   Canny Edge Detection   | How to use Canny Edge Detection to find lane lines using edges in Image. | Completed |
|  5. |     Hough Transform      | Using Image to Hough Transform to plot Lane Lines. | Completed |
|  6. | Hough Transform Filtered | Filtering the Image further to detect the Yellow & White Lane Lines | Completed |
|  7. | Project-1: Lane Finding  | Using the knowledge from above learnings for our First Project. | Completed | 

# Requirements

* Python 3.3+

* Matplotlib
```
pip3 install matplotlib --upgrade
```

* Numpy [+mkl for Windows]
```
pip3 install numpy --upgrade
```

* OS: Windows/Linux/Mac OS

***NOTE: If you have problem installing any of these packages, you can install these by downloading the windows pip wheel from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/).***
