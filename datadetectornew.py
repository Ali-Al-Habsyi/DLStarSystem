import matplotlib.pyplot as plt
import tensorflow as tf
#import tensorrt
import numpy as np
import time
from keras.applications import VGG16
import keras
import tensorflow_datasets as tfds

import pprint

# <> Continue after reading up on the matter <>
################################################################
# A scraper over tensorflow-prepared Dataset Collections #######
################################################################
collection_loaders = []
dataset_collector = []
for collection in tfds.list_dataset_collections():
    print(collection)
    dataset_collection = tfds.dataset_collection(collection)
    collection_loaders.append(dataset_collection)
    dataset_collection = dataset_collection.load_all_datasets() # free up disk-space, machine-upgrade would solve this
    datasets = dataset_collection.keys()
    for dataset in datasets:
        dataset_collector.append(dataset_collection[dataset])
       
# All scraped collected in dataset_collector
print(dataset_collector)

################################################################
# Temporarily more useful: data for vision processing (retrieved from TF's catalog)
# Collect and organize vision data and generate linknodes for system
# builders = tfds.list_dataset_collections()
#collection_loader2 = tfds.dataset_collection('xtreme')
#print("---------------------------------------------------------------")
#collection_loader1.print_datasets()
#print("---------------------------------------------------------------")
#collection_loader2.print_datasets()
#print("---------------------------------------------------------------")
#print(type(collection_loader1))
#xtreme_xnli
#xtreme_pawsx
# - xnli: DatasetReference(dataset_name='xtreme_xnli', namespace=None, config=None, version='1.1.0', data_dir=None, split_mapping=None, info_filenames=None)
# - pawsx: DatasetReference(dataset_name='xtreme_pawsx', namespace=None, config=None, version='1.0.0', data_dir=None, split_mapping=None, info_filenames=None)
#- pos: DatasetReference(dataset_name='xtreme_pos', namespace=None, config=None, version='1.0.0', data_dir=None, split_mapping=None, info_filenames=None)
#-# ner: DatasetReference(dataset_name='wikiann', namespace=None, config=None, version='1.0.0', data_dir=None, split_mapping=None, info_filenames=None)
#- xquad: DatasetReference(dataset_name='xquad', namespace=None, config=None, version='3.0.0', data_dir=None, split_mapping=None, info_filenames=None)
# - mlqa: DatasetReference(dataset_name='mlqa', namespace=None, config=None, version='1.0.0', data_dir=None, split_mapping=None, info_filenames=None)
# - tydiqa: DatasetReference(dataset_name='tydi_qa', namespace=None, config=None, version='3.0.0', data_dir=None, split_mapping=None, info_filenames=None)
# - bucc: DatasetReference(dataset_name='bucc', namespace=None, config=None, version='1.0.0', data_dir=None, split_mapping=None, info_filenames=None)
# - tatoeba: DatasetReference(dataset_name='tatoeba', namespace=None, config=None, version='1.0.0', data_dir=None, split_mapping=None, info_filenames=None)
#collection_loader =  tfds.dataset_collection('xtreme')
#all_datasets = collection_loader.load_all_datasets()
#splits = collection_loader.load_dataset("ner")
#print(splits)

tfds.load(
    "tf_flowers", split=["train[:85%]", "train[85%:]"], as_supervised=True
)
all_datasets = collection_loader.load_all_datasets()
pprint.pprint(all_datasets)

#splits = collection_loader.load_dataset("ner")
#tfds.dataset_collection('xtreme')
#builders
#all_datasets = collection_loader.load_all_datasets() 
#pprint.pprint(all_datasets)

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

images = np.array(images)
labels = np.array(labels)
#num_classes = NUM_CLASSES

NUM_CLASSES = np.max(labels) + 1

# fix this

labels = keras.utils.to_categorical(labels)
# Make sure images have shape (28, 28, 1)
#images = np.expand_dims(images, -1)
#print("images shape:", images.shape)
#print(labels.shape)

# Find compatible convolutional base for given vision source
conv_base_1 = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
features = conv_base_1.predict(images)

nodes_vision = []
nodes_labels = labels

#exit()
#print(features.shape)
#print(features[:, 0, :, :].shape)
#print(labels.shape)
#print(images.shape)

#exit()

# for each feature, one link, with result 8 data environments, i.e. 8 nodes, from one vision source.
# goal: NN feature -> label probability

#feature_link.add(keras.layers.Input(shape=(7 * 512)))
input_shape = features[0, 0, :, :].shape

##feature_link
#feature_link = keras.models.Sequential()
#keras.Input(shape=input_shape),
#feature_link.add(keras.layers.Dense(256, activation='relu', ))
#feature_link.add(keras.layers.Dropout(0.5))
##feature_link.add(keras.layers.Flatten())
#feature_link.add(keras.layers.Dense(NUM_CLASSES, activation='sigmoid'))
#feature_link.compile(optimizer= 'rmsprop',
#    loss='binary_crossentropy',
#    metrics=['acc'])
#feature_link.fit(features[:, 0, :, :], labels, batch_size = 30, epochs = 150)
#link_collection.append(feature_link)
#exit()

# for each feature, one link, with result 8 data environments, i.e. 8 nodes, from one vision source.
link_collection = []
detected_node_count = features.shape[1]
for index in range(detected_node_count):
 #   
 #   feature_link = keras.models.Sequential()
 #   feature_link.add(keras.layers.Input(shape=(224, 224, 3)))
 #   feature_link.add(keras.layers.Dense(256, activation='relu', ))
 #   feature_link.add(keras.layers.Dropout(0.5))
 #   feature_link.add(keras.layers.Dense(1, activation='sigmoid'))
 #   feature_link.compile(optimizer= 'rmsprop',
 #       loss='binary_crossentropy',
 #       metrics=['acc'])
 #   feature_link.fit(features[:, index, :, :], labels, batch_size = 30, epochs = 150)
 #   
    nodes_vision.append(features[:, index, :, :])
    feature_link = keras.models.Sequential()
    keras.Input(shape=input_shape),
    feature_link.add(keras.layers.Dense(256, activation='relu', ))
    feature_link.add(keras.layers.Dropout(0.5))
    feature_link.add(keras.layers.Flatten())
    feature_link.add(keras.layers.Dense(NUM_CLASSES, activation='sigmoid'))
    feature_link.compile(optimizer= 'rmsprop',
        loss='binary_crossentropy',
        metrics=['acc'])
    feature_link.fit(features[:, 0, :, :], labels, batch_size = 30, epochs = 10)
    link_collection.append(feature_link)
  
for link in link_collection:
    link.summary()
    

#print(feature_link)
#print(nodes_vision)
#print(nodes_labels)

# Next step: integrate into an existing DL StarSystem: add nodes to system and recomplete graph
# Data collection and graph expansion can occur along the above lines, an implementation of the smallest scale

# Result: 7 new data-environments from one vision source. 
# One datadetector results from generalization to automatic compatibility convolutional base for given vision source
# Construct compatible convolutional base from applied CNN

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

exit()