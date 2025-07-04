##################################################################
#
# 
# Arch DL Starsystem, 5 Data-environments, bidirectional internode links, monodirectional intranode links, low-dimensional data (sampled by stratification)
# Computable implementation of sub-minimal scale
# Extent of inter-/ or intralink-complexity only due NN Specification.
# For considering effectivity of system over node-counts and stratified data, fix NN-link to dense
##################################################################
# Functionalize

# CHECK CODE FOR BUGS IN COMPUTATION



import keras
import numpy as np
import os
from tensorflow import keras
from tensorflow.keras import layers
import math
 

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

print(data_extraction_1_preprocess.shape)
print(data_extraction_2_preprocess.shape)
print(data_extraction_3_preprocess.shape)
print(data_extraction_4_preprocess.shape)
print(data_extraction_5_preprocess.shape)

num_train_samples = int(0.5 * len(raw_data))
num_val_samples = int(0.25 * len(raw_data))
num_test_samples = len(raw_data) - num_train_samples - num_val_samples
duration = len(raw_data) - delay

# TWEAK SYSTEM PARAMETERS FOR OPTIMAL INFERENCE
# FOR CONSTRUCTION
# TWEAK PARAMETERS UNTIL STARLINK SUPREMACY
INTRALINK_N = 130 # TO BE TWEAKED, VARIABILITY DUE TO DURATION EXPOSURE, MAKE LARGER MAGNITUDES POSSIBLE
NETWORK_ORDER = 5
INTERLINK_DENSITY = 3


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

volume_tracker = 0           
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NETWORK_ORDER + 1):
        for k in range(NETWORK_ORDER + 1):
            volume_tracker += 1
            print(volume_tracker)
 #           threelayerlink_bidirectional_tangent_storage[i][j][k]

 
#for i in range(INTERLINK_DENSITY + 1):
#    for j in range(NETWORK_ORDER + 1):
#        for k in range(NETWORK_ORDER + 1):
#            p#rint(threelayerlink_bidirectional_tangent_storage[i][j][k])
            
#4 * 6 * 6      
#print(threelayerlink_bidirectional_tangent_storage)  
print(volume_tracker)  
#exit()
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

# INTRALINK_N loop

