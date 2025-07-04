######################################
#
# A DL Star-system with 2 nodes, monodirectional, i.e., a DL Star-system in its smallest possible scale
# Start accounting for matters of computing power/memory
#
######################################

import keras
import pandas as pd
from zipfile import ZipFile
import numpy as np
import matplotlib.pyplot as plt
import math

# Time series data better, otherwise assume underlying unity in observation index
# D1
(train_data_1, train_labels_1), (test_data_1, test_labels_1) = keras.datasets.boston_housing.load_data()

#D2
(train_images_2, train_labels_2), (test_images_2, test_labels_2) = keras.datasets.mnist.load_data()
train_images_2 = train_images_2.reshape((60000, 28 * 28))
train_images_2 = train_images_2.astype('float32') / 255

batch_training_1 = []
batch_test_1 = []
batch_training_2 = []
batch_test_2 = []
batch_training_3 = []
batch_test_3 = []
batch_training_4 = []
batch_test_4 = []
link_D1_tangent_batch = []
link_D1_bias_batch = []
link_D2_tangent_batch = []
link_D2_bias_batch = []
link_D3_tangent_batch = []
link_D3_bias_batch = []
link_D4_tangent_batch = []
link_D4_bias_batch = []


link_D1_tangent_layer1_batch = []
link_D1_tangent_layer2_batch = []
link_D1_tangent_layer3_batch = []
link_D1_bias_layer1_batch = []
link_D1_bias_layer2_batch = []
link_D1_bias_layer3_batch = []

link_D2_tangent_layer1_batch = []
link_D2_tangent_layer2_batch = []
link_D2_tangent_layer3_batch = []
link_D2_bias_layer1_batch = []
link_D2_bias_layer2_batch = []
link_D2_bias_layer3_batch = []

link_collection_size = 10

