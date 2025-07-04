#import numpy as np

#array = np.array([[-1,2,3],[1,2,3]])

import matplotlib.pyplot as plt
import tensorflow as tf
#import tensorrt
import numpy as np
import time
from keras.applications import VGG16
import keras
import tensorflow_datasets as tfds

train_ds, validation_ds = tfds.load(
    "tf_flowers", split=["train[:85%]", "train[85%:]"], as_supervised=True
)

IMAGE_SIZE = 224
NUM_IMAGES = 1000

images = []
labels = []

for (image, label) in train_ds.take(NUM_IMAGES):
    image = tf.image.resize(image, (IMAGE_SIZE, IMAGE_SIZE))
    images.append(image.numpy())
    labels.append(label.numpy())

#ret = relu(array)
#print(ret)