##################################################################
#
# 
# Arch DL Starsystem, 5 Data-environments, bidirectional internode links, monodirectional intranode links, low-dimensional data (sampled by stratification)
# Computable implementation of sub-minimal scale
# Extent of inter-/ or intralink-complexity only due NN Specification.
# For considering effectivity of system over node-counts and stratified data, fix NN-link to dense
##################################################################

import keras
import numpy as np
import os


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

extraction_1 = [header[1],  header[3], header[2]]
extraction_2 = [header[4],  header[5], header[2]]
extraction_3 = [header[6], header[7], header[8], header[2]]
extraction_4 = [header[9], header[10], header[11], header[2]]
extraction_5 = [header[12], header[13], header[14], header[2]]
#data_extraction_1 = raw_data[3: -delay]

# display data catalogue
for i in range(len(header)):
    print((i, header[i]))

data_extraction_1 = raw_data[:-delay, [0, 2, 3]]
data_extraction_2 = raw_data[:-delay, [4, 5]]
data_extraction_3 = raw_data[:-delay, [6, 7, 8]]
data_extraction_4 = raw_data[:-delay, [9, 10, 11]]
data_extraction_5 = raw_data[:-delay, [12, 13]]
target_extraction = temperature[delay:]

print(data_extraction_1.shape)
print(data_extraction_2.shape)
print(data_extraction_3.shape)
print(data_extraction_4.shape)
print(data_extraction_5.shape)

num_train_samples = int(0.5 * len(raw_data))
num_val_samples = int(0.25 * len(raw_data))
num_test_samples = len(raw_data) - num_train_samples - num_val_samples

#D1

# The manual route of node-construction
#training
start_index=0,
end_index=num_train_samples
data_extraction_1_training = data_extraction_1[start_index:end_index]
target_extraction = temperature[delay:]
targets_1_training = target_extraction[start_index:end_index]

#validation
start_index=num_train_samples,
end_index=num_train_samples + num_val_samples
data_extraction_1_val = data_extraction_2[start_index:end_index]
targets_1_validation = target_extraction[start_index:end_index]

#test
start_index=num_train_samples + num_val_samples
data_extraction_1_test = data_extraction_2[start_index:end_index]
targets_1_test = target_extraction[start_index:end_index]

data_extraction_1[:-delay],
targets=temperature[delay:],
start_index=num_train_samples + num_val_samples

#sampling_rate=sampling_rate,
#sequence_length=sequence_length,
#shuffle=True,
#batch_size=batch_size,


