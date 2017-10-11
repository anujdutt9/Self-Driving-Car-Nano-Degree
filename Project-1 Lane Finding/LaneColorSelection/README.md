# Lane Color Selection
The first step in this course is to find the Lane Lines from a Video recorded from front camera mounted on a car. To do that, we first start off by recognizing the lane lines in the images and later on apply this knowledge to the video data that we recieve frame by frame.

***In this example, we start off by doing the color selection from the images i.e. selecting only the lane lines color (yellow/white) from the image and neglecting the rest of the things in the image.***

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


# Results

* **Input Image**

![Output a1](test.jpg?raw=true "Output a1")

* **Lane Color Selection**

![Output a1](Images/LaneData.png?raw=true "Output a1") 

