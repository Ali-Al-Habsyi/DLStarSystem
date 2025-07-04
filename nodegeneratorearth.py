################################################################################
#
# ESSENTIAL REQUIREMENT
# NODE GENERATOR
#
################################################################################

################################################################################
# DEVICES
# COMMUNICATORS OF OBSERVATION
################################################################################

################################################################################
# VIRTUAL DEVICES 
# 
# DATA RETRIEVAL FROM SIMULATED GENERATING-PROCESS (TEMPORARY SOLUTION-TEMPLATE FOR IMPLEMENTATION COMPUTATION SYSTEM IN FULL GENERALITY)
# DATA RETRIEVAL FROM DATABANKS SPACE-AGENCIES
# (CURRENT) --> COLLECTORS OVER WWW
#
################################################################################

# NODE GENERATOR <-> SYSTEM OUTPUT CONTROLLER <-> STARLINK (CYCLIC REVAMP)
# IN LAYMAN TERMS: OBSERVER <-> EXPLORER <-> COMPUTER (CYCLIC REVAMP)
# HARDWARE: COMPUTER SIMULATION, LATER SPECIALIZED
# MACHINE PROGRESS BY MILESTONES OF DISCOVERY
# OBSERVE -> COMPUTE -> EXPLORE -> OBSERVE -> COMPUTE -> EXPLORE -> ...



################################################################################
#
# ESSENTIAL REQUIREMENT
# NODE GENERATOR
#
################################################################################

################################################################################
# DEVICES
# COMMUNICATORS OF OBSERVATION
################################################################################

################################################################################
# VIRTUAL DEVICES 
# 
# DATA RETRIEVAL FROM SIMULATED GENERATING-PROCESS (TEMPORARY SOLUTION-TEMPLATE FOR IMPLEMENTATION COMPUTATION SYSTEM IN FULL GENERALITY)
# DATA RETRIEVAL FROM DATABANKS SPACE-AGENCIES
# (CURRENT) --> COLLECTORS OVER WWW
#
################################################################################

# NODE GENERATOR <-> SYSTEM OUTPUT CONTROLLER <-> STARLINK (CYCLIC REVAMP)
# IN LAYMAN TERMS: OBSERVER <-> EXPLORER <-> COMPUTER (CYCLIC REVAMP)
# HARDWARE: COMPUTER SIMULATION, LATER SPECIALIZED
# MACHINE PROGRESS BY MILESTONES OF DISCOVERY








































################################################################################



import numpy as np
import os
from tensorflow import keras
from tensorflow.keras import layers
import math
 
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
# VARIANT 1 (OUTPUT: LINK BETWEEN LINKS <=> LINK BETWEEN LINK AND LINKS) 
#           (INTERESTING; D1 - D5 ARE ENVIRONMENTS THAT ARE WORLD'S AWAY FROM ONE ANOTHER)
# CHECK CODE FOR BUGS IN COMPUTATION; D1 -> D5 - D4 -> D5 PRESICION VARIATION EXPECTED

##################################################################
# NODE-ENVIRONMENT PROCEDURE OF DOWNLOAD (License: Keras Developer)
##################################################################

from zipfile import ZipFile

# Access NASA Earthdata
import earthaccess
import dlc2kinematics

earthaccess.login()








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
INTRALINK_N = 50 # TO BE TWEAKED, VARIABILITY DUE TO DURATION EXPOSURE, MAKE LARGER MAGNITUDES POSSIBLE
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

for j in range(INTRALINK_N):
    
    print("Intralink loop 2")
    
    # INTRALINK_N 
    data_extraction_1 = data_extraction_1_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    data_extraction_2 = data_extraction_2_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    data_extraction_3 = data_extraction_3_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    data_extraction_4 = data_extraction_4_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    data_extraction_5 = data_extraction_5_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    temperature_extraction = temperature[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    
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






################################################################################
#
# ESSENTIAL REQUIREMENT
# NODE GENERATOR
#
################################################################################

################################################################################
# DEVICES
# COMMUNICATORS OF OBSERVATION
################################################################################

################################################################################
# VIRTUAL DEVICES 
# 
# DATA RETRIEVAL FROM SIMULATED GENERATING-PROCESS (TEMPORARY SOLUTION-TEMPLATE FOR IMPLEMENTATION COMPUTATION SYSTEM IN FULL GENERALITY)
# DATA RETRIEVAL FROM DATABANKS SPACE-AGENCIES
# (CURRENT) --> COLLECTORS OVER WWW
#
################################################################################

# NODE GENERATOR <-> SYSTEM OUTPUT CONTROLLER <-> STARLINK (CYCLIC REVAMP)
# IN LAYMAN TERMS: OBSERVER <-> EXPLORER <-> COMPUTER (CYCLIC REVAMP)
# HARDWARE: COMPUTER SIMULATION, LATER SPECIALIZED
# MACHINE PROGRESS BY MILESTONES OF DISCOVERY







import keras
import numpy as np
import os
from tensorflow import keras
from tensorflow.keras import layers
import math
 
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
# VARIANT 1 (OUTPUT: LINK BETWEEN LINKS <=> LINK BETWEEN LINK AND LINKS) 
#           (INTERESTING; D1 - D5 ARE ENVIRONMENTS THAT ARE WORLD'S AWAY FROM ONE ANOTHER)
# CHECK CODE FOR BUGS IN COMPUTATION; D1 -> D5 - D4 -> D5 PRESICION VARIATION EXPECTED

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
INTRALINK_N = 50 # TO BE TWEAKED, VARIABILITY DUE TO DURATION EXPOSURE, MAKE LARGER MAGNITUDES POSSIBLE
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





for j in range(INTRALINK_N):
    
    print("Intralink loop 2")
    
    # INTRALINK_N 
    data_extraction_1 = data_extraction_1_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    data_extraction_2 = data_extraction_2_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    data_extraction_3 = data_extraction_3_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    data_extraction_4 = data_extraction_4_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    data_extraction_5 = data_extraction_5_preprocess[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    temperature_extraction = temperature[math.floor(j * duration/INTRALINK_N) : math.floor((j + 1) * duration/INTRALINK_N)]
    
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
