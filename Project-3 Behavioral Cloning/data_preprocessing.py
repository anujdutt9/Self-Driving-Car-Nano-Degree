# Import Dependencies
import csv
import cv2
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('Agg')
#get_ipython().magic('matplotlib inline')



'''
    Step - 1: Load the Dataset.
    Aim: Load the driving_log.csv file containing the center, left, right image paths,
    steering angles and speed at each time instance.
'''
def read_data(data_path, skip_header=False):
    lines = []
    with open(data_path) as csvfile:
        reader = csv.reader(csvfile)
        if skip_header:
            next(reader, None)
        for line in reader:
            lines.append(line)
    return lines


# Check that the above function reads the data correctly
data = read_data(data_path='./data/driving_log.csv', skip_header=True)

# If data is loaded successfully, continue else give the User an Error
if data:
    pass
else:
    print("Error Loading Dataset !!!")



''' 
    Step - 2: Load and Separate all the Images and the Steering Angle Measurements.
    Step - 3: Apply Correction to Left and Right Image Steering Angle Values
    
    Aim: Add correction to left steering angles to get to center & subtract correction from right steering angles
    to get to center.
    
    Paths:
    data_path: './data/driving_log.csv'
    image_path: './data/IMG/'
'''
def getImagesAndMeasurements(data_path, image_path, correction_val):
    # Arrays to hold the Images and Steering Measurements
    # Here, we will keep all images i.e. Center, Left & Right in the same array: images_total
    images_total = []

    center_images_path = []
    left_images_path = []
    right_images_path = []

    steeringAngle = []
    steeringAngle_total = []

    # Fetch all the Lines from the above function
    lines = read_data(data_path, skip_header=True)

    for line in lines:
        for i in range(3):

            # Select Center, Left & Right Images
            if i == 0:
                source_path = line[0]
                filename = source_path.split('/')[-1]
                current_path = image_path + filename
                center_images_path.append(current_path)
                # image = cv2.imread(current_path)
                # center_images.append(image)

            elif i == 1:
                source_path = line[1]
                filename = source_path.split('/')[-1]
                current_path = image_path + filename
                left_images_path.append(current_path)
                # image = cv2.imread(current_path)
                # left_images.append(image)

            elif i == 2:
                source_path = line[2]
                filename = source_path.split('/')[-1]
                current_path = image_path + filename
                right_images_path.append(current_path)
                # image = cv2.imread(current_path)
                # right_images.append(image)

        # Get the Steering Measurements
        measurement = float(line[3])
        steeringAngle.append(measurement)

    # Add All Image Paths in Order: Center, Left, Right to One Array
    images_total.extend(center_images_path)
    images_total.extend(left_images_path)
    images_total.extend(right_images_path)

    # Add All Steering Angles in Order: Center, Left, Right to One Array
    steeringAngle_total.extend(steeringAngle)
    # Left Steering Angle with Correction
    steeringAngle_total.extend([m + correction_val for m in steeringAngle])
    # Right Steering Angle with Correction
    steeringAngle_total.extend([m - correction_val for m in steeringAngle])

    return (images_total, steeringAngle_total)



'''
    Step - 4: Data Augmentation
    
    The data that we have is less in size. So, to increase the size of the dataset, we augment the data.
    
    Data Augmentation Steps:
    1. Flip the Image: LEFT <-> RIGHT
    2. Flip the Measurements for the corresponding images using product with -1.0
    3. Add Random Brightness in the image.
    4. Add the Augmented Images to the Original Image set in the Generator Function.
'''
# Add random brightness to Images
# Hint Taken From: https://stackoverflow.com/questions/32609098/how-to-fast-change-image-brightness-with-python-opencv
def random_brightness(image):
    # Convert image from RGB to HSV
    rgbTohsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    # random brightness ratio
    brightness_ratio = 1.0 + 0.4 * (np.random.rand() - 0.5)
    # change brightness to random values using 3rd channel of HSV image
    rgbTohsv[:,:,2] = rgbTohsv[:,:,2] * brightness_ratio
    # return the RGB image
    return cv2.cvtColor(rgbTohsv, cv2.COLOR_HSV2RGB)


# Function to Augment Data
def augment_data(input_image, steering_angle):
    # Flip Images
    aug_image = cv2.flip(input_image, 1)
    aug_measurements = steering_angle * -1.0
    # Random Brightness
    aug_image = random_brightness(aug_image)
    return aug_image, aug_measurements



'''
    Step - 5: Batch Data Generator
    
    This function takes in the input data i.e. (Xy_train) => (X,y) and batch size i.e. number of samples used by the model
    at a time. In this function, we shuffle the input data so that the model does not recognizes the patterns in the data
    and then we apply augmentation i.e. flip the images LEFT <-> RIGHT and add Random Brightness.
    Then, we add these images to the existing pool of images. 
    
'''
# Batch Data Generator
def batch_data_generator(input_data, batch_size):
    # Get the number of Input Data Samples (X,y)
    num_samples = len(input_data)

    while 1:
        # Shuffle the Data Samples so that the Model does not recignize a Pattern
        shuffled_data = shuffle(input_data)

        for samples in range(0, num_samples, batch_size):
            batch_samples = shuffled_data[samples:samples + batch_size]

            # Arrays to Store Features & Labels
            images = []
            steeringAngles = []

            for image, measurement in batch_samples:
                img = cv2.imread(image)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                images.append(img)
                steeringAngles.append(measurement)

                # Augmented Images
                # aug_image , aug_measurements = augment_data(input_image=image, steering_angle=measurement)
                # aug_image = cv2.flip(img, 1)
                # aug_measurement = measurement * -1.0
                # aug_image = random_brightness(aug_image)
                aug_image, aug_measurements = augment_data(img,measurement)
                images.append(aug_image)
                steeringAngles.append(aug_measurements)

            # Features
            X = np.array(images)

            # Labels
            y = np.array(steeringAngles)

            yield shuffle(X, y)




'''
    Helper Functions: Function to Plot Images, Training Output etc.
'''
# Function to Plot Images
def plot_image(input_image):
    plt.imshow(input_image)
    plt.show()


# Function to plot Model Metrics
# Reference: https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
def plot_model_metrics(hist_obj):
    plt.plot(hist_obj.history['loss'])
    plt.plot(hist_obj.history['val_loss'])
    plt.title('Behavioral Cloning')
    plt.ylabel('Loss: Mean Squared Error')
    plt.xlabel('Epochs')
    plt.legend(['Training Curve', 'Validation Curve'], loc='upper right')
    #plt.show()
    try:
        plt.savefig('output.png')
    except:
        plt.savefig('/home/anuj_dutt_ml/SDCND/Behavioral-Cloning/BehavioralCloning/output.png')

# ---------------------------------------------- END ----------------------------------------------------
