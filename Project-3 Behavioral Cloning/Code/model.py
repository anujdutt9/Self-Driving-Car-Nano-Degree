# Import Dependencies
from data_preprocessing import *
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
from keras.layers import Flatten, Dense, Lambda, Convolution2D, Cropping2D, Dropout


# ------------------------------------ Load Images and Get Steering Angles -------------------------------------
images, measurements = getImagesAndMeasurements(data_path='./data/driving_log.csv', image_path='./data/IMG/', correction_val=0.2)

# getImagesAndMeasurements Function Analysis
print("Total Number of Images (before Augmentation): ",len(images))
print("Total Number of Steering Angles (before Augmentation): ",len(measurements))

print("Sample Center Camera Images: \n",images[0:8036:1000])
print("\nSample Left Camera Images: \n",images[8036:16072:1000])
print("\nSample Right Camera Images: \n",images[16070::1000])

print("\nSample Center Camera Angles: \n",measurements[:8036:1000])
print("\nSample Left Camera Angles: \n",measurements[8036:16072:1000])
print("\nSample Right Camera Angles: \n",measurements[16072::1000])



# ------------------------------- Train Test Split and Batch Data Generation -------------------------------
# Features: Images
X = images

# labels: Measurements [Steering Angles]
y = measurements

# Combine the Features and Labels in a list
data_samples = list(zip(X, y))

# Train_Test_Split
Xy_train, Xy_validation = train_test_split(data_samples, test_size=0.2, random_state=0)

print("Number of Samples in Training Data: ",len(Xy_train))
print("Number of Samples in Validation Data: ",len(Xy_validation))


model_training_generator = batch_data_generator(Xy_train, batch_size=32)
model_validation_generator = batch_data_generator(Xy_validation, batch_size=32)


# ------------------------------------------ CNN Model ----------------------------------------------
# Model Ref: NVIDIA []
def cnnModel():
    model = Sequential()
    model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160, 320, 3)))
    # model.add(Lambda(lambda x: (x / 127.5) - 1., input_shape=(160, 320, 3)))
    #model.add(Cropping2D(cropping=((60, 20), (0, 0))))
    model.add(Cropping2D(cropping=((50, 20), (0, 0))))
    model.add(Convolution2D(24, (5, 5), subsample=(2, 2), activation='relu'))
    model.add(Convolution2D(36, (5, 5), subsample=(2, 2), activation='relu'))
    model.add(Convolution2D(48, (5, 5), subsample=(2, 2), activation='relu'))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    #model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(100))
    model.add(Dense(50))
    model.add(Dense(10))
    model.add(Dense(1))
    model.summary()
    return model



if __name__ == '__main__':
    # Train the Model
    model = cnnModel()

    try:
        checkpoint = ModelCheckpoint('./saved_models/model-{epoch:03d}.h5', monitor='val_loss', verbose=0, save_best_only=True,mode='auto')
    except:
        checkpoint = ModelCheckpoint('/home/anuj_dutt_ml/SDCND/Behavioral-Cloning/BehavioralCloning/saved_models/model-{epoch:03d}.h5', monitor='val_loss', verbose=0, save_best_only=True,mode='auto')

    model.compile(loss='mse', optimizer='adam')
    history_object = model.fit_generator(model_training_generator, samples_per_epoch=len(Xy_train),
                                     validation_data=model_validation_generator, nb_val_samples=len(Xy_validation),
                                     nb_epoch=3, verbose=1)
    #model.save('model.h5')
    try:
        model.save('./saved_models/model.h5')
    except:
        model.save('/home/anuj_dutt_ml/SDCND/Behavioral-Cloning/BehavioralCloning/saved_models/model.h5')