batch_size = [math.floor(len(train_data_1) / 10), math.floor(len(train_images_2) / 10)] 
for i in range(0, link_collection_size): 
    

    batch_training_1.append(train_data_1[i * batch_size[0] : (i + 1) * (batch_size[0])])
    batch_test_1.append(test_labels_1[i * batch_size[0] : (i + 1) * batch_size[0]])
    batch_training_2.append(train_images_2[i * batch_size[1]  : (i + 1) * batch_size[1]])
    batch_test_2.append(test_labels_2[i * batch_size[1]  : (i + 1) * batch_size[1]])

    link_D1 = keras.models.Sequential()
    link_D1.add(keras.layers.Dense(64, activation='relu',))
    link_D1.add(keras.layers.Dense(64, activation='relu'))
    link_D1.add(keras.layers.Dense(1))
    link_D1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    link_D1.fit(train_data_1, train_labels_1, epochs=5, batch_size=128)
    # the possibility of computation relies on this network
    link_D1_tangent_layer1_batch.append(link_D1.layers[0].get_weights()[0])
    link_D1_tangent_layer2_batch.append(link_D1.layers[1].get_weights()[0])
    link_D1_tangent_layer3_batch.append(link_D1.layers[2].get_weights()[0])
    
    link_D1_bias_layer1_batch.append(link_D1.layers[0].get_weights()[1])
    link_D1_bias_layer2_batch.append(link_D1.layers[1].get_weights()[1])
    link_D1_bias_layer3_batch.append(link_D1.layers[2].get_weights()[1])
    # the possibility of computation relies on this network
    link_D2 = keras.models.Sequential()
    link_D2.add(keras.layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
    link_D2.add(keras.layers.Dense(10, activation='softmax'))
    link_D2.add(keras.layers.Dense(1))
    link_D2.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    link_D2.fit(train_images_2, train_labels_2, epochs=5, batch_size=128)
    
    link_D2_tangent_layer1_batch.append(link_D2.layers[0].get_weights()[0])
    link_D2_tangent_layer2_batch.append(link_D2.layers[1].get_weights()[0])
    link_D2_tangent_layer3_batch.append(link_D2.layers[2].get_weights()[0])
    
    link_D2_bias_layer1_batch.append(link_D2.layers[0].get_weights()[1])
    link_D2_bias_layer2_batch.append(link_D2.layers[1].get_weights()[1])
    link_D2_bias_layer3_batch.append(link_D2.layers[2].get_weights()[1])
    
    
#########################################################################################################
    
print("-------------------------------------------------")
print("D1TL1")
link_D1_tangent_layer1_batch = np.array(link_D1_tangent_layer1_batch)
print(link_D1_tangent_layer1_batch.shape)
print("D1TL2")
link_D1_tangent_layer2_batch = np.array(link_D1_tangent_layer2_batch)
print(link_D1_tangent_layer2_batch.shape)
print("D1TL3")
link_D1_tangent_layer3_batch = np.array(link_D1_tangent_layer3_batch)
print(link_D1_tangent_layer3_batch.shape)
print("D1BL1")
link_D1_bias_layer1_batch = np.array(link_D1_bias_layer1_batch)
print(link_D1_bias_layer1_batch.shape)
print("D1BL2")
link_D1_bias_layer2_batch = np.array(link_D1_bias_layer2_batch)
print(link_D1_bias_layer2_batch.shape)
print("D1BL3")
link_D1_bias_layer3_batch = np.array(link_D1_bias_layer3_batch)
print(link_D1_bias_layer3_batch.shape)
print("D2TL1")
link_D2_tangent_layer1_batch = np.array(link_D2_tangent_layer1_batch)
print(link_D2_tangent_layer1_batch.shape)
print("D2TL2")
link_D2_tangent_layer2_batch = np.array(link_D2_tangent_layer2_batch)
print(link_D2_tangent_layer2_batch.shape)
print("D2TL3")
link_D2_tangent_layer3_batch = np.array(link_D2_tangent_layer3_batch)
print(link_D2_tangent_layer3_batch.shape)
print("D2BL1")
link_D2_bias_layer1_batch = np.array(link_D2_bias_layer1_batch)
print(link_D2_bias_layer1_batch.shape)
print("D2BL2")
link_D2_bias_layer2_batch = np.array(link_D2_bias_layer2_batch)
print(link_D2_bias_layer2_batch.shape)
print("D2BL3")
link_D2_bias_layer3_batch = np.array(link_D2_bias_layer3_batch)
print(link_D2_bias_layer3_batch.shape)

print("-------------------------------------------------")
#exit()
#########################################################################################################
    
# towards D1 past D2 and D3 and D4
#########################################################################################################
# Functional
# TO D2 PAST D1 (one directed edge, two nodes)
# Extend to 5 node system configured in complete birectional graph 
# Find general code for n nodes

# For succesful computation, i.e. for no bug zsh:killed, networks at data-environments must be small
# Sure computation for data environment input/output 10-dimensional vectors and thin layers
# Reimplementation in the smallest possible scale

#L1
#########################################################################################################

print(len(link_D1_tangent_layer1_batch))
print(len(link_D2_tangent_layer1_batch))
print(len(link_D1_bias_layer1_batch))
print(len(link_D2_bias_layer1_batch))

link_D1_tangent_layer1_batch = np.array(link_D1_tangent_layer1_batch)
link_D2_tangent_layer1_batch = np.array(link_D2_tangent_layer1_batch)
link_D1_bias_layer1_batch = np.array(link_D1_bias_layer1_batch)
link_D2_bias_layer1_batch = np.array(link_D2_bias_layer1_batch)

#print(link_D1_tangent_layer1_batch.shape)
#print(link_D2_tangent_layer1_batch.shape)
#print(link_D1_bias_layer1_batch)
#print(link_D2_bias_layer1_batch.shape)

# fix neural network fit argument dimensions

input_tangent_size = link_D1_tangent_layer1_batch[0].shape
output_tangent_size = link_D2_tangent_layer1_batch[0].shape
input_bias_size = link_D1_bias_layer1_batch[0].shape
output_bias_size = link_D2_bias_layer1_batch[0].shape

link_D2D1_tangent1 = keras.models.Sequential()
link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[1]))
link_D2D1_tangent1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_tangent_layer1_batch = np.array(link_D1_tangent_layer1_batch)
link_D2_tangent_layer1_batch = np.array(link_D2_tangent_layer1_batch)
#print(link_D1_tangent_layer1_batch.shape)
#print(link_D2_tangent_layer1_batch.shape)

amplified_batch_array = np.zeros((link_collection_size, 784, 512))
for i in range(amplified_batch_array.shape[0]):
    for j in range(amplified_batch_array.shape[1]):
        for k in range(amplified_batch_array.shape[2]):
            if j < 13 and k < 64:
                amplified_batch_array[i][j][k] = link_D1_tangent_layer1_batch[i][j][k]

#amplified_batch_array = np.concatenate((link_D2_tangent_layer1_batch, np.zeros((len(link_D1_tangent_layer1_batch), 784-13, 512))), axis=1)
#amplified_batch_array = np.concatenate((link_D1_tangent_layer1_batch, np.zeros((link_D2_tangent_layer1_batch.shape[0], 784 - 13, 512))), axis=1)

print(amplified_batch_array.shape)
print(link_D2_tangent_layer1_batch.shape)

