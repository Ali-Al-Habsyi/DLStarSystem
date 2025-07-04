NETWORK_ORDER = 5
INTERLINK_DENSITY = 3

import itertools
import numpy as np

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
sampling_rate = 6
sequence_length = 120
delay = sampling_rate * (sequence_length + 24 - 1)
batch_size = 256

num_train_samples = int(0.5 * len(raw_data))
num_val_samples = int(0.25 * len(raw_data))
num_test_samples = len(raw_data) - num_train_samples - num_val_samples
duration = len(raw_data) - delay

data_extraction_1_preprocess = raw_data[:-delay, [0, 2]] #3]]
data_extraction_2_preprocess = raw_data[:-delay, [4, 5]]
data_extraction_3_preprocess = raw_data[:-delay, [6, 7]] #8]]
data_extraction_4_preprocess = raw_data[:-delay, [9, 10]] #11]] # Make Node-observations equidimensional
data_extraction_5_preprocess = raw_data[:-delay, [12, 13]]
temperature_extraction_preprocess = temperature[delay:]

layer_density = 100
tangent_collection = []
bias_collection = []

threelayerlink_bidirectional_tangent_storage = []
threelayerlink_bidirectional_bias_storage = []

#for node_number in range(0, NETWORK_ORDER + 1): 
##    threelayerlink_bidirectional_tangent_storage.append([])
 #   
  #  node_permutation_counter = 0
 #   for node_number in range(0, NETWORK_ORDER + 1):
    #    threelayerlink_bidirectional_tangent_storage[node_number].append([])
   #     
        #bias_collection[permutation_count].append([]) 
#
 #       for layer_number in range(0, INTERLINK_DENSITY + 1): 
            #tangent_collection[permutation_count][node_permutation_counter].append([])
            #bias_collection[permutation_count][node_permutation_counter].append([])
       #     
 #           threelayerlink_bidirectional_tangent_storage[node_number][node_number]

#        node_permutation_counter += 1


#threelayerlink_bidirectional_tangent_storage

layer_density = 100
tangent_collection = []
bias_collection = []

#TESTLOOP
for permutation_count in range(0, 99): 
    tangent_collection.append([])
    bias_collection.append([])
    for node_permutation_counter in range(0, 99):
        tangent_collection[permutation_count].append([])
        bias_collection[permutation_count].append([]) 
        for layer_number in range(0, 99): 
            tangent_collection[permutation_count][node_permutation_counter].append([])
            bias_collection[permutation_count][node_permutation_counter].append([]) 
            print("STORAGE INITIALIZATION")
            
# TESTLOOP   
inference_total = []
for permutation_count in range(0, 99): 
    inference_total.append([])
    for permutation_counter in range(0, 99):
        inference_total[permutation_count].append([])




#permutation_counter = 0
#for permutation_count in range(0, NETWORK_ORDER): 
#    permutation_counter += 1
#    for node_permutation in findsubsets(node_collection, permutation_count):
#        for layer_number in range(1, INTERLINK_DENSITY + 1):  



#PROBLEM: ENTRY: bias_collection[permutation_count][permutation_counter][layer_number].append(D5_link_bias[0])




for layer_number in range(0, INTERLINK_DENSITY + 1): 
    
    threelayerlink_bidirectional_tangent_storage.append([])
    threelayerlink_bidirectional_bias_storage.append([])
    print("===============================================================")
    print(len(threelayerlink_bidirectional_tangent_storage))
    #node_permutation_counter = 0
    
    for node_number_1 in range(0, NETWORK_ORDER + 1): 
        
        print(len(threelayerlink_bidirectional_tangent_storage[layer_number]))
        threelayerlink_bidirectional_tangent_storage[layer_number].append([])
        threelayerlink_bidirectional_bias_storage[layer_number].append([])

        for node_number_2 in range(0, NETWORK_ORDER + 1): 
            #tangent_collection[permutation_count][node_permutation_counter].append([])
            #bias_collection[permutation_count][node_permutation_counter].append([])
            threelayerlink_bidirectional_tangent_storage[layer_number][node_number_1].append([]) 
            threelayerlink_bidirectional_bias_storage[layer_number][node_number_1].append([])
            
            for i in range(10):
                
                threelayerlink_bidirectional_tangent_storage[layer_number][node_number_1][node_number_2].append(np.eye(100))
                threelayerlink_bidirectional_bias_storage[layer_number][node_number_1][node_number_2].append(np.eye(100))

