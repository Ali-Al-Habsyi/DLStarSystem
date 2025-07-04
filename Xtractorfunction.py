################################################################################
#
# SUGGESTIVE ROUTE:
# ISOLATE ONE DATA-EVIRONMENT
# INFER DATA-ENVIRONMENT X FROM ALL OTHER DATA-ENVIRONMENTS AND MINIMAL EXPOSURE TO DATA-ENVIRONMENT X
#
################################################################################

################################################################################
# INIATIALIZE MINIMAL INTERLINK-MERGE OVER FULL COMBINATORIC SPECTRUM
################################################################################

# USUAL STARLINKS
# D1 -> D5
# D2 -> D5
# D3 -> D5
# D4 -> D5

# COMBINATORIC INTEGRATION
# D1, D2 -> D5
# D2, D3 -> D5
# D2, D4 -> D5
# D4, D3 -> D5
#... (12 TOTAL COMBINATIONS)
# D1, D2, D4 -> D5
# D3, D2, D4 -> D5
# D1, D2, D4 -> D5
# D1, D2, D3 -> D5
# D3, D1, D4 -> D5
#... (4 TOTAL COMBINATIONS)
# D1, D2, D3, D4 -> D5

# DEVELOP VARIANTS OF COMBINATORIC INTEGRATION
# VARIANT 1
################################################################################
# LOAD PRE-COMPUTED LINKS
################################################################################
##################################################################
# NODE-ENVIRONMENT PROCEDURE OF DOWNLOAD (License: Keras Developer)
##################################################################


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
INTRALINK_N = 1 # TO BE TWEAKED, VARIABILITY DUE TO DURATION EXPOSURE, MAKE LARGER MAGNITUDES POSSIBLE
NETWORK_ORDER = 5
INTERLINK_DENSITY = 3



# add 1 for suggestive storage-access
threelayerlink_bidirectional_tangent_storage = []
threelayerlink_bidirectional_bias_storage = []
for i in range(INTERLINK_DENSITY + 1):
    threelayerlink_bidirectional_tangent_storage.append([])
    threelayerlink_bidirectional_bias_storage.append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NETWORK_ORDER + 1):
        threelayerlink_bidirectional_tangent_storage[i].append([])
        threelayerlink_bidirectional_bias_storage[i].append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NETWORK_ORDER + 1):
        for k in range(NETWORK_ORDER + 1):
            threelayerlink_bidirectional_tangent_storage[i][j].append([])
            threelayerlink_bidirectional_bias_storage[i][j].append([])


volume_tracker = 0           
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NETWORK_ORDER + 1):
        for k in range(NETWORK_ORDER + 1):
            volume_tracker += 1
            print(volume_tracker)
 #           threelayerlink_bidirectional_tangent_storage[i][j][k]

 
 #threelayerlink_bidirectional_tangentINTERLINK_storage
 #threelayerlink_bidirectional_biasINTERLINK_storage
 
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
    # D1, D2 -> D5 DENSE INTERLINK-CONSTRUCTION
    ################################################################################

    print("----------------*******************----------------------")
    print("----------------*******************----------------------")
    print("----------------*******************----------------------")

    inputs1 = keras.Input(shape=(sequence_length, data_extraction_2.shape[-1]))
    inputs2 = keras.Input(shape=(sequence_length, data_extraction_2.shape[-1]))
    
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

    for j in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[j][2][2].append(np.array(Intra_D2._layers[j].get_weights()[0]))        
        threelayerlink_bidirectional_bias_storage[j][2][2].append(np.array(Intra_D2._layers[j].get_weights()[1]))
        
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
        threelayerlink_bidirectional_tangent_storage[j][5][5].append(np.array(Intra_D5._layers[j].get_weights()[0]))  # j-1        
        threelayerlink_bidirectional_bias_storage[j][5][5].append(np.array(Intra_D5._layers[j].get_weights()[1]))
        
        
        print(Intra_D5._layers[1].get_weights()[1])

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
# EXTEND BY MERGED INTERLINKS
################################################################################
################################################################################
# DEBUG MANUAL MATRIX COMPUTATION FOR FINAL INFERENCE
################################################################################

