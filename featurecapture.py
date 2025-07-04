###############################################################
#
# DATA-ENVIRONMENT DETECTION: AUTOMATIC GRAPH EXPANSION
#
#
#
###############################################################

# Goal: Collect data from surroundings, similar to how a windmill generates energy from the winds
# First tool: Convolution
# Each channel in last CNN layer connect with CNN target and give data-environment, 3 channels, 3 Nodes
# At least one detector needed, consider CNN corner case: one source -> 512 features

import matplotlib.pyplot as plt
from keras.applications import VGG16, VGG19
import keras

conv_base1 = VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))
#conv_base2 = VGG19(weights='imagenet', input_shape=(32, 32, 3))
#(images_train, class_train), (images_train, class_test) = keras.datasets.mnist.load_data()

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar100.load_data()
print(x_train[0].shape)
exit()
#print(len(x_train))
#print()
#exit()
# Search for compatible conv base
features_train = conv_base2.predict(x_train)
#  feature per source detected...

#for i in range(len(features_train)):
#    print(len(features_train.shape)
print(features_train[0].shape)
exit()


batch_size = 20
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator

#base_dir = '/Users/fchollet/Downloads/cats_and_dogs_small'
#train_dir = os.path.join(base_dir, 'train')
#validation_dir = os.path.join(base_dir, 'validation')
#test_dir = os.path.join(base_dir, 'test')
datagen = ImageDataGenerator(rescale=1./255)

def extract_features2(directory, sample_count):
    features = np.zeros(shape=(sample_count, 4, 4, 512))
    labels = np.zeros(shape=(sample_count))
    generator = datagen.flow_from_directory(
        directory,
        target_size=(150, 150),
        batch_size= batch_size,
        class_mode='binary')
    i=0
    for inputs_batch, labels_batch in generator:
        features_batch = conv_base.predict(inputs_batch)
        features[i * batch_size : (i + 1) * batch_size] = features_batch
        labels[i * batch_size : (i + 1) * batch_size] = labels_batch
        i += 1
    #if i * batch_size >= sample_count:
        #break
    return features, labels

def VGG16detect_features():
    features = np.zeros(shape=(len(x_train), 4, 4, 512))
    labels = np.zeros(shape=len(x_train))
    features_batch = conv_base.predict(x_train)
    return features_batch, labels
    
#generator = 
#for inputs_batch, labels_batch in generator:
#    features_batch = 
#    features[i * batch_size : (i + 1) * batch_size] = features_batch
#    labels[i * batch_size : (i + 1) * batch_size] = labels_batch
#    i += 1
#if i * batch_size >= sample_count:
#    break
#return features, labels 
    
#train_features, train_labels = extract_features(train_dir, 2000)
#validation_features, validation_labels = extract_features(validation_dir, 1000)
#test_features, test_labels = extract_features(test_dir, 1000)

feature_link = keras.models.Sequential()
feature_link.add(keras.layers.Dense(256, activation='relu', input_dim = 1 * 1 * 512))
feature_link.add(keras.layers.Dropout(0.5))
feature_link.add(keras.layers.Dense(1, activation='sigmoid'))
feature_link.compile(optimizer= keras.optimizers.RMSprop(lr=2e-5),
    loss='binary_crossentropy',
    metrics=['acc'])
history = feature_link.fit(features_train, class_train,
    epochs=30,
    batch_size=20)


exit()







#validation_data=(validation_features, validation_labels))
acc = history.history['acc']
#val_acc = history.history['val_acc']
loss = history.history['loss']
#val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
#plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
#plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()