#permutation_count
#layer_number
     #node_permutation_counter += 1
      
import keras

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
print("-----------------------------------------------------------------------")
################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################

################################################################################
# DEBUG UNTIL MILEPOINT LINE 940
################################################################################


#np.array(threelayerlink_bidirectional_bias_storage[k][i][i]) 
#np.array(threelayerlink_bidirectional_bias_storage[k][i][i])

inference_combinatoric = []  
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1   
        for layer_number in range(1, INTERLINK_DENSITY + 1):  
            break


inference_combinatoric = []  





#permutation_counter = 0
#for permutation_count in range(1, NETWORK_ORDER): 
#    permutation_counter += 1
#    for node_permutation in findsubsets(node_collection, permutation_count):
#        for layer_number in range(1, INTERLINK_DENSITY + 1):  

for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1   
        for layer_number in range(1, INTERLINK_DENSITY + 1):  
            
            print(permutation_count)
            print(permutation_counter)
            print(node_permutation)
            print(layer_number)
            
            threelayerlink_bidirectional_tangent_storage_kii = []
            threelayerlink_bidirectional_bias_storage_kii = []
            for node_number in node_permutation:

                #array_conversion_tangent = np.array(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number])
                #array_conversion_bias = np.array(threelayerlink_bidirectional_bias_storage[layer_number][node_number][node_number])
                threelayerlink_bidirectional_tangent_storage_kii.append(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number])
                threelayerlink_bidirectional_bias_storage_kii.append(threelayerlink_bidirectional_bias_storage[layer_number][node_number][node_number])
                size_t = threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number][0].shape
                size_b = threelayerlink_bidirectional_bias_storage[layer_number][node_number][node_number][0].shape
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
                preprocess_1 = keras.layers.Dense(layer_density)(node_input)
                processed_input_node = keras.layers.Dense(layer_density)(preprocess_1)
                processed_input.append(processed_input_node)
                
            #processed_input.remove(processed_input[0])
            #processed_input2 = processed_input
            
            #for layer in processed_input:
            #    merge = layers.concatenate(merge, layer)
            #    processed_input2.remove(processed_input2[0])
            processed_input_initialise = processed_input[:]
            
                
            if permutation_count > 1:
                print(type(processed_input[0]))
                #print(processed_input[0].shape)
                #print(processed_input[1].shape)
                
                merged_input = keras.layers.concatenate([processed_input[0], processed_input[1]])#, axis=1) #TypeError: concatenate() got multiple values for argument 'axis'
                processed_input.pop(0)
                
                for i in range(permutation_count):
                    merged_input = keras.layers.concatenate([processed_input[0], merged_input])#, axis=1) #TypeError: concatenate() got multiple values for argument 'axis'
                    processed_input.pop(0)
                    
                    if len(processed_input) == 0:
                        break
            else:
                merged_input = processed_input[0]

            output = keras.layers.Dense(layer_density, activation='softmax')(merged_input)

            model = keras.Model(processed_input_initialise, output)
            model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['acc'])
            
            for node_number in node_permutation:
                print(len(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number]))
                training_input_nodes.append(np.array(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number]))
                print(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number])
                print(len(training_input_nodes))
                
                
                #print(processed_input[0].shape)
                #print(processed_input[1].shape)
            
            training_output_node = np.array(threelayerlink_bidirectional_tangent_storage[layer_number][5][5])
            
            
            # ([text, question], answers 
            # DEBUG
            # training_input_nodes
            #  expected shape=(None, 2, 16), found shape=(2, 16)
    
            # Check all dimensions
            
            print(training_input_nodes[0].shape)
            print(training_output_node.shape)
            
            # 
            model.fit(training_input_nodes, training_output_node, epochs=10, batch_size=1)
            
            environment = []
            for training_input_node in training_input_nodes:
                environment.append(training_input_node)
            #environment = np.array(environment)
            
            print(environment)
            #print(environment[0].shape)
            
            
           
            D5_link = model.predict(environment)
            print(permutation_count)
            print(permutation_counter)
            print(layer_number)
            tangent_collection[permutation_count][permutation_counter][layer_number].append(D5_link[0])
            
            #print(D5_link)
            
            
            # BIAS
            
            
            processed_input = []
                     
            for node_number in node_permutation:
                
                node_input = keras.Input(shape=input_bias_size,
                    dtype='int32',
                    name='tangent')
                preprocess_1 = keras.layers.Dense(layer_density)(node_input)
                processed_input_node = keras.layers.Dense(layer_density)(preprocess_1)
                processed_input.append(processed_input_node)

            processed_input_initialise = processed_input[:]
            
            if permutation_count > 1:
                merged_input = keras.layers.concatenate([processed_input[0], processed_input[1]])#, axis=-1)
                processed_input.pop(0)
                
                for i in range(permutation_count):
                    merged_input = keras.layers.concatenate([processed_input[0], merged_input])# , axis=-1)
                    processed_input.pop(0)
                    
                    if len(processed_input) == 0:
                        break
            else:
                merged_input = processed_input[0]

            output = keras.layers.Dense(layer_density, activation='softmax')(merged_input)
                
            model = keras.Model(processed_input_initialise, output)
            model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['acc'])

            training_input_nodes = []
            bias_node = []
            
            for node_number in node_permutation:
                training_input_nodes.append(np.array(threelayerlink_bidirectional_bias_storage[layer_number][node_number][node_number]))
            
            #training_input_nodes = np.array(training_input_nodes)
            training_output_node = np.array(threelayerlink_bidirectional_bias_storage[layer_number][5][5])
            
            print(training_input_nodes[0][0].shape)
            print(training_output_node.shape)
            model.fit(training_input_nodes, training_output_node)  # <-----------------------

            environment = []
            for training_input_node in training_input_nodes:
                environment.append(training_input_node)
            #environment = np.array(environment)
            
            #print(environment)
           #print(environment.shape)
           
        
            print(permutation_count)
            print(permutation_counter)
            print(layer_number)
            D5_link_bias = model.predict(environment)
            bias_collection[permutation_count][permutation_counter][layer_number].append(D5_link_bias[0])
            
        #permutation_counter += 1
                    


