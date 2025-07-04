import keras
import pandas as pd
from zipfile import ZipFile
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

link_D1_tangent_layer1_batch = []
link_D2_tangent_layer1_batch = []
link_D1_bias_layer1_batch = []
link_D2_bias_layer1_batch = []

(train_data_1, train_labels_1), (test_data_1, test_labels_1) = keras.datasets.boston_housing.load_data()

for i in range(10):
    link_D1_tangent_layer1_batch.append(np.eye(100))
    link_D2_tangent_layer1_batch.append(np.eye(100))
    link_D1_bias_layer1_batch.append(np.eye(100))
    link_D2_bias_layer1_batch.append(np.eye(100))
   
link_D1_tangent_layer1_batch = np.array(link_D1_tangent_layer1_batch)
link_D2_tangent_layer1_batch = np.array(link_D2_tangent_layer1_batch)
link_D1_bias_layer1_batch = np.array(link_D1_bias_layer1_batch)
link_D2_bias_layer1_batch = np.array(link_D2_bias_layer1_batch)
# print(link_D1_tangent_layer1_batch[0].shape)

#print("--------------------------------------------------------------------------------------------------------------------------------------------")
#print(np.array(link_D1_tangent_layer1_batch))
#print("--------------------------------------------------------------------------------------------------------------------------------------------")
#print(np.array(link_D2_tangent_layer1_batch))
#p#rint("--------------------------------------------------------------------------------------------------------------------------------------------")
#print(np.array(link_D1_bias_layer1_batch))
#print("--------------------------------------------------------------------------------------------------------------------------------------------")
#print(np.array(link_D2_bias_layer1_batch))
#print("--------------------------------------------------------------------------------------------------------------------------------------------")

#print(type(train_data_1))
#print(len(train_data_1))
#print(len(train_labels_1))
#exit()



# TASK ATTACH ZEROES TO SMALL MATRIX FOR BIGGER MATRIX WITH ZEROES
print(link_D1_tangent_layer1_batch.shape)
print(link_D2_tangent_layer1_batch.shape)

A = np.ones((6, 100, 100))
B = np.ones((6, 10, 100))
amplified_batch_array = np.concatenate((B, np.ones((6, 90, 100))), axis=1)
print(amplified_batch_array.shape)

exit()
#input_size = link_D1_tangent_layer1_batch[0].shape
##output_size = link_D2_tangent_layer1_batch[0].shape
#link_D1 = keras.models.Sequential()
#link_D1.add(keras.layers.Dense(64, activation='relu'))
#link_D1.add(keras.layers.Dense(64, activation='relu'))
#link_D1.add(keras.layers.Dense(1))
#link_D1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
#link_D1.fit(train_data_1, train_labels_1, epochs=5, batch_size=128)

###### Either this was functional ###################################################### 1/2

#input_size = link_D1_tangent_layer1_batch[0].shape
#output_size = link_D2_tangent_layer1_batch[0].shape

#link_D2D1_tangent1 = keras.models.Sequential()
#link_D2D1_tangent1.add(keras.Input(shape=input_size))  
#link_D2D1_tangent1.add(keras.layers.Dense(output_size[0] * output_size[1]))
#link_D2D1_tangent1.add(keras.layers.Dense(output_size[0] * output_size[1]))
#link_D2D1_tangent1.add(keras.layers.Dense(output_size[0]))
#link_D2D1_tangent1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
##link_D2D1_tangent1.summary()
#inference1 = link_D2D1_tangent1.predict(np.eye(input_size[100]))
#print(inference1.shape)
## Fix Wednesday: easy fix
#link_D1_tangent_layer1_batch = np.array(link_D1_tangent_layer1_batch)
#link_D2_tangent_layer1_batch = np.array(link_D2_tangent_layer1_batch)
#print(link_D1_tangent_layer1_batch[0])
#print(link_D2_tangent_layer1_batch[0])

# Fix the keras predict method....
#link_D1_tangent_layer1_batch
#link_D2D1_tangent1.fit(link_D2_tangent_layer1_batch, link_D1_tangent_layer1_batch, epochs=5, batch_size=128)
#link_D2D1_tangent1.fit(link_D2_tangent_layer1_batch, link_D1_tangent_layer1_batch, epochs=5, batch_size=128)

#discovered_linkD1_past2_tangent_layer1 = link_D2D1_tangent1.predict(1)
#print("--------------------------------------------------------------------------------------------------------------------------------------------")

