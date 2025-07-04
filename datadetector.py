import keras
from keras import layers
from keras import ops
from keras.utils import load_img
from keras.utils import array_to_img
from keras.utils import img_to_array
from keras.preprocessing import image_dataset_from_directory
import tensorflow as tf  #  only for data preprocessing
import matplotlib.pyplot as plt
from keras.applications import VGG16, VGG19

conv_base_1 = VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3))

import os

os.environ["KERAS_BACKEND"] = "tensorflow"
import keras
from keras import ops
from keras import layers
import tensorflow as tf

import tensorflow_datasets as tfds

tfds.disable_progress_bar()

import matplotlib.pyplot as plt
import numpy as np

INP_SIZE = (300, 300)
TARGET_SIZE = (150, 150)
INTERPOLATION = "bilinear"

AUTO = tf.data.AUTOTUNE
BATCH_SIZE = 64
EPOCHS = 5

train_ds, validation_ds = tfds.load(
    "cats_vs_dogs",
    # Reserve 10% for validation
    split=["train[:40%]", "train[40%:50%]"],
    as_supervised=True,
)

def preprocess_dataset(image, label):
    image = ops.image.resize(image, (INP_SIZE[0], INP_SIZE[1]))
    label = ops.one_hot(label, num_classes=2)
    return (image, label)

train_ds = (
    train_ds.shuffle(BATCH_SIZE * 100)
    .map(preprocess_dataset, num_parallel_calls=AUTO)
    .batch(BATCH_SIZE)
    .prefetch(AUTO)
)

validation_ds = (
    validation_ds.map(preprocess_dataset, num_parallel_calls=AUTO)
    .batch(BATCH_SIZE)
    .prefetch(AUTO)
)

print(train_ds)
print(train_ds.shape)
print(train_ds[0])
print(train_ds[1])
print(validation_ds[0])
print(len(train_ds))
#train_ds[]
conv_base_1.predict(np.array(train_ds))
np.array(validation_ds)
feature_link = keras.models.Sequential()
feature_link.add(keras.layers.Dense(256, activation='relu', input_dim = 4 * 4 * 512))
feature_link.add(keras.layers.Dropout(0.5))
feature_link.add(keras.layers.Dense(1, activation='sigmoid'))
feature_link.compile(optimizer= keras.optimizers.RMSprop(lr=2e-5),
    loss='binary_crossentropy',
    metrics=['acc'])
#history = feature_link.fit(np.array(train_ds), ,
#    epochs=30,
#    batch_size=20)

exit()