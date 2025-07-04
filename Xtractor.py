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

from torch import inference_mode

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

    for i in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[i][1][1].append(Intra_D1._layers[i].get_weights()[0])          
        threelayerlink_bidirectional_bias_storage[i][1][1].append(Intra_D1._layers[i].get_weights()[1])

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

    for i in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[i][2][2].append(np.array(Intra_D2._layers[i].get_weights()[0]))        
        threelayerlink_bidirectional_bias_storage[i][2][2].append(np.array(Intra_D2._layers[i].get_weights()[1]))
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

        for i in range(1, INTERLINK_DENSITY + 1):
            threelayerlink_bidirectional_tangent_storage[i][3][3].append(np.array(Intra_D3._layers[i].get_weights()[0]))          
            threelayerlink_bidirectional_bias_storage[i][3][3].append(np.array(Intra_D3._layers[i].get_weights()[1]))

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

    for i in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[i][3][3].append(np.array(Intra_D3._layers[i].get_weights()[0]))          
        threelayerlink_bidirectional_bias_storage[i][3][3].append(np.array(Intra_D3._layers[i].get_weights()[1]))

    
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

    for i in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[i][4][4].append(np.array(Intra_D4._layers[i].get_weights()[0]))          
        threelayerlink_bidirectional_bias_storage[i][4][4].append(np.array(Intra_D4._layers[i].get_weights()[1]))

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

    for i in range(1, INTERLINK_DENSITY + 1):
        threelayerlink_bidirectional_tangent_storage[i][5][5].append(np.array(Intra_D5._layers[i].get_weights()[0]))          
        threelayerlink_bidirectional_bias_storage[i][5][5].append(np.array(Intra_D5._layers[i].get_weights()[1]))

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


import itertools

# COLLECT NODES
node_collection = []
for i in range(1, NETWORK_ORDER):
    node_collection.append(i)  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

# OUTER LOOP OVER ALL NODE PERMUTATIONS OF [D1 - D5]  --> LOOP OVER m IN CHOSEN PERMUTATION m
# INNER LOOP OVER NODE LAYERS --> CHOICES k

layer_density = 16

model_tangent_collection = []
model_bias_collection = []
for permutation_count in range(1, NETWORK_ORDER): 
    model_tangent_collection.append([])
    model_bias_collection.append([])
    permutation_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        model_tangent_collection[permutation_count].append([])
        model_bias_collection[permutation_count].append([])
        permutation_counter += 1
        for layer_number in range(1, INTERLINK_DENSITY + 1):  
            model_tangent_collection[permutation_count][permutation_counter].append([])
            model_bias_collection[permutation_count][permutation_counter].append([]) 

#model_collection[permutation_count][loop_counter][layer_number]
model_bias_collection[permutation_count][permutation_counter][layer_number]

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
                size = threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number].shape
            
            
            prime_threelayerlink_bidirectional_tangent_storage_kii = np.array(threelayerlink_bidirectional_tangent_storage_kii)
            prime_threelayerlink_bidirectional_bias_storage_kii = np.array(threelayerlink_bidirectional_bias_storage_kii)
    
            input_tangent_size = size

            input_bias_size = prime_threelayerlink_bidirectional_bias_storage_kii.shape
            
            output_tangent_size = threelayerlink_bidirectional_tangent_storage.shape[layer_number][5][5][0].shape
            
            output_bias_size = threelayerlink_bidirectional_bias_storage[layer_number][5][5][0].shape

            prime_input_tangent_size = prime_threelayerlink_bidirectional_tangent_storage_kii.shape

            prime_input_bias_size = prime_threelayerlink_bidirectional_bias_storage_kii.shape
            
            prime_output_tangent_size = output_tangent_size

            prime_output_bias_size = output_bias_size

            processed_input = []
            training_input_nodes = []
            bias_node = []
            
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

            training_input_nodes = np.array(training_input_nodes)

            training_output_node
            
            model.fit(training_input_nodes, training_output_node)
            
            D5_link = model.predict(training_input_nodes[0])
            model_tangent_collection[permutation_count][permutation_counter][layer_number].append(D5_link)
            

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
            
            D5_link = model.predict(training_input_nodes[0])

            model_bias_collection[permutation_count][permutation_counter][layer_number].append(D5_link)
                    

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

        tangent_link_1 = model_tangent_collection[permutation_count][permutation_counter][1][0]
        tangent_link_2 = model_tangent_collection[permutation_count][permutation_counter][2][0]
        tangent_link_3 = model_tangent_collection[permutation_count][permutation_counter][3][0]
        bias_link_1 = model_bias_collection[permutation_count][permutation_counter][1][0]
        bias_link_2 = model_bias_collection[permutation_count][permutation_counter][2][0]
        bias_link_3 = model_bias_collection[permutation_count][permutation_counter][3][0]
      
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
        print(np.sqrt(np.sum(np.square(inference_combinatoric - temperature_extraction_preprocess))))
        print(str(node_permutation)+ "towards D5 link" + score)
        
        
        
        
        
