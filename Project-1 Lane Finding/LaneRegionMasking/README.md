# Lane Region Masking
This is the second step in the Lane Finding project. In this, we take the same input image as in the Lane Color Selection project and select a region of Interest in the image. That region of interest can be defined in form of a rectangle, square, triangle etc. 

Note that we want our region of interest to cover only the parts of the image in which we see our lane in which the car is currently present and nothing more than that.

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

* **Lane Region Masked Image**

![Output a1](RegionMasking.png?raw=true "Output a1") 

* **Marking Region of Interest**

![Output a1](RegionOfInterest.png?raw=true "Output a1") 

The last iamge might look like that the dotted lines should be on the white lane lines but that's not the case. This is because when we apply color masking on the image in the next step, we should be able to see only the white lane lines. This is possible when we take the white lane lines without the region masking it completely. This will be more clear when we'll do the color masking for the lane lines in the next step.