################################################################################
# ASSUME GIVEN INTRA INTER AND MULTIPLE NODES D1 D2

# FULL COMPLETE COMBINTORIC INTEGRATION VIA MERGED NEURALNET
# D1, D2 --> D5 VIA MERGED INTRALINKS IF VIA MERGED NEURALNET ***
# COLLECT INTRALINKS D1 D2 --> INPUT FOR MULTI-INPUT MONO-OUTPUT 
################################################################################






print(Intra_D5._layers[1].get_weights()[1])
print(len(Intra_D5._layers[1].get_weights()[1]))

print(len(threelayerlink_bidirectional_tangent_storage[1][5][5][0]))
print(threelayerlink_bidirectional_tangent_storage[1][5][5][0])

output_tangent_size = threelayerlink_bidirectional_tangent_storage[1][5][5][0]

#print(len(Intra_D5._layers[1].get_weights()[0]))

print("------------------------------------------")
print(len(Intra_D5._layers))

print("------------------------------------------")
print(len(Intra_D5._layers[1].get_weights()[0])) #2lists
print("------------------------------------------")
print(len(Intra_D5._layers[2].get_weights()[0])) # 1list
print("------------------------------------------")
print(len(Intra_D5._layers[3].get_weights()[0])) # 1list
print("------------------------------------------")
print("slope")
print("------------------------------------------")
print(Intra_D5._layers[1].get_weights()[0]) #1list2arrays
print("------------------------------------------")
print(Intra_D5._layers[2].get_weights()[0]) # 1list
print("------------------------------------------")
print(Intra_D5._layers[3].get_weights()[0]) # 1list
print("------------------------------------------")


print("bias")
print("------------------------------------------")
print(Intra_D5._layers[1].get_weights()[1]) #2lists
print("------------------------------------------")
print(Intra_D5._layers[2].get_weights()[1]) # 1list
print("------------------------------------------")
print(Intra_D5._layers[3].get_weights()[1]) # 1list
print("------------------------------------------")
exit()

print(len(Intra_D5._layers[4].get_weights()[0])) # IndexError: list index out of range
print("------------------------------------------")
#print(Intra_D5._layers[1].get_weights()[0])
#print(Intra_D5._layers[1].get_weights()[0])
print("------------------------------------------")

print(threelayerlink_bidirectional_tangent_storage)
print("------------------------------------------")

print(threelayerlink_bidirectional_tangent_storage[1][5][5][0])

#threelayerlink_bidirectional_tangent_storage[1][5][5][0]

print("------------------------------------------")
#output_tangent_size = threelayerlink_bidirectional_tangent_storage[layer_number][5][5][0].shape
#AttributeError: 'list' object has no attribute 'shape'




exit()





import itertools

# COLLECT NODES
node_collection = []
for i in range(1, NETWORK_ORDER):
    node_collection.append(i)  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

# OUTER LOOP OVER ALL NODE PERMUTATIONS OF [D1 - D5]  --> LOOP OVER m IN CHOSEN PERMUTATION m
# INNER LOOP OVER NODE LAYERS --> CHOICES k

#layer_density = 16
#tangent_collection = []
#bias_collection = []

#for permutation_count in range(1, NETWORK_ORDER): 
#    tangent_collection.append([])
#    bias_collection.append([])
#    permutation_counter = 0
#    
#    tangent_collection[permutation_count].append([])
#    bias_collection[permutation_count].append([]) 
#    
#    for node_permutation in findsubsets(node_collection, permutation_count):
#        permutation_counter += 1
#        tangent_collection[permutation_count].append([])
#        bias_collection[permutation_count].append([])
#        
#        tangent_collection[permutation_count][permutation_counter].append([])
#        bias_collection[permutation_count][permutation_counter].append([]) 
#        
#        for layer_number in range(1, INTERLINK_DENSITY + 1):  
#            tangent_collection[permutation_count][permutation_counter].append([])
#            bias_collection[permutation_count][permutation_counter].append([]) 

#model_collection[permutation_count][loop_counter][layer_number]




layer_density = 16
tangent_collection = []
bias_collection = []