#data_extraction_5_preprocess

print("===========================================================================================")
#data_extraction_5_preprocess

def relu(x):
    return np.maximum(0, x)

node_collection = []
for i in range(1, NETWORK_ORDER):
    node_collection.append(i)
    
inference_total = []
inference_total.append([])

#for permutation_count in range(1, NETWORK_ORDER): 
#    permutation_counter = 0
#    node_permutations = findsubsets(node_collection, permutation_count)
#    for node_permutation in node_permutations:
#        inference_total[permutation_count].append([])
#        permutation_counter += 1
        
# TESTLOOP   
inference_total = []
for permutation_count in range(0, 99): 
    inference_total.append([])
    for permutation_counter in range(0, 99):
        inference_total[permutation_count].append([])
  
#1 4


# CHECK
inference_combinatoric = []  
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1   
        #permutation_counter += 1
        print([permutation_count, node_permutation])
        
        print(tangent_collection[permutation_count][permutation_counter][1][0].shape)
        print(tangent_collection[permutation_count][permutation_counter][3][0].shape)
        print(tangent_collection[permutation_count][permutation_counter][2][0].shape)
        print(bias_collection[permutation_count][permutation_counter][1][0].shape)
        print(bias_collection[permutation_count][permutation_counter][2][0].shape)
        print(bias_collection[permutation_count][permutation_counter][3][0].shape)
        
        #print("L:" + str(layer_number - 1 + 1))
        #print(bias_collection[permutation_count][permutation_counter][layer_number][0].shape)
        #print(tangent_collection[permutation_count][permutation_counter][layer_number][0].shape)
        
        
  