#print(discovered_linkD1_past2_tangent_layer1[0])
#exit()

#print(link_D1_bias_layer1_batch)
#print(link_D2_tangent_layer1_batch)
#print(link_D2_bias_layer1_batch)
#print(link_D1_tangent_layer1_batch[0].shape[0] * link_D1_tangent_layer1_batch[0].shape[1])
#link_D2D1_tangent1 = keras.models.Sequential()
#link_D1 = keras.models.Sequential()
#link_D1.add(keras.layers.Dense(64, activation='relu',))
#link_D1.add(keras.layers.Dense(64, activation='relu'))
#link_D1.add(keras.layers.Dense(1))
#link_D1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
#link_D1.fit(train_data_1, train_labels_1, epochs=5, batch_size=128)
#link_D1.summary()
#print(len(link_D1.layers))
#(train_images_2, train_labels_2), (test_images_2, test_labels_2) = keras.datasets.mnist.load_data()
#train_images_2 = train_images_2.reshape((60000, 28 * 28))
#train_images_2 = train_images_2.astype('float32') / 255
#print(len(train_images_2[0]))
#link_D2 = keras.models.Sequential()
#link_D2.add(keras.layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
#link_D2.add(keras.layers.Dense(10, activation='softmax'))
#link_D2.add(keras.layers.Dense(1))
#link_D2.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
#link_D2.fit(train_images_2, train_labels_2, epochs=5, batch_size=128)
# output_size
# link_D2.summary() 


###### Or this was functional ###################################################### 1/2

input_size = link_D1_tangent_layer1_batch[0].shape
output_size = link_D2_tangent_layer1_batch[0].shape
link_D2D1_tangent1 = keras.models.Sequential()
# time-series or similar stratified sampling data gives better loss
link_D2D1_tangent1.add(keras.Input(shape=input_size)) 
link_D2D1_tangent1.add(keras.layers.Dense(output_size[0] * output_size[1]))
link_D2D1_tangent1.add(keras.layers.Dense(output_size[0] * output_size[1]))
link_D2D1_tangent1.add(keras.layers.Dense(output_size[1]))
link_D2D1_tangent1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
link_D2D1_tangent1.fit(link_D2_tangent_layer1_batch, link_D1_tangent_layer1_batch, epochs=3, batch_size=128)
link_D2D1_tangent1.summary()
discovered_linkD1_past2_tangent_layer1 = link_D2D1_tangent1.predict(link_D2_tangent_layer1_batch)
print(discovered_linkD1_past2_tangent_layer1[0])


link_D1 = keras.models.Sequential()
link_D1.add(keras.layers.Dense(64, activation='relu',))
link_D1.add(keras.layers.Dense(64, activation='relu'))
link_D1.add(keras.layers.Dense(1))
link_D1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
link_D1.fit(train_data_1, train_labels_1, epochs=3, batch_size=128)
link_D1.summary()
discovered_linkD1_past2_tangent_layer1 = link_D1.predict(test_data_1)
# Another temporary route, is to explore link orders and the star DL-system in more nodes and edges
print(discovered_linkD1_past2_tangent_layer1)
# link_D1_tangent_layer1_batch[0].shape
#link_D2D1_bias1 = keras.models.Sequential()
#link_D2D1_bias1.add(keras.layers.Dense(link_D1_tangent_layer1_batch[0].shape[0] * link_D1_tangent_layer1_batch[0].shape[1], activation='relu', input_shape= (link_D1_bias_layer1_batch[0].shape,)))
#link_D2D1_bias1.add(keras.layers.Reshape(link_D1_bias_layer1_batch[0].shape))
#link_D2D1_bias1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
#link_D2D1_bias1.fit(link_D2_bias_layer1_batch, link_D1_bias_layer1_batch, epochs=5, batch_size=128)
#discovered_linkD1_past2_bias_layer1 = link_D2D1_bias1.predict(link_D1_bias_layer1_batch[0])
#print(discovered_linkD1_past2_tangent_layer1)
#print(discovered_linkD1_past2_tangent_layer1)
#print("--------------------------------------------------------------------------------------------------------------------------------------------")

#nb_hidden = 100

#model = Sequential()
#model.add(Dense(input_dim = 100, output_dim = nb_hidden)
#model.add(Dense(output_dim = 18, activation = 'softmax')
#model.compile(loss='categorical_crossentropy', optimizer='adadelta')


#tf.Tensor([[2 3] [4 5]], shape=(2, 2), dtype=int32) 


# Or this was functional


