######################################
#
# A DL Star-system with 4 nodes and variable link order
# 
#
#
######################################

import keras
import pandas as pd
from zipfile import ZipFile
import numpy as np
import matplotlib.pyplot as plt

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


for i in range(100):
    
    batch_size = [len(train_data_1), len(train_images_2)] 
    batch_training_1.append(train_data_1[i * batch_size[0] : (i + 1) * batch_size[0]])
    batch_test_1.append(test_labels_1[i * batch_size[0] : (i + 1) * batch_size[0]])
    batch_training_2.append(train_images_2[i * batch_size[1]  : (i + 1) * batch_size[1]])
    batch_test_2.append(train_images_2[i * batch_size[1]  : (i + 1) * batch_size[1]])
    #batch_training_3.append(train_data_3[i * batch_size[3] : (i + 1) * batch_size[2]])
    #batch_test_3.append(test_data_3[i * batch_size[3] : (i + 1) * batch_size[2]])
    #batch_training_4.append(train_data_4[i * batch_size[4] : (i + 1) * batch_size[3]])
    #batch_test_4.append(test_data_4[i * batch_size[3] : (i + 1) * batch_size[3]])
    
    link_D1 = keras.models.Sequential()
    link_D1.add(keras.layers.Dense(64, activation='relu',))
    link_D1.add(keras.layers.Dense(64, activation='relu'))
    link_D1.add(keras.layers.Dense(1))
    link_D1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    link_D1.fit(train_data_1, train_labels_1, epochs=5, batch_size=128)
    
    link_D1_tangent_layer1_batch.append(link_D1.layers[0].get_weights()[0])
    link_D1_tangent_layer2_batch.append(link_D1.layers[1].get_weights()[0])
    link_D1_tangent_layer3_batch.append(link_D1.layers[2].get_weights()[0])
    
    link_D1_bias_layer1_batch.append(link_D1.layers[0].get_weights()[1])
    link_D1_bias_layer2_batch.append(link_D1.layers[1].get_weights()[1])
    link_D1_bias_layer3_batch.append(link_D1.layers[2].get_weights()[1])
    
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
    
# towards D1 past D2 and D3 and D4
#########################################################################################################

# three layers, three links

input_tangent_size = link_D1_tangent_layer1_batch[0].shape
output_tangent_size = link_D2_tangent_layer1_batch[0].shape
input_bias_size = link_D1_tangent_layer1_batch[0].shape
output_bias_size = link_D2_tangent_layer1_batch[0].shape

link_D2D1_tangent1 = keras.models.Sequential()
link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[1]))
link_D2D1_tangent1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
link_D2D1_tangent1.fit(link_D2_tangent_layer1_batch, link_D1_tangent_layer1_batch, epochs=5, batch_size=128)
discovered_linkD1_past2_tangent_layer1 = link_D2D1_tangent1.predict(link_D1_tangent_layer1_batch[0])

link_D2D1_bias1 = keras.models.Sequential()
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[1]))
link_D2D1_tangent1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_tangent_layer2_batch = np.array(link_D1_tangent_layer2_batch)
link_D2_tangent_layer2_batch = np.array(link_D2_tangent_layer2_batch)

link_D2D1_tangent1.fit(link_D2_bias_layer1_batch, link_D1_bias_layer1_batch, epochs=5, batch_size=128)
discovered_linkD1_past2_bias_layer1 = link_D2D1_bias1.predict(link_D1_tangent_layer1_batch[0])

# TO D2 PAST D1

#L1
#########################################################################################################

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