for i in range(INTRALINK_N):
    
    print("Intralink loop 2")
    
    # INTRALINK_N 
    data_extraction_1 = data_extraction_1_preprocess[math.floor(i * duration/INTRALINK_N) : math.floor((i + 1) * duration/INTRALINK_N)]
    data_extraction_2 = data_extraction_2_preprocess[math.floor(i * duration/INTRALINK_N) : math.floor((i + 1) * duration/INTRALINK_N)]
    data_extraction_3 = data_extraction_3_preprocess[math.floor(i * duration/INTRALINK_N) : math.floor((i + 1) * duration/INTRALINK_N)]
    data_extraction_4 = data_extraction_4_preprocess[math.floor(i * duration/INTRALINK_N) : math.floor((i + 1) * duration/INTRALINK_N)]
    data_extraction_5 = data_extraction_5_preprocess[math.floor(i * duration/INTRALINK_N) : math.floor((i + 1) * duration/INTRALINK_N)]
    temperature_extraction = temperature[math.floor(i * duration/INTRALINK_N) : math.floor((i + 1) * duration/INTRALINK_N)]
    
    print(len(data_extraction_1))
    print(len(data_extraction_2))
    print(len(data_extraction_3))
    print(len(data_extraction_4))
    print(len(data_extraction_5))
    

    # retweak
    num_train_samples = math.floor(0.5 * duration/INTRALINK_N)
    num_val_samples = math.floor(0.25 * duration/INTRALINK_N)
    num_test_samples = math.floor(0.25 * duration/INTRALINK_N)
    #batch_size = 10

    #D1
    train_node_1 = keras.utils.timeseries_dataset_from_array(
        data_extraction_1,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=0,
        end_index=num_train_samples) #duration/INTRALINK_N

    val_node_1 = keras.utils.timeseries_dataset_from_array(
        data_extraction_1,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples,
        end_index=num_train_samples + num_val_samples)

    test_node_1 = keras.utils.timeseries_dataset_from_array(
        data_extraction_1,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples + num_val_samples)

    #D2
    train_node_2 = keras.utils.timeseries_dataset_from_array(
        data_extraction_2,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=0,
        end_index=num_train_samples)

    val_node_2 = keras.utils.timeseries_dataset_from_array(
        data_extraction_2,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples,
        end_index=num_train_samples + num_val_samples)

    test_node_2 = keras.utils.timeseries_dataset_from_array(
        data_extraction_2,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples + num_val_samples)

    #D3
    train_node_3 = keras.utils.timeseries_dataset_from_array(
        data_extraction_3,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=0,
        end_index=num_train_samples)

    val_node_3 = keras.utils.timeseries_dataset_from_array(
        data_extraction_3,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples,
        end_index=num_train_samples + num_val_samples)

    test_node_3 = keras.utils.timeseries_dataset_from_array(
        data_extraction_3,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples + num_val_samples)


    #D4
    train_node_4 = keras.utils.timeseries_dataset_from_array(
        data_extraction_4,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=0,
        end_index=num_train_samples)

    val_node_4 = keras.utils.timeseries_dataset_from_array(
        data_extraction_4,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples,
        end_index=num_train_samples + num_val_samples)

    test_node_4 = keras.utils.timeseries_dataset_from_array(
        data_extraction_4,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples + num_val_samples)


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


    #sampling_rate = 6
    #sequence_length = 120
    #delay = sampling_rate * (sequence_length + 24 - 1)
    #batch_size = 256
    #n#um_train_samples = int(0.5 * len(raw_data))
    #num_val_samples = int(0.25 * len(raw_data))
    #num_test_samples = len(raw_data) - num_train_samples - num_val_samples
    #raw_data of type ndarray

    #print(values)
    #print(temperature)
    #print(test_node_3)
    #print(test_node_4)
    #print(test_node_5)
    #exit()

    ##################################################################
    ##################################################################
    ##################################################################

    # link_D1_tangent_layer1_batch encode in accessible data-structure

    # D1
    #link_D1_tangent_layer1_batch
    #threelayerlink_bidirectional_tangent_storage = []
    #[[[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]], [[],[],[],[],[]],[[],[],[],[],[]]], [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]], [[[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]],[[],[],[],[],[]],[]], [[],[],[],[],[]], [[],[],[],[],[]]]

    # Construct threelayerlink_node_intratangent_storage
    # Construct threelayerlink_node_intrabias_storage

    # Template Series Data of dimension approx. Boston-Dat
    # Task: Intralink D1 - D5 by learning NN via series data. Search for exemplary series data
    # Later, automate process of data-integration and capture <-> research avenue
    # FIX INTRALINK DATA PROCESSING: FIXED
    # Catalogue of intralink-types


    # STORE WEIGHTS IN threelayerlink_bidirectional_tangent_storage AND threelayerlink_bidirectional_bias_storage
    #for i in range(1, INTERLINK_DENSITY):
    #    threelayerlink_bidirectional_tangent_storage[i][j][k].append(Intra_D1._layers[1].get_weights()[0])
    #threelayerlink_bidirectional_tangent_storage[1][1][1].append(Intra_D1._layers[1].get_weights()[0])          
    #threelayerlink_bidirectional_tangent_storage[i][j][k].append(Intra_D1._layers[1].get_weights()[0])           
    #threelayerlink_bidirectional_tangent_storage[2][1][1].append(Intra_D1._layers[2].get_weights()[0])
    #threelayerlink_bidirectional_tangent_storage[3][1][1].append(Intra_D1._layers[3].get_weights()[0])



    #testlink = keras.models.Sequential()
    #testlink.add(keras.Input(shape=(sequence_length, data_extraction_1.shape[-1])))
    #testlink.add(keras.layers.Dense(16, activation='relu',))
    #testlink.add(keras.layers.Dense(16, activation='relu'))
    #testlink.add(keras.layers.Dense(1))
    #testlink.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    #history = testlink.fit(train_node_1,
    #    epochs=10,
    #    validation_data=val_node_1)
    ##print(testlink.layers[0].get_weights()[0])
    #p#rint(testlink.layers[0].get_weights()[1])

    #print(testlink.summary)
    #print(testlink)

    #inputs = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))
    #x = layers.Dense(16, activation="relu")(inputs)
    #x# = layers.Dense(16, activation="relu")(inputs)
    #outputs = layers.Dense(1)(x)
    #Intra_D1 = keras.Model(inputs, outputs)
    #callbacks = [
    #keras.callbacks.ModelCheckpoint("jena_dense.keras",
    # save_best_only=True)
    #]
    #Intra_D1.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    #history = Intra_D1.fit(train_node_1,
    #  epochs=10,
    #   validation_data=val_node_1,
    #    callbacks=callbacks)
    #Intra_D1 = keras.models.load_model("jena_dense.keras")
    #print(f"Test MAE: {Intra_D1.evaluate(test_node_1)[1]:.2f}")

    #print(Intra_D1.layers)
    #print(Intra_D1.layers[0].get_weights()[0])

    #exit()



    ################################################################################
    print("----------------^^^^^^^^^^^^^^^----------------------")

    # DENSE
    #exit()
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")

    ##################################################################

    print("--------------**********---------------------------------")
    print("-----------------------**********----------------------")


    ##################################################################
    # D1 DENSE Intralink-Learning
    ##################################################################

    print("----------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

        
    inputs = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))
    x = layers.Dense(16, activation="relu")(inputs)
    x = layers.Dense(16, activation="relu")(x)
    outputs = layers.Dense(1)(x)
    Intra_D1 = keras.Model(inputs, outputs)
    callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
    ]
    Intra_D1.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    history = Intra_D1.fit(train_node_1,
        epochs=1,
        validation_data=val_node_1,
        callbacks=callbacks)
    Intra_D1 = keras.models.load_model("jena_dense.keras")
    print(f"Test MAE: {Intra_D1.evaluate(test_node_1)[1]:.2f}")

    for j in range(1, INTERLINK_DENSITY + 1):
        #print(i)
        threelayerlink_bidirectional_tangent_storage[j][1][1].append(Intra_D1._layers[j].get_weights()[0])          
        threelayerlink_bidirectional_bias_storage[j][1][1].append(Intra_D1._layers[j].get_weights()[1])

    print("D1--------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")
    
    print(threelayerlink_bidirectional_tangent_storage[1][1][1][0].shape)
    print(threelayerlink_bidirectional_tangent_storage[2][1][1][0].shape)
    print(threelayerlink_bidirectional_tangent_storage[3][1][1][0].shape)
    
    print(threelayerlink_bidirectional_bias_storage[2][1][1][0].shape)
    print(threelayerlink_bidirectional_bias_storage[1][1][1][0].shape)
    print(threelayerlink_bidirectional_bias_storage[3][1][1][0].shape)
    

    ################################################################################
    # D2 DENSE Intralink-Learning
    ################################################################################

    print("----------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

    inputs = keras.Input(shape=(sequence_length, data_extraction_2.shape[-1]))
    x = layers.Dense(16, activation="relu")(inputs)
    x = layers.Dense(16, activation="relu")(x)
    outputs = layers.Dense(1)(x)
    Intra_D2 = keras.Model(inputs, outputs)
    callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
    ]
    Intra_D2.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    history = Intra_D2.fit(train_node_2,
        epochs=1,
        validation_data=val_node_2,
        callbacks=callbacks)
    Intra_D2 = keras.models.load_model("jena_dense.keras")
  #  print(f"Test MAE: {Intra_D1.evaluate(test_node_2)[1]:.2f}")

    for j in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[j][2][2].append(np.array(Intra_D2._layers[j].get_weights()[0]))        
        threelayerlink_bidirectional_bias_storage[j][2][2].append(np.array(Intra_D2._layers[j].get_weights()[1]))

    print("D2--------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

    ################################################################################
    # D3 DENSE Intralink-Learning
    ################################################################################

    print("----------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

    inputs = keras.Input(shape=(sequence_length, data_extraction_3.shape[-1]))
    x = layers.Dense(16, activation="relu")(inputs)
    x = layers.Dense(16, activation="relu")(x)
    outputs = layers.Dense(1)(x)
    Intra_D3 = keras.Model(inputs, outputs)
    callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
    ]
    Intra_D3.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    history = Intra_D1.fit(train_node_3,
        epochs=1,
        validation_data=val_node_3,
        callbacks=callbacks)
    Intra_D3 = keras.models.load_model("jena_dense.keras")
    print(f"Test MAE: {Intra_D3.evaluate(test_node_3)[1]:.2f}")

    for j in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[j][3][3].append(np.array(Intra_D3._layers[j].get_weights()[0]))          
        threelayerlink_bidirectional_bias_storage[j][3][3].append(np.array(Intra_D3._layers[j].get_weights()[1]))

    print("D3--------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

    ################################################################################
    # D4 DENSE Intralink-Learning
    ################################################################################
    print("----------------*******************----------------------")

    print("----------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

    inputs = keras.Input(shape=(sequence_length, data_extraction_4.shape[-1]))
    x = layers.Dense(16, activation="relu")(inputs)
    x = layers.Dense(16, activation="relu")(x)
    outputs = layers.Dense(1)(x)
    Intra_D4 = keras.Model(inputs, outputs)
    callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
    ]
    Intra_D4.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    history = Intra_D1.fit(train_node_4,
        epochs=1,
        validation_data=val_node_4,
        callbacks=callbacks)
    Intra_D4 = keras.models.load_model("jena_dense.keras")
    print(f"Test MAE: {Intra_D3.evaluate(test_node_4)[1]:.2f}")

    for j in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[j][4][4].append(np.array(Intra_D4._layers[j].get_weights()[0]))          
        threelayerlink_bidirectional_bias_storage[j][4][4].append(np.array(Intra_D4._layers[j].get_weights()[1]))

    print("D4--------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

    ################################################################################
    # D5 DENSE Intralink-Learning
    ################################################################################

    print("----------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

    inputs = keras.Input(shape=(sequence_length, data_extraction_5.shape[-1]))
    x = layers.Dense(16, activation="relu")(inputs)
    x = layers.Dense(16, activation="relu")(x)
    outputs = layers.Dense(1)(x)
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
        threelayerlink_bidirectional_tangent_storage[j][5][5].append(np.array(Intra_D5._layers[j].get_weights()[0]))          
        threelayerlink_bidirectional_bias_storage[j][5][5].append(np.array(Intra_D5._layers[j].get_weights()[1]))

    print("D5--------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")
    

################################################################################

#print(threelayerlink_bidirectional_tangent_storage[1,5,5].shape)
#print(threelayerlink_bidirectional_tangent_storage[1,5,5].shape)
#p#rint(threelayerlink_bidirectional_bias_storage[1,5,5].shape)
#print(threelayerlink_bidirectional_bias_storage[1,5,5].shape)

################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################
################################################################################
# REWRITE LATER
################################################################################
################################################################################
# INTERLINK CONSTRUCTION, follows from the above
################################################################################
################################################################################
# DEBUG MANUAL MATRIX COMPUTATION FOR FINAL INFERENCE
################################################################################

for k in range(1, INTERLINK_DENSITY + 1):
    for i in range(1, NETWORK_ORDER + 1):
        for j in range(1, NETWORK_ORDER + 1):
        
            # Node i -> Node j, Layer k
            print("Start INTERLINK CONSTRUCTION")
            print(k)
            print(i)
            print(j)
            # layer 3, node 1 -> node 2 no entry
            
            #print(len(threelayerlink_bidirectional_tangent_storage[k][i][i]))
            #print(len(threelayerlink_bidirectional_tangent_storage[k][j][j])) # Storage Size INTRALINK_N
            #print(len(threelayerlink_bidirectional_bias_storage[k][i][i]))
            #print(len(threelayerlink_bidirectional_bias_storage[k][j][j]))
            
            #print("Start CONSTRUCTION auxilliary")
            #for m in range(1, 4):
            #    print(threelayerlink_bidirectional_tangent_storage[k][1][1][m].shape)
            
            if i == j:
                continue

            input_tangent_size = threelayerlink_bidirectional_tangent_storage[k][i][i][0].shape
            output_tangent_size = threelayerlink_bidirectional_tangent_storage[k][j][j][0].shape
            input_bias_size = threelayerlink_bidirectional_bias_storage[k][i][i][0].shape
            output_bias_size = threelayerlink_bidirectional_bias_storage[k][j][j][0].shape
            
            #print(input_tangent_size)
            #print(output_tangent_size)
            #print(input_bias_size)
            #print(output_bias_size)

            Inter_D1_D2_tangent = keras.models.Sequential()
            Inter_D1_D2_tangent.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
            Inter_D1_D2_tangent.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
            Inter_D1_D2_tangent.add(keras.layers.Dense(output_tangent_size[1]))
            Inter_D1_D2_tangent.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

            Inter_D1_D2_bias = keras.models.Sequential()
            Inter_D1_D2_bias.add(keras.layers.Dense(output_bias_size[0]))
            Inter_D1_D2_bias.add(keras.layers.Dense(output_bias_size[0]))
            Inter_D1_D2_bias.add(keras.layers.Dense(output_bias_size[0]))
            Inter_D1_D2_bias.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

            #print(len(threelayerlink_bidirectional_tangent_storage[k][i][i]))
            #print(len(threelayerlink_bidirectional_tangent_storage[k][j][j]))
            #print(len(threelayerlink_bidirectional_tangent_storage[k][i][i]))
            #print(threelayerlink_bidirectional_tangent_storage[k][i][i].shape)
            #print(threelayerlink_bidirectional_tangent_storage[k][j][j].shape)
            #print(threelayerlink_bidirectional_tangent_storage[k][i][i].shape)
            
            threelayerlink_bidirectional_tangent_storage_kii = np.array(threelayerlink_bidirectional_tangent_storage[k][i][i])
            threelayerlink_bidirectional_tangent_storage_kjj = np.array(threelayerlink_bidirectional_tangent_storage[k][j][j])
            
            print("==========================================================================================")
            print(threelayerlink_bidirectional_tangent_storage_kii.shape)
            print(threelayerlink_bidirectional_tangent_storage_kjj.shape)
            print("==========================================================================================")

            Inter_D1_D2_tangent.fit(threelayerlink_bidirectional_tangent_storage_kii, threelayerlink_bidirectional_tangent_storage_kjj, epochs=5, batch_size=128)
            Emergent_Inter_D1_D2_tangent = Inter_D1_D2_tangent.predict(threelayerlink_bidirectional_tangent_storage_kii)
            print(type(Emergent_Inter_D1_D2_tangent[0]))
            threelayerlink_bidirectional_tangent_storage[k][i][j].append(Emergent_Inter_D1_D2_tangent[0])
            
            threelayerlink_bidirectional_bias_storage_kii = np.array(threelayerlink_bidirectional_bias_storage[k][i][i])
            threelayerlink_bidirectional_bias_storage_kjj = np.array(threelayerlink_bidirectional_bias_storage[k][j][j])
            
            print("==========================================================================================")
            print(threelayerlink_bidirectional_bias_storage_kii.shape)
            print(threelayerlink_bidirectional_bias_storage_kjj.shape)
            print("==========================================================================================")

            Inter_D1_D2_bias.fit(threelayerlink_bidirectional_bias_storage_kii, threelayerlink_bidirectional_bias_storage_kjj, epochs=5, batch_size=128)
            Emergent_Inter_D1_D2_bias  = Inter_D1_D2_bias.predict(threelayerlink_bidirectional_bias_storage_kii)
            print(type(Emergent_Inter_D1_D2_bias[0]))
            threelayerlink_bidirectional_bias_storage[k][i][j].append(Emergent_Inter_D1_D2_bias[0])
            

            
            #exit()
       #     print(threelayerlink_bidirectional_tangent_storage_kii.shape)
       #     print(threelayerlink_bidirectional_tangent_storage_kjj.shape)
       #     print(threelayerlink_bidirectional_bias_storage_kii.shape)
       #     print(threelayerlink_bidirectional_bias_storage_kjj.shape)
       
       
print("==========================================================================================")
print("INTERLINK")
print(threelayerlink_bidirectional_tangent_storage[1][1][2][0].shape)
print(threelayerlink_bidirectional_tangent_storage[2][1][2][0].shape)
print(threelayerlink_bidirectional_tangent_storage[3][1][2][0].shape)

print(threelayerlink_bidirectional_bias_storage[1][1][2][0].shape)
print(threelayerlink_bidirectional_bias_storage[2][1][2][0].shape)
print(threelayerlink_bidirectional_bias_storage[3][1][2][0].shape)

print("INTRALINK")
print(threelayerlink_bidirectional_tangent_storage[1][1][1][0].shape)
print(threelayerlink_bidirectional_tangent_storage[2][1][1][0].shape)
print(threelayerlink_bidirectional_tangent_storage[3][1][1][0].shape)

print(threelayerlink_bidirectional_bias_storage[1][1][1][0].shape)
print(threelayerlink_bidirectional_bias_storage[2][1][1][0].shape)
print(threelayerlink_bidirectional_bias_storage[3][1][1][0].shape)
print("==========================================================================================")
################################################################################

# RETRAIN ALL INTRALINK WITH DATA FROM FULL EXPOSURE DURATION 
# AFTERWARDS, PERFORM NEURALNET INFERENCE
# UNDER CONSTRUCTION, VIA Keras Class Sequential if necessary

#Intra_D1inference = Intra_D1.predict(data_extraction_1_preprocess)
#Intra_D2inference = Intra_D2.predict(data_extraction_2_preprocess)
#Intra_D3inference = Intra_D3.predict(data_extraction_3_preprocess)
#Intra_D4inference = Intra_D4.predict(data_extraction_4_preprocess)
#Intra_D5inference = Intra_D5.predict(data_extraction_5_preprocess)
#FROM INTRALINK TO INTRALINK VIA INTERLINK
#INTRALINK DIMENSIONS

# Weight dimensions tranposed by use of Keras API (?)
#(2, 16)
#(16, 16)
#(16, 1)
#(16,)
#(16,)
#(1,)

#INTERLINK FOLLOWS INTRALINK DIMENSIONS

#(2, 16)
#(16, 16)
#(16, 1)
#(16,)
#(16,)
#(1,)

#(2, 16)
#(16, 16)
#(16, 1)
#(16,)
#(16,)
#(1,)

################################################################################
######## MANUAL MATRIX COMPUTATION INITIALIZATION #############################################

inference_starlink = []
for i in range(0, NETWORK_ORDER + 1):
    inference_starlink.append([])
    for j in range(0, NETWORK_ORDER + 1):
        inference_starlink[i].append([])
        
# inference_starlink = np.eye(NETWORK_ORDER + 1)
inference_NeuralNet = np.eye(NETWORK_ORDER + 1)
data_extraction_postprocess = []
data_extraction_postprocess.append([])
data_extraction_postprocess.append(data_extraction_1_preprocess)
data_extraction_postprocess.append(data_extraction_2_preprocess)
data_extraction_postprocess.append(data_extraction_3_preprocess)
data_extraction_postprocess.append(data_extraction_4_preprocess)
data_extraction_postprocess.append(data_extraction_5_preprocess)

#################################################################################

# RETRAIN ALL INTRALINK WITH DATA FROM FULL EXPOSURE DURATION 
# AFTERWARDS, PERFORM NEURALNET INFERENCE
# *** UNDER CONSTRUCTION ***

#Intra_D1inference = Intra_D1.predict(data_extraction_1_preprocess)
#Intra_D2inference = Intra_D2.predict(data_extraction_2_preprocess)
#Intra_D3inference = Intra_D3.predict(data_extraction_3_preprocess)
#Intra_D4inference = Intra_D4.predict(data_extraction_4_preprocess)
#Intra_D5inference = Intra_D5.predict(data_extraction_5_preprocess)

#Inference_NeuralNet.append(Intra_D1inference)
#Inference_NeuralNet.append(Intra_D2inference)
#Inference_NeuralNet.append(Intra_D3inference)
#Inference_NeuralNet.append(Intra_D4inference)
#Inference_NeuralNet.append(Intra_D5inference)

# DETOUR RETRAIN ALL INTRALINK WITH DATA FROM FULL EXPOSURE DURATION WITH INTRALINK KERAS SEQUENTIAL 

#################################################################################

Inference_NeuralNet = []
Inference_NeuralNet.append(0)

SequentIntra_D1 = keras.models.Sequential()
SequentIntra_D1.add(keras.layers.Dense(16, activation='relu'))
SequentIntra_D1.add(keras.layers.Dense(16, activation='relu'))
SequentIntra_D1.add(keras.layers.Dense(1))
SequentIntra_D1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
SequentIntra_D1.fit(data_extraction_1_preprocess, temperature_extraction_preprocess, epochs=5, batch_size=128)
Intra_D1NeuralNetInference = SequentIntra_D1.predict(data_extraction_1_preprocess)
Intra_D1NeuralNetInference = Intra_D1NeuralNetInference[0]
Inference_NeuralNet.append(Intra_D1NeuralNetInference)

SequentIntra_D2 = keras.models.Sequential()
SequentIntra_D2.add(keras.layers.Dense(16, activation='relu'))
SequentIntra_D2.add(keras.layers.Dense(16, activation='relu'))
SequentIntra_D2.add(keras.layers.Dense(1))
SequentIntra_D2.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
SequentIntra_D2.fit(data_extraction_2_preprocess, temperature_extraction_preprocess, epochs=5, batch_size=128)
Intra_D2NeuralNetInference = SequentIntra_D2.predict(data_extraction_2_preprocess)
Intra_D2NeuralNetInference = Intra_D2NeuralNetInference[0]
Inference_NeuralNet.append(Intra_D2NeuralNetInference)

SequentIntra_D3 = keras.models.Sequential()
SequentIntra_D3.add(keras.layers.Dense(16, activation='relu'))
SequentIntra_D3.add(keras.layers.Dense(16, activation='relu'))
SequentIntra_D3.add(keras.layers.Dense(1))
SequentIntra_D3.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
SequentIntra_D3.fit(data_extraction_5_preprocess, temperature_extraction_preprocess, epochs=5, batch_size=128)
Intra_D3NeuralNetInference = SequentIntra_D3.predict(data_extraction_5_preprocess)
Intra_D3NeuralNetInference = Intra_D3NeuralNetInference[0]
Inference_NeuralNet.append(Intra_D3NeuralNetInference)

SequentIntra_D4 = keras.models.Sequential()
SequentIntra_D4.add(keras.layers.Dense(16, activation='relu'))
SequentIntra_D4.add(keras.layers.Dense(16, activation='relu'))
SequentIntra_D4.add(keras.layers.Dense(1))
SequentIntra_D4.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
SequentIntra_D4.fit(data_extraction_4_preprocess, temperature_extraction_preprocess, epochs=5, batch_size=128)
Intra_D4NeuralNet = SequentIntra_D4.predict(data_extraction_5_preprocess)
Intra_D4NeuralNetInference = Intra_D4NeuralNet[0]
Inference_NeuralNet.append(Intra_D4NeuralNetInference)

SequentIntra_D5 = keras.models.Sequential()
SequentIntra_D5.add(keras.layers.Dense(16, activation='relu',))
SequentIntra_D5.add(keras.layers.Dense(16, activation='relu',))
SequentIntra_D5.add(keras.layers.Dense(1))
SequentIntra_D5.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
SequentIntra_D5.fit(data_extraction_5_preprocess, temperature_extraction_preprocess, epochs=5, batch_size=128)
Intra_D5NeuralNetInference = SequentIntra_D5.predict(data_extraction_5_preprocess)
Intra_D5NeuralNetInference = Intra_D5NeuralNetInference[0]
Inference_NeuralNet.append(Intra_D5NeuralNetInference)

#################################################################################
######## MANUAL MATRIX COMPUTATION #############################################

def relu(x):
    return np.maximum(0, x)

for i in range(1, NETWORK_ORDER + 1):
    for j in range(1, NETWORK_ORDER + 1):
        print("inference_starlink under computation" + str(i) + "*" + str(j) + "/" + str(NETWORK_ORDER) + "*" + str(NETWORK_ORDER))
        for m in range(duration):
            sample_data = data_extraction_postprocess[j][m]
            sub_result1 = relu((threelayerlink_bidirectional_tangent_storage[1][i][j][0].transpose() @ sample_data) + threelayerlink_bidirectional_bias_storage[1][i][j][0])
            sub_result2 = relu((threelayerlink_bidirectional_tangent_storage[2][i][j][0].transpose() @ sub_result1) + threelayerlink_bidirectional_bias_storage[2][i][j][0])
            sub_result3 = ((threelayerlink_bidirectional_tangent_storage[3][i][j][0].transpose() @ sub_result2) + threelayerlink_bidirectional_bias_storage[3][i][j][0])
            print(sub_result3)
            print(type(sub_result3))
            inference_starlink[i][j].append(sub_result3[0])
        
        inference_starlink[i][j] = np.array(inference_starlink[i][j])
        print(np.sqrt(np.mean(np.square(inference_starlink[i][j] - temperature_extraction_preprocess))))

#print(np.sqrt(np.mean(np.square((inference_starlink[2][2] - temperature_extraction_preprocess)))))
print("**************************************************************************************")


for i in range(1, NETWORK_ORDER + 1):
    for j in range(1, NETWORK_ORDER + 1):
        if i == j:
            continue
        print("Machine Inference Starlink: D" + str(i)+ " -> D" + str(j))############################################################################
        print(np.sqrt(np.mean(np.square(np.array(inference_starlink[j][i]) - temperature_extraction_preprocess))))
        print("Machine Inference NeuralNet: D" + str(j))
        Inference_NeuralNet[j] = np.array(Inference_NeuralNet[j])
        print(np.sqrt(np.mean(np.square(temperature_extraction_preprocess - Inference_NeuralNet[j]))))

################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################

exit()

################################################################################
# SUGGESTIVE ROUTE:
# ISOLATE ONE DATA-EVIRONMENT
# INFER DATA-ENVIRONMENT X FROM ALL OTHER DATA-ENVIRONMENTS AND MINIMAL EXPOSURE TO DATA-ENVIRONMENT X
################################################################################


## Debugging due
# D2 intralink undiscovered 
# D1 intralink computed
# D2 target inference inquired
# D2 partial data observable
# D1 -> D2 interlink for full clarivoyance D2

# Node Generator essential

#threelayerlink_bidirectional_bias_storage          

# Seek general structure for quick construction of all interlinks
# Reconsider terminologies

# D2 -> D1

#   link_D2D1_tangent1 = keras.models.Sequential()
#   link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
#   link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
#   link_D2D1_tangent1.add(keras.layers.Dense(output_tangent_size[1]))
#   link_D2D1_tangent1.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

# D1 -> D2
# D1 -> D3
# D1 -> D4
# D1 -> D5

# D2 -> D1
# D2 -> D3
# D2 -> D4
# D2 -> D5

# D3 -> D1
# D3 -> D2
# D3 -> D4
# D3 -> D5

# D4 -> D1
# D4 -> D2
# D4 -> D3
# D4 -> D5

# D5 -> D1
# D5 -> D2
# D5 -> D3
# D5 -> D4

#inputs = keras.Input(shape=(sequence_length, raw_data.shape[-1]))
#x = layers.Flatten()(inputs)
#x = layers.Dense(16, activation="relu")(x)
#outputs = layers.Dense(1)(x)
#model = keras.Model(inputs, outputs)

#callbacks = [
#    keras.callbacks.ModelCheckpoint("jena_dense.keras",
#    save_best_only=True)
#]

#model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
#history = model.fit(train_dataset,
#epochs=10,
#validation_data=val_dataset,
#callbacks=callbacks)
#model = keras.models.load_model("jena_dense.keras")
#print(f"Test MAE: {model.evaluate(test_dataset)[1]:.2f}")


#exit()


################################################################################




exit()

print("---------------------------------------------------------")

inputs = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))
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

# CONV1D Intralink-Learner

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



# LSTM WORKS!
exit()
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




exit()


inputs = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))
x = layers.Dense(16, activation="relu")(x)
outputs = layers.Dense(1)(x)
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

print("--------------**********---------------------------------")
print("-----------------------**********----------------------")
print("---------------------------------------------------------")





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



M = []


for i in range(3):
    M.append([])
    for j in range(3):
        M.append[i]([1])
        

