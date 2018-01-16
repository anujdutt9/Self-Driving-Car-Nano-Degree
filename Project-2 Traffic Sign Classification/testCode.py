import random
import pickle
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


# Step-1: Load the Dataset
training_file = './dataset/train.p'
testing_file = './dataset/test.p'

with open(training_file, mode='rb') as f:
    train = pickle.load(f)
with open(testing_file, mode='rb') as f:
    test = pickle.load(f)

X_train, y_train = train['features'], train['labels']
X_test, y_test = test['features'], test['labels']

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)