for permutation_count in range(0, NETWORK_ORDER + 1): 
    tangent_collection.append([])
    bias_collection.append([])
    
    node_permutation_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        tangent_collection[permutation_count].append([])
        
        bias_collection[permutation_count].append([]) 

        for layer_number in range(0, INTERLINK_DENSITY + 1): 
            tangent_collection[permutation_count][node_permutation_counter].append([])
            bias_collection[permutation_count][node_permutation_counter].append([]) 

        node_permutation_counter += 1
      


#tangent_collection[permutation_count][permutation_counter][layer_number]
#bias_collection[permutation_count][permutation_counter][layer_number]

for permutation_count in range(0, NETWORK_ORDER + 1): 
    
    node_permutation_counter = 0
    
    for node_permutation in findsubsets(node_collection, permutation_count):
        for layer_number in range(0, INTERLINK_DENSITY + 1):  
            print(tangent_collection[permutation_count][node_permutation_counter])
            print(bias_collection[permutation_count][node_permutation_counter])
            print(INTERLINK_DENSITY + 1)
            
    node_permutation_counter += 1
            
  #  permutation_counter = 0
  #  tangent_collection[permutation_count].append([])
  #  bias_collection[permutation_count].append([]) 

################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################

################################################################################
# DEBUG UNTIL MILEPOINT LINE 940
################################################################################

permutation_counter = 0
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter += 1
    for node_permutation in findsubsets(node_collection, permutation_count):
        for layer_number in range(1, INTERLINK_DENSITY + 1):  
            
            threelayerlink_bidirectional_tangent_storage_kii = []
            threelayerlink_bidirectional_bias_storage_kii = []
            for node_number in node_permutation:
                threelayerlink_bidirectional_tangent_storage_kii.append(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number])
                threelayerlink_bidirectional_bias_storage_kii.append(threelayerlink_bidirectional_bias_storage[layer_number][node_number][node_number])
                size_t = threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number][0].shape
                size_b = threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number][0].shape
            prime_threelayerlink_bidirectional_tangent_storage_kii = np.array(threelayerlink_bidirectional_tangent_storage_kii)
            prime_threelayerlink_bidirectional_bias_storage_kii = np.array(threelayerlink_bidirectional_bias_storage_kii)

            input_tangent_size = size_t
            input_bias_size = size_b
            output_tangent_size = threelayerlink_bidirectional_tangent_storage[layer_number][5][5][0].shape
            output_bias_size = threelayerlink_bidirectional_bias_storage[layer_number][5][5][0].shape
            prime_input_tangent_size = prime_threelayerlink_bidirectional_tangent_storage_kii.shape
            prime_input_bias_size = prime_threelayerlink_bidirectional_bias_storage_kii.shape
            prime_output_tangent_size = output_tangent_size
            prime_output_bias_size = output_bias_size

            processed_input = []
            training_input_nodes = []
            bias_node = []
            
            # TANGENT
            
            for node_number in node_permutation:
                
                node_input = keras.Input(shape=input_tangent_size,
                    dtype='int32',
                    name='tangent')
                preprocess_1 = layers.Dense(layer_density)(node_input)
                processed_input_node = layers.Dense(layer_density)(preprocess_1)
                processed_input.append(processed_input_node)

            concatenated = layers.concatenate(processed_input,axis=-1)
            output = layers.Dense(layer_density, activation='sigmoid')(concatenated)
            
            merged_input = []
            for node_number in node_permutation:
                merged_input.append(processed_input[node_number])
                
            model = keras.Model(merged_input, output)
            model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['acc'])
            
            for node_number in node_permutation:
                training_input_nodes.append(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number])

            training_output_node = threelayerlink_bidirectional_tangent_storage[layer_number][5][5]
            model.fit(training_input_nodes, training_output_node)
            
            environment = []
            for training_input_node in training_input_nodes:
                environment.append(training_input_node[0])
            
            D5_link = model.predict(environment)
            tangent_collection[permutation_count][permutation_counter][layer_number].append(D5_link)
            
            # BIAS
            
            processed_input = []
                     
            for node_number in node_permutation:
                
                node_input = keras.Input(shape=input_bias_size,
                    dtype='int32',
                    name='tangent')
                preprocess_1 = layers.Dense(layer_density)(node_input)
                processed_input_node = layers.Dense(layer_density)(preprocess_1)
                processed_input.append(processed_input_node)

            concatenated = layers.concatenate(processed_input,axis=-1)
            output = layers.Dense(layer_density, activation='sigmoid')(concatenated)
            
            merged_input = []
            for node_number in node_permutation:
                merged_input.append(processed_input[node_number])
                
            model = keras.Model(merged_input, output)
            model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['acc'])

            training_input_nodes = []
            bias_node = []
            
            for node_number in node_permutation:
                training_input_nodes.append(threelayerlink_bidirectional_bias_storage[layer_number][node_number][node_number])

            training_input_nodes = np.array(training_input_nodes)
            training_output_node = threelayerlink_bidirectional_bias_storage[layer_number][5][5]
            model.fit(training_input_nodes, training_output_node)
            
            environment = []
            for training_input_node in training_input_nodes:
                environment.append(training_input_node[0])
            
            D5_link_bias = model.predict(environment)
            bias_collection[permutation_count][permutation_counter][layer_number].append(D5_link_bias)
                    