#exit()
  
  
  
# CHECK
inference_combinatoric = []  
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1   
        for layer_number in range(1, INTERLINK_DENSITY + 1):  
        #permutation_counter += 1
            print([permutation_count, node_permutation, layer_number])
            print(len(tangent_collection[permutation_count][permutation_counter][layer_number]))
            print(len(bias_collection[permutation_count][permutation_counter][layer_number]))
            print("L:" + str(layer_number - 1 + 1))
            print(bias_collection[permutation_count][permutation_counter][layer_number][0].shape)
            print(tangent_collection[permutation_count][permutation_counter][layer_number][0].shape)
        
#print()
#for permutation_count in range(1, NETWORK_ORDER): 
    
#   permutation_counter = 0
#    node_permutations = findsubsets(node_collection, permutation_count)
#    
#    for node_permutation in node_permutations:
#        permutation_counter += 1
#        
#        print(permutation_count)
#        print(permutation_counter)
#        print(node_permutation)

#        print(len(tangent_collection[permutation_count][permutation_counter][1]))
#        print(len(tangent_collection[permutation_count][permutation_counter][2]))
#        print(len(tangent_collection[permutation_count][permutation_counter][3]))
#        print(len(bias_collection[permutation_count][permutation_counter][1]))
#        print(len(bias_collection[permutation_count][permutation_counter][2]))
#        print(len(bias_collection[permutation_count][permutation_counter][3]))
   
#exit()    
print("***************************************************************************")       

print(bias_collection[permutation_count][permutation_counter][layer_number][0].shape)
print(tangent_collection[permutation_count][permutation_counter][layer_number][0].shape)

inference_combinatoric = []  
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1   


for permutation_count in range(1, NETWORK_ORDER): 
#for permutation_count in range(1, NETWORK_ORDER):
    permutation_counter = 0
    
    node_permutations = findsubsets(node_collection, permutation_count)
    
    #for node_permutation in node_permutations:
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1
    
        
        #for layer_number in range(1, INTERLINK_DENSITY + 1):  
            #print(len(tangent_collection[permutation_count][permutation_counter][layer_number]))
            #print(len(bias_collection[permutation_count][permutation_counter][layer_number]))
            
            
        for m in range(100):
            #sample_data = data_extraction_5_preprocess[m]
            #print("----------Manual Matrix-----------")
            #print(permutation_count)
            #print(permutation_counter)
            #print("---------------------------------------")
            sample_data = np.ones(100)
            sub_result1 = relu((tangent_collection[permutation_count][permutation_counter][1][0].transpose() @ sample_data) + bias_collection[permutation_count][permutation_counter][1][0])
            sub_result2 = relu((tangent_collection[permutation_count][permutation_counter][2][0].transpose() @ sub_result1) + bias_collection[permutation_count][permutation_counter][2][0])
            sub_result3 = ((tangent_collection[permutation_count][permutation_counter][3][0].transpose() @ sub_result2) + bias_collection[permutation_count][permutation_counter][3][0])
            inference_total[permutation_count][permutation_counter].append(sub_result3[0])
            
        inference_total[permutation_count][permutation_counter] = np.array(inference_total[permutation_count][permutation_counter])
        temperature_extraction_preprocess = np.eye(100)
        score = np.sqrt(np.mean(np.square(inference_total[permutation_count][permutation_counter] - temperature_extraction_preprocess)))
        print("Nodes " + str(node_permutation) + " towards D5 link: " + str(score))
        

#        permutation_counter += 1
  

exit()      
    
    
    
        
sample_data = data_extraction_5_preprocess[m]
sub_result1 = relu((tangent_collection[permutation_count][permutation_counter][1][0].transpose() @ sample_data) + bias_collection[permutation_count][permutation_counter][1][0])
sub_result2 = relu((tangent_collection[permutation_count][permutation_counter][2][0].transpose() @ sub_result1) + bias_collection[permutation_count][permutation_counter][2][0])
sub_result3 = ((tangent_collection[permutation_count][permutation_counter][3][0].transpose() @ sub_result2) + bias_collection[permutation_count][permutation_counter][3][0])
#print(sub_result3)

