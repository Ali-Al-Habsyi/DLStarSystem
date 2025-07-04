import keras
import pandas as pd
from zipfile import ZipFile
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import math
import os

sampling_rate = 6
sequence_length = 120
delay = sampling_rate * (sequence_length + 24 - 1)
batch_size = 256

##################################################################
# NODE-ENVIRONMENT PROCEDURE OF DOWNLOAD (License: Keras Developer)
##################################################################

from zipfile import ZipFile

uri = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip"
zip_path = keras.utils.get_file(origin=uri, fname="jena_climate_2009_2016.csv.zip")
zip_file = ZipFile(zip_path)
zip_file.extractall()
csv_path = "jena_climate_2009_2016.csv"
fname = os.path.join(csv_path)
with open(fname) as f:
    data = f.read()

lines = data.split("\n")
header = lines[0].split(",")
lines = lines[1:]

temperature = np.zeros((len(lines),))
raw_data = np.zeros((len(lines), len(header) - 1))

for i, line in enumerate(lines):
    values = [float(x) for x in line.split(",")[1:]]
    temperature[i] = values[1]
    raw_data[i, :] = values[:] 
    
sampling_rate = 6
sequence_length = 120
delay = sampling_rate * (sequence_length + 24 - 1)
batch_size = 256

# target in right column, input in left columns:
# extraction_2
# Debug and reterm

extraction_1 = [header[1],  header[3], header[2]]
extraction_2 = [header[4],  header[5], header[2]]
extraction_3 = [header[6], header[7], header[8], header[2]]
extraction_4 = [header[9], header[10], header[11], header[2]]
extraction_5 = [header[12], header[13], header[14], header[2]]
# data_extraction_1 = raw_data[3: -delay]

# display data catalogue
for i in range(len(header)):
    print((i, header[i]))

data_extraction_1_preprocess = raw_data[:-delay, [0, 2]] #3]]
data_extraction_2_preprocess = raw_data[:-delay, [4, 5]]
data_extraction_3_preprocess = raw_data[:-delay, [6, 7]] #8]]
data_extraction_4_preprocess = raw_data[:-delay, [9, 10]] #11]] # Make Node-observations equidimensional
data_extraction_5_preprocess = raw_data[:-delay, [12, 13]]
temperature_extraction_preprocess = temperature[delay:]


duration = len(raw_data) - delay
# INTRALINK_N 
#data_extraction_1 = data_extraction_1_preprocess
data_extraction_5 = data_extraction_5_preprocess
#data_extraction_5_preprocess = raw_data[:-delay, [12, 13]]
#temperature_extraction = temperature[math.floor(i * duration/INTRALINK_N) : math.floor((i + 1) * duration/INTRALINK_N)]

print(len(data_extraction_5))

INTERLINK_DENSITY = 3
INTRALINK_N = 9

# retweak
num_train_samples = math.floor(0.5 * duration/INTRALINK_N)
num_val_samples = math.floor(0.25 * duration/INTRALINK_N)
num_test_samples = math.floor(0.25 * duration/INTRALINK_N)
#batch_size = 10

#D5
train_node_5 = keras.utils.timeseries_dataset_from_array(
    data_extraction_5,
    targets=temperature_extraction,
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=0,
    end_index=num_train_samples)

val_node_5 = keras.utils.timeseries_dataset_from_array(
    data_extraction_5,
    targets=temperature_extraction,
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples,
    end_index=num_train_samples + num_val_samples)

test_node_5 = keras.utils.timeseries_dataset_from_array(
    data_extraction_5,
    targets=temperature_extraction,
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples + num_val_samples)


inputs = keras.Input(shape=(sequence_length, data_extraction_5.shape[-1]))
x = keras.layers.Dense(16, activation="relu")(inputs)
x = keras.layers.Dense(16, activation="relu")(x)
outputs = keras.layers.Dense(1)(x)
Intra_D5 = keras.Model(inputs, outputs)
callbacks = [
keras.callbacks.ModelCheckpoint("jena_dense.keras",
save_best_only=True)
]
Intra_D5.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = Intra_D5.fit(train_node_5,
    epochs=1,
    validation_data=val_node_5,
    callbacks=callbacks)
Intra_D5 = keras.models.load_model("jena_dense.keras")
print(f"Test MAE: {Intra_D5.evaluate(test_node_5)[1]:.2f}")

for j in range(1, INTERLINK_DENSITY + 1):
    np.array(Intra_D5._layers[j].get_weights()[0])
    np.array(Intra_D5._layers[j].get_weights()[1])       
    #threelayerlink_bidirectional_bias_storage[j][4][4].append(np.array(Intra_D5._layers[j].get_weights()[1]))

#Intra_D5._layers[j].get_weights()[0]




exit()


























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