loop_counter = 0
permutation_counter = 0
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter += 1
    for node_permutation in findsubsets(node_collection, permutation_count):
        loop_counter += 1
        print(loop_counter)
        print(permutation_counter)
        print(node_permutation)

def relu(x):
    return np.maximum(0, x)

inference_combinatoric = []
permutation_counter = 0
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter += 1
    for node_permutation in findsubsets(node_collection, permutation_count):
        loop_counter += 1

        tangent_link_1 = tangent_collection[permutation_count][permutation_counter][1][0]
        tangent_link_2 = tangent_collection[permutation_count][permutation_counter][2][0]
        tangent_link_3 = tangent_collection[permutation_count][permutation_counter][3][0]
        bias_link_1 = bias_collection[permutation_count][permutation_counter][1][0]
        bias_link_2 = bias_collection[permutation_count][permutation_counter][2][0]
        bias_link_3 = bias_collection[permutation_count][permutation_counter][3][0]
      
        print(loop_counter)
        print(permutation_count)
        print(node_permutation)
        
        for m in range(duration):
            sample_data = data_extraction_5_preprocess[m]
            sub_result1 = relu((tangent_link_1.transpose() @ sample_data) + bias_link_1)
            sub_result2 = relu((tangent_link_2.transpose() @ sub_result1) + bias_link_2)
            sub_result3 = ((tangent_link_3.transpose() @ sub_result2) + bias_link_3)
            print(sub_result3)

            inference_combinatoric.append(sub_result3)
        
        inference_combinatoric = np.array(inference_combinatoric)
        
        score = np.sqrt(np.sum(np.square(inference_combinatoric - temperature_extraction_preprocess)))
        #print(np.sqrt(np.sum(np.square(inference_combinatoric - temperature_extraction_preprocess))))
        print("Nodes" + str(node_permutation)+ "towards D5 link" + score)
        
exit() 




       
    
    
    
    
    
    
    
       
       
       

# INTERLINK STORAGE REQUIRES EXTRA DIMENSION
threelayerlink_bidirectional_tangentINTERLINK_storage = []   
threelayerlink_bidirectional_biasINTERLINK_storage = []        
for k in range(INTERLINK_DENSITY + 1):
    threelayerlink_bidirectional_tangentINTERLINK_storage.append([])
    threelayerlink_bidirectional_biasINTERLINK_storage.append([])
    for i in range(INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangentINTERLINK_storage[k].append([])
        threelayerlink_bidirectional_biasINTERLINK_storage[k].append([])
    for i in range(INTERLINK_DENSITY + 1):
        for j in range(NETWORK_ORDER + 1):
            threelayerlink_bidirectional_tangentINTERLINK_storage[k][i].append([])
            threelayerlink_bidirectional_biasINTERLINK_storage[k][i].append([])
    for i in range(INTERLINK_DENSITY + 1):
        for j in range(NETWORK_ORDER + 1):
            for k in range(NETWORK_ORDER + 1):
                threelayerlink_bidirectional_tangentINTERLINK_storage[k][i][j].append([])
                threelayerlink_bidirectional_biasINTERLINK_storage[k][i][j].append([])