##### DEBUG SIMULATION


#tangent_collection[permutation_count][permutation_counter][1][0].transpose() @ sample_data) + bias_collection[permutation_count][permutation_counter][1][0])
#tangent_collection



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








################################################################################################
######## MANUAL MATRIX COMPUTATION #############################################################


node_collection = []
for i in range(1, NETWORK_ORDER):
    node_collection.append(i)
    
inference_total = []
inference_total.append([])
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter = 0
    inference_total.append([])
    node_permutations = findsubsets(node_collection, permutation_count)
    for node_permutation in node_permutations:
        permutation_counter += 1
        inference_total[permutation_count].append([])

for permutation_count in range(1, NETWORK_ORDER): 
    
    permutation_counter = 0
    node_permutations = findsubsets(node_collection, permutation_count)
    
    for node_permutation in node_permutations:
        permutation_counter += 1
        
        print(len(tangent_collection[permutation_count][permutation_counter][1]))
        print(len(tangent_collection[permutation_count][permutation_counter][2]))
        print(len(tangent_collection[permutation_count][permutation_counter][3]))
        print(len(bias_collection[permutation_count][permutation_counter][1]))
        print(len(bias_collection[permutation_count][permutation_counter][2]))
        print(len(bias_collection[permutation_count][permutation_counter][3]))

        for m in range(duration):
            sample_data = data_extraction_5_preprocess[m]
            sub_result1 = relu((tangent_collection[permutation_count][permutation_counter][1][0].transpose() @ sample_data) + bias_collection[permutation_count][permutation_counter][1][0])
            # IndexError: list index out of range occurs here but not in scaledfunctionsystem.py
            # continue later
            sub_result2 = relu((tangent_collection[permutation_count][permutation_counter][2][0].transpose() @ sub_result1) + bias_collection[permutation_count][permutation_counter][2][0])
            sub_result3 = ((tangent_collection[permutation_count][permutation_counter][3][0].transpose() @ sub_result2) + bias_collection[permutation_count][permutation_counter][3][0])
            #print(sub_result3)
            #print(node_permutation)
            inference_total[permutation_count][permutation_counter].append(sub_result3[0])
        
        inference_total[permutation_count][permutation_counter] = np.array(inference_total[permutation_count][permutation_counter])
        score = np.sqrt(np.sum(np.square(inference_total[permutation_count][permutation_counter] - temperature_extraction_preprocess)))
        print("Nodes " + str(node_permutation) + " towards D5 link: " + str(score))
        #permutation_counter += 1
        
################################################################################################
# same bug
# data_extraction_5_preprocess = raw_data[:-delay, [12, 13]]
################################################################################################
 
            
#print(node_permutation)




exit()  




################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################

temperature_extraction_preprocess = 0

inference_combinatoric = []

for permutation_count in range(1, NETWORK_ORDER): 
    
    permutation_counter = 0
    
    for node_permutation in findsubsets(node_collection, permutation_count):

        tangent_link_1 = tangent_collection[permutation_count][permutation_counter][1][0]
        tangent_link_2 = tangent_collection[permutation_count][permutation_counter][2][0]
        tangent_link_3 = tangent_collection[permutation_count][permutation_counter][3][0]
        bias_link_1 = bias_collection[permutation_count][permutation_counter][1][0]
        bias_link_2 = bias_collection[permutation_count][permutation_counter][2][0]
        bias_link_3 = bias_collection[permutation_count][permutation_counter][3][0]
      
        #print(loop_counter)
        #p#rint(permutation_count)
        #print(node_permutation)
        #inference_combinatoric = []
        print(tangent_link_1.shape)
        print(tangent_link_2.shape)
        print(tangent_link_3.shape)
        print(bias_link_1.shape)
        print(bias_link_2.shape)
        print(bias_link_3.shape)
        
        exit()
        
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
    
        permutation_counter += 1
        
        
        
        
        