############################################################
train_node_1 = keras.utils.timeseries_dataset_from_array(
    data_extraction_1[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=0,
    end_index=num_train_samples)

val_node_1 = keras.utils.timeseries_dataset_from_array(
    data_extraction_1[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples,
    end_index=num_train_samples + num_val_samples)

test_node_1 = keras.utils.timeseries_dataset_from_array(
    data_extraction_1[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples + num_val_samples)
############################################################


# 


#D2
# The manual route of node-construction
#training
data_extraction_2[:-delay]
targets=temperature[delay:],
start_index=0,
end_index=num_train_samples

#validation
data_extraction_2[:-delay]
targets=temperature[delay:],
start_index=num_train_samples,
end_index=num_train_samples + num_val_samples

#test
data_extraction_2[:-delay],
targets=temperature[delay:],
start_index=num_train_samples + num_val_samples

#sampling_rate=sampling_rate,
#sequence_length=sequence_length,
#shuffle=True,
#batch_size=batch_size,

#D2
# The manual route of node-construction
#training
start_index=0,
end_index=num_train_samples
data_extraction_2_training = data_extraction_2[start_index:end_index]
target_extraction = temperature[delay:]
targets_2_training = target_extraction[start_index:end_index]

#validation
start_index=num_train_samples,
end_index=num_train_samples + num_val_samples
data_extraction_2_val = data_extraction_2[start_index:end_index]
targets_2_validation = target_extraction[start_index:end_index]

#test
start_index=num_train_samples + num_val_samples
data_extraction_2_test = data_extraction_2[start_index:end_index]
targets_2_test = target_extraction[start_index:end_index]


#D3
# The manual route of node-construction
#training
start_index=0,
end_index=num_train_samples
data_extraction_3_training = data_extraction_3[start_index:end_index]
target_extraction = temperature[delay:]
targets_3_training = target_extraction[start_index:end_index]

#validation
start_index=num_train_samples,
end_index=num_train_samples + num_val_samples
data_extraction_2_val = data_extraction_2[start_index:end_index]
targets_3_validation = target_extraction[start_index:end_index]

#test
start_index=num_train_samples + num_val_samples
data_extraction_2_test = data_extraction_2[start_index:end_index]
targets_3_test = target_extraction[start_index:end_index]






train_node_2 = keras.utils.timeseries_dataset_from_array(
    data_extraction_2[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=0,
    end_index=num_train_samples)

val_node_2 = keras.utils.timeseries_dataset_from_array(
    data_extraction_2[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples,
    end_index=num_train_samples + num_val_samples)

test_node_2 = keras.utils.timeseries_dataset_from_array(
    data_extraction_2[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples + num_val_samples)


# The manual route of node-construction
#training
data_extraction_2[:-delay]
targets=temperature[delay:],
start_index=0,
end_index=num_train_samples

#validation
data_extraction_2[:-delay]
targets=temperature[delay:],
start_index=num_train_samples,
end_index=num_train_samples + num_val_samples

#test
data_extraction_2[:-delay],
targets=temperature[delay:],
start_index=num_train_samples + num_val_samples

#sampling_rate=sampling_rate,
#sequence_length=sequence_length,
#shuffle=True,
#batch_size=batch_size,


#D3
# The manual route of node-construction
#training
data_extraction_3[:-delay]
targets=temperature[delay:],
start_index=0,
end_index=num_train_samples

#validation
data_extraction_3[:-delay]
targets=temperature[delay:],
start_index=num_train_samples,
end_index=num_train_samples + num_val_samples

#test
data_extraction_3[:-delay],
targets=temperature[delay:],
start_index=num_train_samples + num_val_samples

#sampling_rate=sampling_rate,
#sequence_length=sequence_length,
#shuffle=True,
#batch_size=batch_size,

train_node_3 = keras.utils.timeseries_dataset_from_array(
    data_extraction_3[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=0,
    end_index=num_train_samples)

val_node_3 = keras.utils.timeseries_dataset_from_array(
    data_extraction_3[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples,
    end_index=num_train_samples + num_val_samples)

test_node_3 = keras.utils.timeseries_dataset_from_array(
    data_extraction_3[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples + num_val_samples)


#D4

# The manual route of node-construction
#training
data_extraction_4[:-delay]
targets=temperature[delay:],
start_index=0,
end_index=num_train_samples

#validation
data_extraction_4[:-delay]
targets=temperature[delay:],
start_index=num_train_samples,
end_index=num_train_samples + num_val_samples

#test
data_extraction_4[:-delay],
targets=temperature[delay:],
start_index=num_train_samples + num_val_samples

#sampling_rate=sampling_rate,
#sequence_length=sequence_length,
#shuffle=True,
#batch_size=batch_size,



# The keras built-in route of node-construction
train_node_4 = keras.utils.timeseries_dataset_from_array(
    data_extraction_4[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=0,
    end_index=num_train_samples)

val_node_4 = keras.utils.timeseries_dataset_from_array(
    data_extraction_4[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples,
    end_index=num_train_samples + num_val_samples)

test_node_4 = keras.utils.timeseries_dataset_from_array(
    data_extraction_4[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples + num_val_samples)


#D5

#training
data_extraction_5[:-delay]
targets=temperature[delay:],
start_index=0,
end_index=num_train_samples

#validation
data_extraction_5[:-delay]
targets=temperature[delay:],
start_index=num_train_samples,
end_index=num_train_samples + num_val_samples

#test
data_extraction_5[:-delay],
targets=temperature[delay:],
start_index=num_train_samples + num_val_samples

#sampling_rate=sampling_rate,
#sequence_length=sequence_length,
#shuffle=True,
#batch_size=batch_size,





train_node_5 = keras.utils.timeseries_dataset_from_array(
    data_extraction_5[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=0,
    end_index=num_train_samples)

val_node_5 = keras.utils.timeseries_dataset_from_array(
    data_extraction_5[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples,
    end_index=num_train_samples + num_val_samples)

test_node_5 = keras.utils.timeseries_dataset_from_array(
    data_extraction_5[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples + num_val_samples)

temperature = np.zeros((len(lines),))
raw_data = np.zeros((len(lines), len(header) - 1))
for i, line in enumerate(lines):
    values = [float(x) for x in line.split(",")[1:]]
    temperature[i] = values[1]
    raw_data[i, :] = values[:]

#sampling_rate = 6
#sequence_length = 120
#delay = sampling_rate * (sequence_length + 24 - 1)
#batch_size = 256
#n#um_train_samples = int(0.5 * len(raw_data))
#num_val_samples = int(0.25 * len(raw_data))
#num_test_samples = len(raw_data) - num_train_samples - num_val_samples
#raw_data of type ndarray

print(values)
print(temperature)
print(test_node_3)
print(test_node_4)
print(test_node_5)
exit()
##################################################################

# link_D1_tangent_layer1_batch encode in accessible data-structure
NETWORK_ORDER = 5
INTERLINK_DENSITY = 3
# D1

#link_D1_tangent_layer1_batch
#threelayerlink_bidirectional_tangent_storage = []
#[[[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]], [[],[],[],[],[]],[[],[],[],[],[]]], [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]], [[[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]],[[],[],[],[],[]],[]], [[],[],[],[],[]], [[],[],[],[],[]]]

# add 1 for suggestive storage-access
threelayerlink_bidirectional_tangent_storage = []
for i in range(INTERLINK_DENSITY + 1):
    threelayerlink_bidirectional_tangent_storage.append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NETWORK_ORDER + 1):
        threelayerlink_bidirectional_tangent_storage[i].append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NETWORK_ORDER + 1):
        for k in range(NETWORK_ORDER + 1):
            threelayerlink_bidirectional_tangent_storage[i][j].append([])
#print(threelayerlink_bidirectional_tangent_storage)    

#print(len(threelayerlink_bidirectional_tangent_storage))
#print(len(threelayerlink_bidirectional_tangent_storage[0]))
#print(len(threelayerlink_bidirectional_tangent_storage[0][0]))     

#link_D1_tangent_layer1_batch
#threelayerlink_bidirectional_tangent_storage = []
#[[[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]], [[],[],[],[],[]],[[],[],[],[],[]]], [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]], [[[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]],[[],[],[],[],[]],[]], [[],[],[],[],[]], [[],[],[],[],[]]]

# add 1 for suggestive storage-access
threelayerlink_bidirectional_bias_storage = []
for i in range(INTERLINK_DENSITY + 1):
    threelayerlink_bidirectional_bias_storage.append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NETWORK_ORDER + 1):
        threelayerlink_bidirectional_bias_storage[i].append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NETWORK_ORDER + 1):
        for k in range(NETWORK_ORDER + 1):
            threelayerlink_bidirectional_bias_storage[i][j].append([])
#print(threelayerlink_bidirectional_bias_storage) 

# Template Series Data of dimension approx. Boston-Dat
# Task: Intralink D1 - D5 by learning NN via series data. Search for exemplary series data
# Later, automate process of data-integration and capture <-> research avenue

#D1
# 420k entries

print(data_extraction_2.shape)
#train_node_1
#val_node_1
#test_node_1
#print(data_extraction_1.shape)

#D2

#train_node_2
#val_node_2
#test_node_2
print(data_extraction_2.shape)
print(data_extraction_2)
#D3
exit()
#train_node_3
#val_node_3
#test_node_3

#D4

#train_node_4
#val_node_4
#test_node_4

#D5

#train_node_5
#val_node_5
#test_node_5

# FIX INTRALINK DATA PROCESSING

## Catalogue of intralink-types 

# DENSE
print(data_extraction_1.shape)
print((sequence_length, data_extraction_1.shape[-1]))
#exit()
print("---------------------------------------------------------")
print("---------------------------------------------------------")

########################################################


# Either usual array or keras.util.timeseries

########################################################

train_dataset = keras.utils.timeseries_dataset_from_array(
    raw_data[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=0,
    end_index=num_train_samples)
val_dataset = keras.utils.timeseries_dataset_from_array(
    raw_data[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples,
    end_index=num_train_samples + num_val_samples)
test_dataset = keras.utils.timeseries_dataset_from_array(
    raw_data[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples + num_val_samples)

########################################################

#train_node_1
#train_node_1
#val_node_1
#test_node_1
print("--------------**********---------------------------------")
print("-----------------------**********----------------------")


inputs = keras.Input(shape=(sequence_length, raw_data.shape[-1]))
x = layers.Flatten()(inputs)
x = layers.Dense(16, activation="relu")(x)
outputs = layers.Dense(1)(x)
model = keras.Model(inputs, outputs)

callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
]

model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = model.fit(train_dataset,
 epochs=10,
 validation_data=val_dataset,
 callbacks=callbacks)
model = keras.models.load_model("jena_dense.keras")
print(f"Test MAE: {model.evaluate(test_dataset)[1]:.2f}")


exit()

print("---------------------------------------------------------")

inputs = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))
x = keras.layers.Flatten()(inputs)
x = keras.layers.Dense(16, activation="relu")(x)
outputs = keras.layers.Dense(1)(x)
model = keras.Model(inputs, outputs)

callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
]

model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = model.fit(train_node_1,
    epochs=10,
    validation_data=val_node_1,
    callbacks=callbacks)
model = keras.models.load_model("jena_dense.keras")
print(f"Test MAE: {model.evaluate(test_node_1)[1]:.2f}")

for i in range(len(model.get_weights())):
    print("---------------------------------------------------------")
    print(model.get_weights()[i])
    

print("---------------------------------------------------------")

# LSTM

from tensorflow import keras
from tensorflow.keras import layers
inputs = keras.Input(shape=(sequence_length, raw_data.shape[-1]))
x = layers.Flatten()(inputs)
x = layers.Dense(16, activation="relu")(x)
outputs = layers.Dense(1)(x)
model = keras.Model(inputs, outputs)
callbacks = [
 keras.callbacks.ModelCheckpoint("jena_dense.keras",
 save_best_only=True)
]
model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = model.fit(train_dataset,
    epochs=10,
    validation_data=val_dataset,
    callbacks=callbacks)
model = keras.models.load_model("jena_dense.keras")
print(f"Test MAE: {model.evaluate(test_dataset)[1]:.2f}")











#train_node_1
#val_node_1
#test_node_1

inputs = keras.Input(shape=data_extraction_1.shape[1])
x = keras.layers.Conv1D(8, 24, activation="relu")(inputs)
x = keras.layers.MaxPooling1D(2)(x)
x = keras.layers.Conv1D(8, 12, activation="relu")(x)
x = keras.layers.MaxPooling1D(2)(x)
x = keras.layers.Conv1D(8, 6, activation="relu")(x)
x = keras.layers.GlobalAveragePooling1D()(x)
outputs = keras.layers.Dense(1)(x)
model = keras.Model(inputs, outputs)
callbacks = [
    keras.callbacks.ModelCheckpoint("jena_conv.keras",
    save_best_only=True)
    ]
model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = model.fit(train_node_1,
    epochs=10,
    validation_data=val_node_1,
    callbacks=callbacks)
model = keras.models.load_model("jena_conv.keras")
print(f"Test MAE: {model.evaluate(test_node_1)[1]:.2f}")
print("---------------------------------------------------------")
print(model.get_weights())
print(len(model.get_weights()))
print("---------------------------------------------------------")
print(len(model.get_weights()))
print("---------------------------------------------------------")
for i in range(len(model.get_weights())):
    print("---------------------------------------------------------")
    print(model.get_weights()[i])
print("---------------------------------------------------------")



# 1Dconv

#train_node_1
#val_node_1
#test_node_1

inputs = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))
x = keras.layers.Conv1D(8, 24, activation="relu")(inputs)
x = keras.layers.MaxPooling1D(2)(x)
x = keras.layers.Conv1D(8, 12, activation="relu")(x)
x = keras.layers.MaxPooling1D(2)(x)
x = keras.layers.Conv1D(8, 6, activation="relu")(x)
x = keras.layers.GlobalAveragePooling1D()(x)
outputs = keras.layers.Dense(1)(x)
model = keras.Model(inputs, outputs)
callbacks = [
    keras.callbacks.ModelCheckpoint("jena_conv.keras",
    save_best_only=True)
    ]
model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = model.fit(train_node_1,
    epochs=10,
    validation_data=val_node_1,
    callbacks=callbacks)
model = keras.models.load_model("jena_conv.keras")
print(f"Test MAE: {model.evaluate(test_node_1)[1]:.2f}")
print("---------------------------------------------------------")
print(model.get_weights())
print(len(model.get_weights()))
print("---------------------------------------------------------")
print(len(model.get_weights()))
print("---------------------------------------------------------")
for i in range(len(model.get_weights())):
    print("---------------------------------------------------------")
    print(model.get_weights()[i])
print("---------------------------------------------------------")


# DENSE

print("---------------------------------------------------------")
print("---------------------------------------------------------")


#train_node_1
#val_node_1
#test_node_1

inputs = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))
x = keras.layers.Flatten()(inputs)
x = keras.layers.Dense(16, activation="relu")(x)
outputs = keras.layers.Dense(1)(x)
model = keras.Model(inputs, outputs)

callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
]
model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = model.fit(train_node_1,
 epochs=10,
 validation_data=val_node_1,
 callbacks=callbacks)
model = keras.models.load_model("jena_dense.keras")
print(f"Test MAE: {model.evaluate(test_node_1)[1]:.2f}")

for i in range(len(model.get_weights())):
    print("---------------------------------------------------------")
    print(model.get_weights()[i])

exit()

#print(419693)
#print(data_extraction_2.shape)
#print(data_extraction_3.shape)
#print(data_extraction_4.shape)
#print(data_extraction_5.shape)


# Time series data better, otherwise assume underlying unity in observation index
# D1

# labels are in fact targets
(train_data_1, train_labels_1), (test_data_1, test_labels_1) = keras.datasets.boston_housing.load_data()
train_data_1 = train_data_1[:,:10]
test_data_1 = test_data_1[:,:10]

print(train_data_1.shape)
print(test_data_1.shape)

#for k in range(NETWORK_ORDER):
#    threelayerlink_bidirectional_tangent_storage[k].append([])
#    print(threelayerlink_bidirectional_tangent_storage)

#threelayerlink_bidirectional_tangent_storage
#threelayerlink_tangent_storage[0][2].append(5)
#print(threelayerlink_tangent_storage)

#[[],[],[],[]]
#[]
# D2
#D3
#D4
#D5

################################################################################