exit() 
        
       
        
####################################################################################################   
# AFTERWARDS, TO OVERSEE HIGHER LEVEL CODE, MANUAL COMPUTATION AND TWEAKS BY MERGED INTERLINK
# D1, D2 --> D5 VIA MERGED INTRALINKS AND MERGED INTERLINKS IF MANUAL COMPUTATION
####################################################################################################
        
# 






#threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]
#threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]






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








# INTRALINK EXTRACTION
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
            
            # EXTRACT WEIGHTS FROM Inter_D1_D2_tangent and Inter_D1_D2_bias in INTERLINK STORAGE
            # 3 INTERLINK LAYERS PER INTRALINK LAYER
            # CHECK WEIGHT STORAGE IN LAYER 
            for m in range(1, INTERLINK_DENSITY + 1):
                threelayerlink_bidirectional_tangentINTERLINK_storage[k][m][i][j].append(np.array(Inter_D1_D2_tangent._layers[i].get_weights()[0]))
                threelayerlink_bidirectional_biasINTERLINK_storage[k][m][i][j].append(np.array(Inter_D1_D2_bias._layers[i].get_weights()[1]))                                                                           
   
   
   
   
   
        

for permutation_count in range(1, NETWORK_ORDER): 
    
    for node_permutation in findsubsets(node_collection, permutation_count):
        
        for l_intra in range(1, INTERLINK_DENSITY + 1):
            
            for l_inter in range(1, INTERLINK_DENSITY + 1):
                # INTERLINK LAYER k INTRALINK LAYER m NODE i -> NODE j

                 #   threelayerlink_bidirectional_tangentINTERLINK_storage
                 #   threelayerlink_bidirectional_biasINTERLINK_storage

                input_nodes = []
                
                for node in node_permutation:
                    input_nodes.append(threelayerlink_bidirectional_tangentINTERLINK_storage[l_intra][l_inter][node][5])
                    
                    
                D5__tangent_link = threelayerlink_bidirectional_tangentINTERLINK_storage[l_intra][l_inter][node][5][0] @ threelayerlink_bidirectional_tangent_storage[l_intra][node][5][0]  
                D5__bias_link = threelayerlink_bidirectional_biasINTERLINK_storage[l_intra][l_inter][node][5][0] @ threelayerlink_bidirectional_bias_storage[l_intra][node][5][0]

                threelayerlink_bidirectional_tangentINTERLINK_storage[l_intra][l_inter][node][5][0] @ threelayerlink_bidirectional_bias_storage

                D5__tangent_link
                
                D5__bias_link


                
                
                for m in range(duration):
                    sample_data = data_extraction_5[j][m]
                    
                    sub_result1 = relu((threelayerlink_bidirectional_tangent_storage[1][i][j][0].transpose() @ sample_data) + threelayerlink_bidirectional_bias_storage[1][i][j][0])
                    sub_result2 = relu((threelayerlink_bidirectional_tangent_storage[2][i][j][0].transpose() @ sub_result1) + threelayerlink_bidirectional_bias_storage[2][i][j][0])
                    sub_result3 = ((threelayerlink_bidirectional_tangent_storage[3][i][j][0].transpose() @ sub_result2) + threelayerlink_bidirectional_bias_storage[3][i][j][0])
                    print(sub_result3)
                
                
                
                
                
                
                






     
                
                input_nodes
                    
                    
        
            
        
    #threelayerlink_bidirectional_tangentINTERLINK_storage[1][1][i][5]
    
    
    threelayerlink_bidirectional_tangentINTERLINK_storage[1][2][i][5]
    threelayerlink_bidirectional_tangentINTERLINK_storage[1][3][i][5]
    
    threelayerlink_bidirectional_biasINTERLINK_storage[1][1][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[1][2][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[1][3][i][5]
    
    threelayerlink_bidirectional_biasINTERLINK_storage[2][1][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[2][2][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[2][3][i][5]
    
    threelayerlink_bidirectional_biasINTERLINK_storage[3][1][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[3][2][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[3][3][i][5]
    
    
    threelayerlink_bidirectional_biasINTERLINK_storage[1][1][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[1][2][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[1][3][i][5]
    
    threelayerlink_bidirectional_biasINTERLINK_storage[2][1][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[2][2][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[2][3][i][5]
    
    threelayerlink_bidirectional_biasINTERLINK_storage[3][1][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[3][2][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[3][3][i][5]
    
    
    
    
    
    
    threelayerlink_bidirectional_biasINTERLINK_storage[1][2][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[1][3][i][5]
    
    threelayerlink_bidirectional_biasINTERLINK_storage[1][2][i][5]
    threelayerlink_bidirectional_biasINTERLINK_storage[1][3][i][5]











    threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][i][5]
                    




















threelayerlink_bidirectional_biasINTERLINK_storage
threelayerlink_bidirectional_biasINTERLINK_storage

input_tangent_size = threelayerlink_bidirectional_tangent_storage[k][i][i][0].shape
output_tangent_size = threelayerlink_bidirectional_tangent_storage[k][j][j][0].shape
input_bias_size = threelayerlink_bidirectional_bias_storage[k][i][i][0].shape
output_bias_size = threelayerlink_bidirectional_bias_storage[k][j][j][0].shape

#threelayerlink_bidirectional_tangent_storage[k][i][j][0]




threelayerlink_bidirectional_tangentINTERLINK_storage[k][j][j][0]
threelayerlink_bidirectional_biasINTERLINK_storage[k][j][j][0]




threelayerlink_bidirectional_tangentINTERLINK_storage


threelayerlink_bidirectional_biasINTERLINK_storage








            
node_permutation, 
          

inference_starlink[i][j] = np.array(inference_starlink[i][j])
print(np.sqrt(np.sum(np.square(inference_starlink[i][j] - temperature_extraction_preprocess))))

model_tangent_collection[permutation_count][permutation_counter][layer_number][i]
data_extraction_5
sample_data = data_extraction_postprocess[j][m]

sub_result1 = relu((threelayerlink_bidirectional_tangent_storage[1][i][j][0].transpose() @ sample_data) + threelayerlink_bidirectional_bias_storage[1][i][j][0])
sub_result2 = relu((threelayerlink_bidirectional_tangent_storage[2][i][j][0].transpose() @ sub_result1) + threelayerlink_bidirectional_bias_storage[2][i][j][0])
sub_result3 = ((threelayerlink_bidirectional_tangent_storage[3][i][j][0].transpose() @ sub_result2) + threelayerlink_bidirectional_bias_storage[3][i][j][0])
print(sub_result3)
print(type(sub_result3))
inference_starlink[i][j].append(sub_result3[0])
    
        
        
        




        
####################################################################################################
        


model_bias_collection









for node_number in node_permutation:
    node_input = keras.Input(shape=input_tangent_size,
        dtype='int32',
        name='tangent')
    preprocess_1 = layers.Dense(layer_density)(node_input)
    processed_input_node = layers.Dense(layer_density)(preprocess_1)
    processed_input.append(processed_input_node)


for permutation_count in range(1, NETWORK_ORDER): 
    loop_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        loop_counter += 1
        for layer_number in range(1, INTERLINK_DENSITY + 1):              
            


for permutation_count in range(1, NETWORK_ORDER): 
    for node_permutation in findsubsets(node_collection, permutation_count):
        for layer_number in range(1, INTERLINK_DENSITY + 1):  
            

for node_number in node_permutation:
    threelayerlink_bidirectional_tangent_storage_kii.append(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][5])  

        Intra_D1._layers[i].get_weights()[0]

 #       model(merged_input)
        
        
        
        

        
        
        
            
            
    
                
                
                
                
                
              #  input_tangent_size
                
            #    input_bias_size
                
           #     embedded_text = layers.Embedding(
           #     64, text_vocabulary_size)(text_input)
                
           # for node_number in 
            
                    
            
            
            
question_input = Input(shape=(None,),
    dtype='int32',
    name='question')

embedded_question = layers.Embedding(
    32, question_vocabulary_size)(question_input)

encoded_question = layers.LSTM(16)(embedded_question)


answer = layers.Dense(answer_vocabulary_size,
    activation='softmax')(concatenated)

model = Model([text_input, question_input], answer)

model.compile(optimizer='rmsprop',
    loss='categorical_cr)
            
            
            
            

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
            
        
        
        
                

        
            
            
        [text, question]
        input_tangent_size = threelayerlink_bidirectional_tangent_storage[k][i][i][0].shape
        output_tangent_size = threelayerlink_bidirectional_tangent_storage[k][j][j][0].shape
        input_bias_size = threelayerlink_bidirectional_bias_storage[k][i][i][0].shape
        output_bias_size = threelayerlink_bidirectional_bias_storage[k][j][j][0].shape
            
        
                
                
                
            
            
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
                # INTERLINK LAYER k INTRALINK LAYER m NODE i -> NODE j
                for l_intra in range(1, INTERLINK_DENSITY + 1):
                    
                    










# INTRALINK EXTRACTION
#for k in range(1, INTERLINK_DENSITY + 1):
#    for i in range(1, NETWORK_ORDER + 1):
#        for j in range(1, NETWORK_ORDER + 1):
#            threelayerlink_bidirectional_tangent_storage[][][]
#





####################################################################################




# INTRALINK EXTRACTION
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
            
            # EXTRACT WEIGHTS FROM Inter_D1_D2_tangent and Inter_D1_D2_bias in INTERLINK STORAGE
            # 3 INTERLINK LAYERS PER INTRALINK LAYER
            # CHECK WEIGHT STORAGE IN LAYER 
            for m in range(1, INTERLINK_DENSITY + 1):
                threelayerlink_bidirectional_tangentINTERLINK_storage[k][m][i][j].append(np.array(Inter_D1_D2_tangent._layers[i].get_weights()[0]))
                threelayerlink_bidirectional_biasINTERLINK_storage[k][m][i][j].append(np.array(Inter_D1_D2_bias._layers[i].get_weights()[1]))                                                                           
        
##############################################################################
# D1, D2 -> D5
# MERGED INTERLINK CONSTRUCTION
##############################################################################
# MERGED D1 -> D5, D2 -> D5 INTERLINK AS MEDIUM FOR MERGED D1, D2 INTRALINK
# --> CAPTURE ENVIRONMENT INTERACTION
##############################################################################

# INTERLINK STORAGE MANUAL

# threelayerlink_bidirectional_tangentINTERLINK_storage[k][m][i][j]
# INTERLINK LAYER k INTRALINK LAYER m NODE i -> NODE j

threelayerlink_bidirectional_tangentINTERLINK_storage[k][m][i][j]

data_extraction_5
data_extraction_1_preprocess = raw_data[:-delay, [0, 2]] #3]]
data_extraction_2_preprocess = raw_data[:-delay, [4, 5]]
data_extraction_3_preprocess = raw_data[:-delay, [6, 7]] #8]]
data_extraction_4_preprocess = raw_data[:-delay, [9, 10]] #11]] # Make Node-observations equidimensional
data_extraction_5_preprocess = raw_data[:-delay, [12, 13]]
temperature_extraction_preprocess = temperature[delay:] 














#data_extraction = []
#=(64,))

# OUTER-LOOP INTRALINK INNER-LOOP INTERLINK 
# OUTER LOOP OVER NODE COMBINATIONS  COLLECT ALL PERMUTATIONS OF [D1 - D5] IN LIST  --> LOOP OVER m IN CHOSEN PERMUTATION m
# INNER LOOP OVER NODE LAYERS --> CHOICES k


import itertools

# Driver Code

#n = 3
 
 
##############################################################################
# D1, D2 -> D5
# MERGED INTERLINK CONSTRUCTION
##############################################################################
# MERGED D1 -> D5, D2 -> D5 INTERLINK AS MEDIUM FOR MERGED D1, D2 INTRALINK
# --> CAPTURE ENVIRONMENT INTERACTION
##############################################################################

 
 
 
#print(findsubsets(s, n))

#for subset in findsubsets(s, n):
 #   print(subset)
 #   for i in subset:
 #       findsubsets(s, i)


# COLLECT NODES
node_collection = []
for i in range(1, NETWORK_ORDER):
    node_collection.append(i)  
def findsubsets(s, n):
    return list(itertools.combinations(s, n))

# OUTER LOOP OVER ALL NODE PERMUTATIONS OF [D1 - D5]  --> LOOP OVER m IN CHOSEN PERMUTATION m
# INNER LOOP OVER NODE LAYERS --> CHOICES k

# DIFFICULTY: EITHER MERGE DATA, OR USE MERGE NeuralNet

# ORGANIZE LOOP ORDER
#for z in range(1, INTERLINK_DENSITY + 1):

merged_inputnode_tangent_interintra = []
merged_inputnode_bias_interintra = []
merged_inputnode_tangent_interintra
merged_inputnode_tangent_interintra

for permutation_count in range(1, NETWORK_ORDER): 
    for node_permutation in findsubsets(node_collection, permutation_count):
        for node in node_permutation:
            for l_inter in range(1, INTERLINK_DENSITY + 1):
                # INTERLINK LAYER k INTRALINK LAYER m NODE i -> NODE j
                for l_intra in range(1, INTERLINK_DENSITY + 1):
                    
                    
                
                
            #       print(permutation_count)
            #       print(node_permutation)
            #       print(l_inter)
        #           print(l_intra)
                
exit()
                

# PROCEED LEARNING IN CURRENT LOOP
#             merged_inputnode_tangent_interintra.append([])

#for node_input in node_permutation:
#       
#     merged_inputnode_bias_interintra[-1].append(threelayerlink_bidirectional_biasINTERLINK_storage[l_inter][l_intra][node_input][5])

#     merged_inputnode_tangent_interintra[-1].append(threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5])
# threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]

# Inter_D1_D2_tangent.fit(threelayerlink_bidirectional_tangent_storage_kii, threelayerlink_bidirectional_tangent_storage_kjj, epochs=5, batch_size=128)

# threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]          

# tangent data in 
# bias data in 

#      merged_inputnode_tangent_interintra[-1]

#merged_inputnode_tangent_interintra[-1]

# PROCEED WITH MERGE NEURALNET

#INTERLINK WEIGHTS

#node_permutation

#for node_input in node_permutation:
#threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]

#for node_input in node_permutation:
#threelayerlink_bidirectional_biasINTERLINK_storage[l_inter][l_intra][node_input][5]
            
#threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]



# CONCATENATE NODE_INPUT IN SUBSET FOR EACH L_INTER FOR EACH L_INTRA

print("----------------*******************----------------------")
print("----------------*******************----------------------")
print("----------------*******************----------------------")

#threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]
#threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]

inputs_extraction_1 = keras.Input(shape = threelayerlink_bidirectional_tangent_storage_kii.shape)
inputs_extraction_2 = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))

x_1 = layers.Dense(16, activation="relu")(inputs_extraction_1)
x_1 = layers.Dense(16, activation="relu")(inputs_extraction_1)

x_2 = layers.Dense(16, activation="relu")(inputs_extraction_2)


x = layers.Dense(16, activation="relu")(inputs)

threelayerlink_bidirectional_tangent_storage_kii = np.array(threelayerlink_bidirectional_tangent_storage[k][i][i])
threelayerlink_bidirectional_tangent_storage_kjj = np.array(threelayerlink_bidirectional_tangent_storage[k][j][j])

x = layers.Dense(16, activation="relu")(x)
outputs = layers.Dense(1)(x)


threelayerlink_bidirectional_tangent_storage_kii
                        
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




threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]
threelayerlink_bidirectional_tangentINTERLINK_storage[l_inter][l_intra][node_input][5]








inputs_extraction_1 = keras.Input(shape = threelayerlink_bidirectional_tangent_storage_kii.shape)
inputs_extraction_2 = keras.Input(shape = threelayerlink_bidirectional_tangent_storage_kii.shape)
x_1 = layers.Dense(16, activation="relu")(inputs_extraction_1)
x_2 = layers.Dense(16, activation="relu")(inputs_extraction_2)




concatenated = layers.concatenate([x_1, x_2],
axis=-1)

answer = layers.Dense(answer_vocabulary_size,
activation='softmax')(concatenated)







x = layers.Dense(16, activation="relu")(inputs)                






for permutation_count in range(1, NETWORK_ORDER): 
    for node_permutation in findsubsets(node_collection, permutation_count):
        for node in node_permutation:
            for l_inter in range(1, INTERLINK_DENSITY + 1):
                # INTERLINK LAYER k INTRALINK LAYER m NODE i -> NODE j
                for l_intra in range(1, INTERLINK_DENSITY + 1):
                    
                    















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


#threelayerlink_bidirectional_tangentINTERLINK_storage[]

# INTERLINK LAYER k INTRALINK LAYER m NODE i -> NODE j


threelayerlink_bidirectional_tangentINTERLINK_storage[k][n][j][5]


    
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

for i in range(1, INTERLINK_DENSITY + 1):
threelayerlink_bidirectional_tangent_storage[i][1][1].append(Intra_D1._layers[i].get_weights()[0])          
threelayerlink_bidirectional_bias_storage[i][1][1].append(Intra_D1._layers[i].get_weights()[1])



shape
inputs_extraction_1 = keras.Input(shape = threelayerlink_bidirectional_tangent_storage_kii.shape)
inputs_extraction_2 = keras.Input(shape=(sequence_length, data_extraction_1.shape[-1]))

x_1 = layers.Dense(16, activation="relu")(inputs_extraction_1)
x_1 = layers.Dense(16, activation="relu")(inputs_extraction_1)

x_2 = layers.Dense(16, activation="relu")(inputs_extraction_2)


x = layers.Dense(16, activation="relu")(inputs)

threelayerlink_bidirectional_tangent_storage_kii = np.array(threelayerlink_bidirectional_tangent_storage[k][i][i])
threelayerlink_bidirectional_tangent_storage_kjj = np.array(threelayerlink_bidirectional_tangent_storage[k][j][j])

x = layers.Dense(16, activation="relu")(x)
outputs = layers.Dense(1)(x)



Inter_ = keras.Model(inputs, outputs)
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



text_input = keras.Input(shape=(None,), dtype='int32', name='text')
embedded_text = keras,layers.Embedding(
64, text_vocabulary_size)(text_input)

encoded_text = keras.layers.LSTM(32)(embedded_text)

question_input = keras.Input(shape=(None,),
dtype='int32',
name='question')

embedded_question = keras.layers.Embedding(
32, question_vocabulary_size)(question_input)

encoded_question = keras.layers.LSTM(16)(embedded_question)
concatenated = layers.concatenate([encoded_text, encoded_question],
axis=-1)

answer = keras.layers.Dense(answer_vocabulary_size,
activation='softmax')(concatenated)

model = keras.Model([text_input, question_input], answer)
model.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['acc'])


for i in range(1, INTERLINK_DENSITY + 1):
threelayerlink_bidirectional_tangent_storage[i][5][5].append(np.array(Intra_D5._layers[i].get_weights()[0]))          
threelayerlink_bidirectional_bias_storage[i][5][5].append(np.array(Intra_D5._layers[i].get_weights()[1]))






    
# MULTI-INPUT MONO OUTPUT

text_vocabulary_size = 10000
question_vocabulary_size = 10000
answer_vocabulary_size = 500

text_input = keras.Input(shape=(None,), dtype='int32', name='text')
embedded_text = keras,layers.Embedding(
    64, text_vocabulary_size)(text_input)

encoded_text = keras.layers.LSTM(32)(embedded_text)

question_input = Input(shape=(None,),
    dtype='int32',
    name='question')

embedded_question = keras.layers.Embedding(
    32, question_vocabulary_size)(question_input)

encoded_question = keras.layers.LSTM(16)(embedded_question)
concatenated = layers.concatenate([encoded_text, encoded_question],
    axis=-1)

answer = keras.layers.Dense(answer_vocabulary_size,
    activation='softmax')(concatenated)

model = Model([text_input, question_input], answer)
model.compile(optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['acc'])



                        
                        
print("D5--------------*******************----------------------")
print("----------------*******************----------------------")
print("----------------*******************----------------------")


# MULTI-INPUT MONO OUTPUT EXAMPLE
text_vocabulary_size = 10000
question_vocabulary_size = 10000
answer_vocabulary_size = 500

text_input = keras.Input(shape=(None,), dtype='int32', name='text')
embedded_text = keras,layers.Embedding(
    64, text_vocabulary_size)(text_input)

encoded_text = keras.layers.LSTM(32)(embedded_text)

question_input = Input(shape=(None,),
    dtype='int32',
    name='question')

embedded_question = keras.layers.Embedding(
    32, question_vocabulary_size)(question_input)

encoded_question = keras.layers.LSTM(16)(embedded_question)
concatenated = layers.concatenate([encoded_text, encoded_question],
    axis=-1)

answer = keras.layers.Dense(answer_vocabulary_size,
    activation='softmax')(concatenated)

model = Model([text_input, question_input], answer)
model.compile(optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['acc'])
        
        
        
        
        
        
                
   
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



# USUAL STARLINKS
# D1 -> D5
# D2 -> D5
# D3 -> D5
# D4 -> D5

# COMBINATORIC INTERLINK INTEGRATION
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













# MULTI-INPUT MONO OUTPUT EXAMPLE
text_vocabulary_size = 10000
question_vocabulary_size = 10000
answer_vocabulary_size = 500

text_input = keras.Input(shape=(None,), dtype='int32', name='text')
embedded_text = keras,layers.Embedding(
    64, text_vocabulary_size)(text_input)

encoded_text = keras.layers.LSTM(32)(embedded_text)

question_input = Input(shape=(None,),
    dtype='int32',
    name='question')

embedded_question = keras.layers.Embedding(
    32, question_vocabulary_size)(question_input)

encoded_question = keras.layers.LSTM(16)(embedded_question)
concatenated = layers.concatenate([encoded_text, encoded_question],
    axis=-1)

answer = keras.layers.Dense(answer_vocabulary_size,
    activation='softmax')(concatenated)

model = Model([text_input, question_input], answer)
model.compile(optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['acc'])




# ASSUME GIVEN INTRA INTER AND MULTIPLE NODES D1 D2

# FULL COMPLETE COMBINTORIC INTEGRATION VIA MERGED NEURALNET
# D1, D2 --> D5 VIA MERGED INTRALINKS IF VIA MERGED NEURALNET ***
# COLLECT INTRALINKS D1 D2 --> INPUT FOR MULTI-INPUT MONO-OUTPUT 

# AFTERWARDS, TO OVERSEE HIGHER LEVEL CODE, MANUAL COMPUTATION AND TWEAKS BY MERGED INTERLINK
# D1, D2 --> D5 VIA MERGED INTRALINKS AND MERGED INTERLINKS IF MANUAL COMPUTATION



########################################################################
########################################################################
# FULL COMPLETE COMBINTORIC INTEGRATION VIA MERGED NEURALNET
# D1, D2 --> D5 VIA MERGED INTRALINKS IF VIA MERGED NEURALNET ***
# COLLECT INTRALINKS D1 D2 --> INPUT FOR MULTI-INPUT MONO-OUTPUT 
# COLLECT INTRALINK D5 OUTPUT MERGED NEURALNET
########################################################################
########################################################################

from keras.models import Model
from keras import layers
from keras import Input

text_vocabulary_size = 10000
question_vocabulary_size = 10000
answer_vocabulary_size = 500

text_input = Input(shape=(None,), dtype='int32', name='text')

embedded_text = layers.Embedding(
    64, text_vocabulary_size)(text_input)
encoded_text = layers.LSTM(32)(embedded_text)

question_input = Input(shape=(None,),
    dtype='int32',
    name='question')

embedded_question = layers.Embedding(
    32, question_vocabulary_size)(question_input)

encoded_question = layers.LSTM(16)(embedded_question)
    
concatenated = layers.concatenate([encoded_text, encoded_question],
    axis=-1)

answer = layers.Dense(answer_vocabulary_size,
    activation='softmax')(concatenated)

model = Model([text_input, question_input], answer)

model.compile(optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['acc'])

########################################################################
########################################################################