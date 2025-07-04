import keras
import itertools
import numpy as np
#from StarSystems.index import INTERLINK_DENSITY


NETWORK_ORDER = 5
INTERLINK_DENSITY = 3

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
print("-----------------------------------------------------------------------")
################################################################################
# <----> MILEPOINT FULLY FUNCTIONAL <---->
################################################################################

################################################################################
# DEBUG UNTIL MILEPOINT LINE 940
################################################################################


np.array(threelayerlink_bidirectional_bias_storage[k][i][i])

np.array(threelayerlink_bidirectional_bias_storage[k][i][i])

permutation_counter = 0
for permutation_count in range(1, NETWORK_ORDER): 
    permutation_counter += 1
    for node_permutation in findsubsets(node_collection, permutation_count):
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
                preprocess_1 = layers.Dense(layer_density)(node_input)
                processed_input_node = layers.Dense(layer_density)(preprocess_1)
                processed_input.append(processed_input_node)
                
            #processed_input.remove(processed_input[0])
            #processed_input2 = processed_input
            
            #for layer in processed_input:
            #    merge = layers.concatenate(merge, layer)
            #    processed_input2.remove(processed_input2[0])
                
            if permutation_count > 1:
                merged_input = layers.concatenate(processed_input[0], processed_input[1], axis=-1)
                processed_input.pop(0)
                
                for i in range(permutation_count):
                    merged_input = layers.concatenate(processed_input[0], merged_input, axis=-1)
                    processed_input.pop(0)
                    
                    if len(processed_input) == 0:
                        break
            else:
                merged_input = processed_input[0]

            output = layers.Dense(layer_density, activation='sigmoid')(merged_input)

            model = keras.Model(processed_input, output)
            model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['acc'])
            
            for node_number in node_permutation:
                print(len(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number]))
                training_input_nodes.append(np.array(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number]))
                print(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number])
                print(len(training_input_nodes))
            
            training_output_node = np.array(threelayerlink_bidirectional_tangent_storage[layer_number][5][5])
            
            
            # ([text, question], answers 
            # DEBUG
            # training_input_nodes
            #  expected shape=(None, 2, 16), found shape=(2, 16)
    
            # Check all dimensions
            model.fit(training_input_nodes, training_output_node, epochs=10, batch_size=1)
            
            environment = []
            for training_input_node in training_input_nodes:
                environment.append(training_input_node[0])
            environment = np.array(environment)
            
            
            # environment shape fault
     
            D5_link = model.predict(environment)
            tangent_collection[permutation_count][permutation_counter][layer_number].append(D5_link)
            
            print(D5_link)
            
            
            # BIAS
            
            processed_input = []
                     
            for node_number in node_permutation:
                
                node_input = keras.Input(shape=input_bias_size,
                    dtype='int32',
                    name='tangent')
                preprocess_1 = layers.Dense(layer_density)(node_input)
                processed_input_node = layers.Dense(layer_density)(preprocess_1)
                processed_input.append(processed_input_node)

            if permutation_count > 1:
                merged_input = layers.concatenate(processed_input[0], processed_input[1], axis=-1)
                processed_input.pop(0)
                
                for i in range(permutation_count):
                    merged_input = layers.concatenate(processed_input[0], merged_input, axis=-1)
                    processed_input.pop(0)
                    
                    if len(processed_input) == 0:
                        break
            else:
                merged_input = processed_input[0]

            output = layers.Dense(layer_density, activation='sigmoid')(merged_input)
                
            model = keras.Model(processed_input, output)
            model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['acc'])

            training_input_nodes = []
            bias_node = []
            
            for node_number in node_permutation:
                training_input_nodes.append(np.array(threelayerlink_bidirectional_bias_storage[layer_number][node_number][node_number]))
            
            #training_input_nodes = np.array(training_input_nodes)
            training_output_node = np.array(threelayerlink_bidirectional_bias_storage[layer_number][5][5])
            
            model.fit(training_input_nodes, training_output_node)  # <-----------------------

            environment = []
            for training_input_node in training_input_nodes:
                environment.append(training_input_node[0])
            environment = np.array(environment)
            
            D5_link_bias = model.predict(environment)
            bias_collection[permutation_count][permutation_counter][layer_number].append(D5_link_bias)
                    

print("===========================================================================================")