link_D2D1_tangent1.fit(amplified_batch_array, link_D2_tangent_layer1_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer1 = link_D2D1_tangent1.predict(amplified_batch_array)
discovered_linkD2_past1_tangent_layer1 = discovered_linkD2_past1_tangent_layer1[0]

# Recurring bug: zsh killed: memory issue: matrices too many entries

link_D2D1_bias1 = keras.models.Sequential()
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[0]))
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[0]))
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[0]))
link_D2D1_bias1.compile(optimizer='adam', loss='mse', metrics=['mae'])

link_D1_bias_layer1_batch = np.array(link_D1_bias_layer1_batch)
link_D2_bias_layer1_batch = np.array(link_D2_bias_layer1_batch)
amplified_batch_array = np.zeros((link_collection_size, 512))

for i in range(amplified_batch_array.shape[0]):
    for j in range(amplified_batch_array.shape[1]):
        if j < 64:
            amplified_batch_array[i][j] = link_D1_bias_layer1_batch[i][j]

link_D2D1_bias1.fit(amplified_batch_array, link_D2_bias_layer1_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_bias_layer1 = link_D2D1_bias1.predict(amplified_batch_array[0])
discovered_linkD2_past1_bias_layer1 = discovered_linkD2_past1_bias_layer1[0]

# L2
####################################################################################################################
# tangent

input_tangent_size = link_D1_tangent_layer2_batch[0].shape
output_tangent_size = link_D2_tangent_layer2_batch[0].shape

link_D2D1_tangent2 = keras.models.Sequential()
link_D2D1_tangent2.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
link_D2D1_tangent2.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
link_D2D1_tangent2.add(keras.layers.Dense(output_tangent_size[1]))
link_D2D1_tangent2.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_tangent_layer2_batch = np.array(link_D1_tangent_layer2_batch)
link_D2_tangent_layer2_batch = np.array(link_D2_tangent_layer2_batch)

#amplified_batch_array = np.zeros((link_collection_size, 512, 64))

link_D2_tangent_layer2_batch = link_D2_tangent_layer2_batch.reshape((link_collection_size, 64, 80))
amplified_batch_array = np.zeros((link_collection_size, 64, 80))

for i in range(link_D2_tangent_layer2_batch.shape[0]):
    for j in range(link_D2_tangent_layer2_batch.shape[1]):
        for k in range(link_D2_tangent_layer2_batch.shape[2]): 
            if k >= 64 and k < 80:
                link_D2_tangent_layer2_batch[i][j][k] = 0
            else:
                amplified_batch_array[i][j][k] = link_D1_tangent_layer2_batch[i][j][k]

link_D2D1_tangent2.fit(amplified_batch_array, link_D2_tangent_layer2_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer1 = link_D2D1_tangent1.predict(amplified_batch_array)
discovered_linkD2_past1_tangent_layer1 = discovered_linkD2_past1_tangent_layer1[0]

# bias

input_bias_size = link_D1_bias_layer2_batch[0].shape
output_bias_size = link_D2_bias_layer2_batch[0].shape

link_D1_tangent_layer2_batch = np.array(link_D1_tangent_layer2_batch)
link_D2_tangent_layer2_batch = np.array(link_D2_tangent_layer2_batch)

link_D2D1_tangent2.fit(link_D2_tangent_batch, link_D1_tangent_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer2 = link_D2D1_tangent2.predict(link_D2_tangent_batch[1])

link_D2D1_bias2 = keras.models.Sequential()
link_D2D1_bias2.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias2.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias2.add(keras.layers.Dense(output_bias_size[1]))
link_D2D1_bias2.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_bias_layer2_batch = np.array(link_D1_bias_layer2_batch)
link_D2_bias_layer2_batch = np.array(link_D2_bias_layer2_batch)

# check for amplification location: either at location pointer or pointee, depending on input/output dimensions
amplified_batch_array = np.zeros((link_collection_size, 64))
for i in range(amplified_batch_array.shape[0]):
    for j in range(amplified_batch_array.shape[1]):
        if j < 10:
            amplified_batch_array[i][j] = link_D2_bias_layer2_batch[i][j]

link_D2D1_bias2.fit(link_D1_bias_layer2_batch, amplified_batch_array, epochs=5, batch_size=128)
discovered_linkD2_past1_bias_layer2 = link_D2D1_bias2.predict(link_D1_bias_layer2_batch)
discovered_linkD2_past1_bias_layer2 = discovered_linkD2_past1_bias_layer2[0][:10]

#L3
####################################################################################################################
# tangent

input_tangent_size = link_D1_tangent_layer3_batch[0].shape
output_tangent_size = link_D2_tangent_layer3_batch[0].shape

link_D2D1_tangent3 = keras.models.Sequential()
link_D2D1_tangent3.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
link_D2D1_tangent3.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
link_D2D1_tangent3.add(keras.layers.Dense(output_tangent_size[1]))
link_D2D1_tangent3.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_tangent_layer3_batch = np.array(link_D1_tangent_layer3_batch)
link_D2_tangent_layer3_batch = np.array(link_D2_tangent_layer3_batch)

#link_D2_tangent_layer3_batch
#amplified_batch_array = np.zeros((link_collection_size, 64, 1))
for i in range(amplified_batch_array.shape[0]):
    for j in range(amplified_batch_array.shape[1]):
        for k in range(amplified_batch_array.shape[2]):
            if k < 10:
                amplified_batch_array[i][j][k] = link_D2_tangent_layer3_batch[i][j][k]

#link_D1_tangent_layer3_batch
#link_D2_tangent_layer3_batch
link_D2D1_tangent3.fit(link_D1_tangent_layer3_batch, amplified_batch_array, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer3 = link_D2D1_tangent3.predict(link_D1_tangent_layer3_batch)
discovered_linkD2_past1_tangent_layer3 = discovered_linkD2_past1_tangent_layer3[0]

# bias

input_bias_size = link_D1_bias_layer3_batch[0].shape
output_bias_size = link_D2_bias_layer3_batch[0].shape

link_D2D1_bias3 = keras.models.Sequential()
link_D2D1_bias3.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias3.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias3.add(keras.layers.Dense(output_bias_size[1]))
link_D2D1_bias3.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_bias_layer3_batch = np.array(link_D1_bias_layer3_batch)
link_D2_bias_layer3_batch = np.array(link_D2_bias_layer3_batch)

#amplified_batch_array = np.zeros((link_collection_size, link_D1_tangent_layer1_batch[0].shape[1], link_D1_tangent_layer1_batch[0].shape[2]))
#for i in range(amplified_batch_array.shape[0]):
#    for j in range(amplified_batch_array.shape[1]):
#        for k in range(amplified_batch_array.shape[2]):
#            if j < 13 and k < 64:
#                amplified_batch_array[i][j][k] = link_D1_tangent_layer1_batch[i][j][k]

# Amplification no need here since input/output have same dimensions

link_D2D1_bias3.fit(link_D1_bias_layer3_batch, link_D2_bias_layer3_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_bias_layer3 = link_D2D1_bias3.predict(link_D1_bias_batch)
discovered_linkD2_past1_bias_layer3 = discovered_linkD2_past1_bias_layer3[0]
link_D1_bias_layer3_batch = np.array(link_D1_bias_layer3_batch)

#link_D2_tangent_layer3_batch
#amplified_batch_array = np.zeros((link_collection_size, 64, 1))
for i in range(amplified_batch_array.shape[0]):
    for j in range(amplified_batch_array.shape[1]):
            if k < 10:
                amplified_batch_array[i][j][k] = link_D2_tangent_layer3_batch[i][j][k]

#link_D1_tangent_layer3_batch
#link_D2_tangent_layer3_batch
link_D2D1_tangent3.fit(link_D1_tangent_layer3_batch, amplified_batch_array, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer3 = link_D2D1_tangent3.predict(link_D1_tangent_layer3_batch)
discovered_linkD2_past1_tangent_layer3 = discovered_linkD2_past1_tangent_layer3[0]


# inference
####################################################################################################################

# discovered_linkD2_past1_tangent_layer1
# discovered_linkD2_past1_bias_layer1
# discovered_linkD2_past1_tangent_layer2
# discovered_linkD2_past1_bias_layer2
# discovered_linkD2_past1_tangent_layer3
# discovered_linkD2_past1_bias_layer3

link_node2_D1_discovered = keras.models.Sequential()
link_node2_D1_discovered.add(keras.layers.Dense(units = 64, 
    kernel_initializer = discovered_linkD2_past1_tangent_layer1,
    bias_initializer= discovered_linkD2_past1_bias_layer1  
    ))
link_node2_D1_discovered.add(keras.layers.Dense(units = 64, 
    kernel_initializer = discovered_linkD2_past1_tangent_layer2,
    bias_initializer= discovered_linkD2_past1_bias_layer2
    ))       
link_node2_D1_discovered.add(keras.layers.Dense(units = 1, 
    kernel_initializer = discovered_linkD2_past1_tangent_layer3,
    bias_initializer= discovered_linkD2_past1_bias_layer3
    ))    
link_node2_D1_discovered.compile(optimizer='rmsprop',
        loss='binary_crossentropy',
        metrics=['acc'])

# Final inference
link_node2_D1_discovered.predict(test_labels_2)

# performance evaluation
history = link_node2_D1_discovered.fit(train_images_2, train_labels_2,
    epochs=10,
    batch_size=32)
acc = history.history['acc']
loss = history.history['loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.title('Training loss, first epoch is the manually computed optimized network, further computation due to RMSprop')
plt.legend()
plt.show()


# functional implementation