link_D2D1_tangent1.fit(link_D1_tangent_layer1_batch, link_D2_tangent_layer1_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer1 = link_D2D1_tangent1.predict(link_D1_tangent_layer1_batch[0])

link_D2D1_bias1 = keras.models.Sequential()
link_D2D1_bias1.add(keras.layers.Dense(sum(link_D2_bias_layer2_batch[0].shape), activation='relu', input_shape=link_D2_bias_layer2_batch[0].shape))
link_D2D1_bias1.add(keras.layers.Reshape(link_D1_bias_batch[1].shape))
link_D2D1_bias1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D2D1_bias1 = keras.models.Sequential()
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias1.add(keras.layers.Dense(output_bias_size[1]))
link_D2D1_bias1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_bias_layer1_batch = np.array(link_D1_bias_layer1_batch)
link_D2_bias_layer1_batch = np.array(link_D2_bias_layer1_batch)

link_D2D1_bias1.fit(link_D1_bias_layer1_batch, link_D2_bias_layer1_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_bias_layer1 = link_D2D1_bias1.predict(link_D1_bias_layer1_batch[1])







# L2
#########################################################################################################

#link_D2D1_bias1.add(keras.layers.Dense(input_tangent_size[0] * input_tangent_size[1]))
#link_D2D1_bias1.add(keras.layers.Reshape(link_D1_bias_layer1_batch[0].shape))
#link_D2D1_bias1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
#link_D2D1_bias1.fit(link_D2_bias_layer1_batch, link_D1_bias_layer1_batch, epochs=5, batch_size=128)
#discovered_linkD1_past2_bias_layer1 = link_D2D1_bias1.predict(link_D1_bias_layer1_batch[0])

#print(discovered_linkD1_past2_tangent_layer1)
#print(discovered_linkD1_past2_tangent_layer1)

#link_D2D1_tangent1 = keras.models.Sequential()
#link_D2D1_tangent1.add(keras.Input(shape=input_size))  
#link_D2D1_tangent1.add(keras.layers.Dense(output_size[0] * output_size[1]))
#link_D2D1_tangent1.add(keras.layers.Dense(output_size[0] * output_size[1]))
#link_D2D1_tangent1.add(keras.layers.Dense(output_size[1]))
#link_D2D1_tangent1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
#inference1 = link_D2D1_tangent1.predict(link_D2_tangent_layer1_batch[0])
#print(inference1.shape)

####################################################################################################################
print("--------------------------------------------------------------------------------------------------------------------------------------------")

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

link_D2D1_tangent2.fit(link_D1_tangent_layer2_batch, link_D2_tangent_layer2_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer1 = link_D2D1_tangent1.predict(link_D1_tangent_layer2_batch[0])

# bias

input_bias_size = link_D1_bias_layer2_batch[0].shape
output_bias_size = link_D2_bias_layer2_batch[0].shape

link_D1_tangent_layer2_batch = np.array(link_D1_tangent_layer2_batch)
link_D2_tangent_layer2_batch = np.array(link_D2_tangent_layer2_batch)

link_D2D1_tangent2.fit(link_D2_tangent_batch, link_D1_tangent_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer2 = link_D2D1_tangent2.predict(link_D2_tangent_batch[1])

link_D2D1_bias2 = keras.models.Sequential()
link_D2D1_bias2.add(keras.layers.Dense(sum(link_D2_bias_layer2_batch[0].shape), activation='relu', input_shape=link_D2_bias_layer2_batch[0].shape))
link_D2D1_bias2.add(keras.layers.Reshape(link_D1_bias_batch[1].shape))
link_D2D1_bias2.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D2D1_bias2 = keras.models.Sequential()
link_D2D1_bias2.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias2.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias2.add(keras.layers.Dense(output_bias_size[1]))
link_D2D1_bias2.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_bias_layer2_batch = np.array(link_D1_bias_layer2_batch)
link_D2_bias_layer2_batch = np.array(link_D2_bias_layer2_batch)

link_D2D1_bias2.fit(link_D2_bias_layer2_batch, link_D1_bias_layer2_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_bias_layer2 = link_D2D1_bias2.predict(link_D1_bias_layer2_batch[1])

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

link_D2D1_tangent3.fit(link_D1_tangent_layer3_batch, link_D2_tangent_layer3_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_tangent_layer3 = link_D2D1_tangent3.predict(link_D1_tangent_layer3_batch[0])

# bias

input_bias_size = link_D1_bias_layer3_batch[0].shape
output_bias_size = link_D2_bias_layer3_batch[0].shape

link_D1_tangent_layer3_batch = np.array(link_D1_tangent_layer3_batch)
link_D2_tangent_layer3_batch = np.array(link_D2_tangent_layer3_batch)

link_D2D1_bias3 = keras.models.Sequential()
link_D2D1_bias3.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias3.add(keras.layers.Dense(output_bias_size[0] * output_bias_size[1]))
link_D2D1_bias3.add(keras.layers.Dense(output_bias_size[1]))
link_D2D1_bias3.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_bias_layer3_batch = np.array(link_D1_bias_layer3_batch)
link_D2_bias_layer3_batch = np.array(link_D2_bias_layer3_batch)

link_D2D1_bias3.fit(link_D1_bias_layer3_batch, link_D2_bias_layer3_batch, epochs=5, batch_size=128)
discovered_linkD2_past1_bias_layer3 = link_D2D1_bias3.predict(link_D1_bias_batch[1])

#link_D2D1_bias3.fit(link_D2_tangent_batch, link_D1_tangent_batch, epochs=5, batch_size=128)
#discovered_linkD1_past2_tangent_layer2 = link_D2D1_tangent2.predict(link_D2_tangent_batch[1])

#link_D2D1_bias3 = keras.models.Sequential()
#link_D2D1_bias3.add(keras.layers.Dense(sum(link_D2_bias_layer2_batch[0].shape), activation='relu', input_shape=link_D2_bias_layer2_batch[0].shape))
#link_D2D1_bias3.add(keras.layers.Reshape(link_D1_bias_batch[1].shape))
#link_D2D1_bias3.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

#link_D2D1_bias2 = keras.models.Sequential()
#link_D2D1_bias2.add(keras.layers.Dense(input_tangent_size[0] * input_tangent_size[1]))
#link_D2D1_bias2.add(keras.layers.Dense(input_tangent_size[0] * input_tangent_size[1]))
#link_D2D1_bias2.add(keras.layers.Dense(input_tangent_size[1]))
#link_D2D1_bias2.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

#link_D1_bias_layer2_batch = np.array(link_D1_bias_layer2_batch)
#link_D2_bias_layer2_batch = np.array(link_D2_bias_layer2_batch)

#link_D2D1_bias3.fit(link_D2_bias_layer2_batch, link_D1_bias_layer2_batch, epochs=5, batch_size=128)
#discovered_linkD1_past2_bias_layer2 = link_D2D1_bias2.predict(link_D1_bias_batch[1])


# inference
####################################################################################################################

discovered_linkD2_past1_tangent_layer1
discovered_linkD2_past1_bias_layer1
discovered_linkD2_past1_tangent_layer2
discovered_linkD2_past1_bias_layer2
discovered_linkD2_past1_tangent_layer3
discovered_linkD2_past1_bias_layer3

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

link_node2_D1_discovered.predict(test_labels_2)











input_tangent_size = link_D1_tangent_layer3_batch[0].shape
output_tangent_size = link_D2_tangent_layer3_batch[0].shape
input_bias_size = link_D1_tangent_layer3_batch[0].shape
output_bias_size = link_D2_tangent_layer3_batch[0].shape

link_D2D1_tangent3 = keras.models.Sequential()
link_D2D1_tangent3.add(keras.layers.Dense(sum(link_D1_tangent_batch[2].shape), activation='relu', input_shape=link_D2_tangent_batch[2].shape))
link_D2D1_tangent3.add(keras.layers.Reshape(link_D1_tangent_batch[2].shape))
link_D2D1_tangent3.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_tangent_layer2_batch = np.array(link_D1_tangent_layer2_batch)
link_D2_tangent_layer2_batch = np.array(link_D2_tangent_layer2_batch)

link_D2D1_tangent3.fit(link_D2_tangent_batch[2], link_D1_tangent_batch[2], epochs=5, batch_size=128)
discovered_linkD1_past2_tangent_layer3 = link_D2D1_tangent2.predict(link_D2_tangent_batch[2])

link_D2D1_bias3 = keras.models.Sequential()
link_D2D1_bias3.add(keras.layers.Dense(sum(link_D1_bias_batch[2].shape), activation='relu', input_shape=link_D2_bias_batch[2].shape))
link_D2D1_bias3.add(keras.layers.Reshape(link_D1_bias_batch[2].shape))
link_D2D1_bias3.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

link_D1_bias_layer3_batch = np.array(link_D1_tangent_layer3_batch)
link_D2_bias_layer3_batch = np.array(link_D2_tangent_layer3_batch)

link_D2D1_bias3.fit(link_D2_bias_batch[2], link_D1_bias_batch[2], epochs=5, batch_size=128)
discovered_linkD1_past2_bias_layer3 = link_D2D1_bias2.predict(link_D2_bias_batch[2])

print(discovered_linkD1_past2_tangent_layer1)
print(discovered_linkD1_past2_tangent_layer1)

####################################################################################################################

link_node2_D1_discovered = keras.models.Sequential()
link_node2_D1_discovered.add(keras.layers.Dense(units = 64, 
    kernel_initializer = discovered_linkD1_past2_tangent[0],
    bias_initializer= discovered_linkD1_past2_bias[0]  
    ))
link_node2_D1_discovered.add(keras.layers.Dense(units = 64, 
    kernel_initializer = discovered_linkD1_past2_tangent[1],
    bias_initializer=discovered_linkD1_past2_bias[1]
    ))       
link_node2_D1_discovered.add(keras.layers.Dense(units = 1, 
    kernel_initializer = discovered_linkD1_past2_tangent[2],
    bias_initializer= discovered_linkD1_past2_bias[2]
    ))    
link_node2_D1_discovered.predict(test_labels_2)

link_node2_D1_discovered.compile(optimizer='rmsprop',
        loss='binary_crossentropy',
        metrics=['acc'])






























link_D2D1_tangent = keras.models.Sequential()
link_D2D1_tangent.add(keras.layers.Dense(sum(link_D1_tangent.shape), activation='relu', input_shape=link_D2_tangent.shape))
link_D2D1_tangent.add(keras.layers.Reshape(link_D1_tangent.shape))
link_D2D1_tangent.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
link_D2D1_tangent.fit(link_D2_tangent_batch, link_D1_tangent_batch, epochs=5, batch_size=128)
discovered_linkD1_past2_tangent = link_D2D1_tangent.predict(link_D2_tangent_batch[0])

link_D2D1_bias = keras.models.Sequential()
link_D2D1_bias.add(keras.layers.Dense(sum(link_D1_bias.shape), activation='relu', input_shape=link_D2_bias.shape))
link_D2D1_bias.add(keras.layers.Reshape(link_D1_bias.shape))
link_D2D1_bias.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
link_D2D1_bias.fit(link_D2_bias_batch, link_D1_bias_batch, epochs=5, batch_size=128)
discovered_linkD1_past2_bias = link_D2D1_bias.predict(link_D2_bias_batch[0])

link_node2_D1_discovered = keras.models.Sequential()
link_node2_D1_discovered.add(keras.layers.Dense(units = 64, 
    kernel_initializer = discovered_linkD1_past2_tangent[0],
    bias_initializer= discovered_linkD1_past2_bias[0]  
    ))
link_node2_D1_discovered.add(keras.layers.Dense(units = 64, 
    kernel_initializer = discovered_linkD1_past2_tangent[1],
    bias_initializer=discovered_linkD1_past2_bias[1]
    ))       
link_node2_D1_discovered.add(keras.layers.Dense(units = 1, 
    kernel_initializer = discovered_linkD1_past2_tangent[2],
    bias_initializer= discovered_linkD1_past2_bias[2]
    ))    
link_node2_D1_discovered.predict(test_labels_2)

link_node2_D1_discovered.compile(optimizer='rmsprop',
        loss='binary_crossentropy',
        metrics=['acc'])






















# rudimentary visualizations
# Evaluate performances link_node3_D1_discovered, link_node2_D1_discovered, link_internodal_D1_discovered
# The above assumes stratified data-sampling over all data-environments D1 to D5, only automatic via time-series, otherwise via some external arrangement

# rudimentary visualizations
# Evaluate performances link_node3_D1_discovered, link_node2_D1_discovered, link_internodal_D1_discovered
# The above assumes stratified data-sampling over all data-environments D1 to D5, only automatic via time-series, otherwise via some external arrangement

############################################################################################################

# simplest plot 
# towards D1 past D2

link_D2D1_tangent = keras.models.Sequential()
link_D2D1_tangent.add(keras.layers.Dense(sum(link_D1_tangent.shape), activation='relu', input_shape=link_D2_tangent.shape))
link_D2D1_tangent.add(keras.layers.Reshape(link_D1_tangent.shape))
link_D2D1_tangent.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
link_D2D1_tangent.fit(link_D2_tangent_batch, link_D1_tangent_batch, epochs=5, batch_size=128)
discovered_linkD1_past2_tangent = link_D2D1_tangent.predict(link_D2_tangent_batch[0])






link_D2D1_bias = keras.models.Sequential()
link_D2D1_bias.add(keras.layers.Dense(sum(link_D1_bias.shape), activation='relu', input_shape=link_D2_bias.shape))
link_D2D1_bias.add(keras.layers.Reshape(link_D1_bias.shape))
link_D2D1_bias.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
link_D2D1_bias.fit(link_D2_bias_batch, link_D1_bias_batch, epochs=5, batch_size=128)
discovered_linkD1_past2_bias = link_D2D1_bias.predict(link_D2_bias_batch[0])

link_node2_D1_discovered = keras.models.Sequential()
link_node2_D1_discovered.add(keras.layers.Dense(units = 64, 
    kernel_initializer = discovered_linkD1_past2_tangent[0],
    bias_initializer= discovered_linkD1_past2_bias[0]  
    ))
link_node2_D1_discovered.add(keras.layers.Dense(units = 64, 
    kernel_initializer = discovered_linkD1_past2_tangent[1],
    bias_initializer=discovered_linkD1_past2_bias[1]
    ))       
link_node2_D1_discovered.add(keras.layers.Dense(units = 1, 
    kernel_initializer = discovered_linkD1_past2_tangent[2],
    bias_initializer= discovered_linkD1_past2_bias[2]
    ))    
link_node2_D1_discovered.predict(test_labels_2)

link_node2_D1_discovered.compile(optimizer='rmsprop',
        loss='binary_crossentropy',
        metrics=['acc'])

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

############################################################################################################