####################################################################
#
# SYSTEM OF LINK-NETWORKS IN FULL GENERALITY
# 
####################################################################


# TWEAK
# PROPER OOP, I.E. CLEAN CODE, AFTER FUNCTIONALITY

# FIX NEURALNET LAYERS TO DENSE
# HYPERPARAMETER STANDARDIZATION
# PERFORM OPTIMIZATION OVER THE BELOW HYPERPARAMETERS

# SIMULATE ENVIRONMENT OF DEPLOYMENT FOR CONSTRUCTION

# ACCOUNT FOR LINK LAYER AND PARAMETER PER LAYER COUNT
# SIMPLE -> COMPLEX, PARALLEL TO PROPERTIES AND CLARIFICATION ENVIRONMENT
# SIMPLE FIRST SIMULATION

# DEEP LEARNING STARSYSTEM CONSTRUCTION
# HIGH LEVEL LIBRARIES FOR INITIAL CONSTRUCTION AND TWEAKS
# DETAILED PROGRAMMING CONSTRUCTS FOR NEW DEEP LEARNING (BACKPROPAGATION OVER COMPLETE LINK-GRAPH)
# CLEAN CODE COMES AFTER DEMONSTRATED FUNCTIONALITY COMES AFTER DESIGN
# D1
#E.G., parameter_count_list = [9,9,9]
#parameter_count_list

#class DenseLinkNetwork(parameter_count_list, activation):
#    
#    def __init__(self):
#        
#        self.parameter_count_list = parameter_count_list
#        self.activation = activation        
#    def integrator(self):
    
#inputs = keras.Input(shape=(sequence_length, data_extraction_4.shape[-1]))
#x = keras.layers.Dense(parameter_count_list[0], activation=activation)(inputs)
#x = keras.layers.Dense(parameter_count_list[0], activation="activation)(inputs)

# CONSTRUCT CLASSES

# Optimization of hyperparameters 
            
# Classes for link between nodes
# Classes for link in nodes
# Classes for complete graph construction
# simulate environment

#for n in range(NODE_COUNT):
#    for t in range(TIME_STEPS):
#        A[n,t] = random.normalvariate(mu = n, sigma = t)

# FULL IMPLEMENTATION IN CONVENTIONAL DL FRAMEWORKS

import random
import numpy as np
import keras
import math

from dataloader3 import TIME_STEPS

sequence_length = 120

# HYPERPARAMETER RESTRICTION (GRID SEARCH OPTIMIZE)
NODE_COUNT = 1000
NODE_MAGNITUDE = 1000000
NODE_DIMENSION = 100
INTERLINK_DENSITY = 10 # layer_count interlink
INTRALINK_DENSITY = 10 # layer_count intralink
PARAMETER_COUNT = 20
OUTPUT_MAGNITUDE = 1
ACTIVATION = 'relu'
OPTIMIZER = "rmsprop"
LOSS="mse"
METRIC=["mae"]
EPOCHS = 3
INTRALINK_N = 1000
LEARN_DEPLOY_RATIO = 0.7
PREPROCESS_LEARN_DEPLOY_RATIO = 0.9
INFERENCE_MAGNITUDE_RATIO = 1 - LEARN_DEPLOY_RATIO
LEARN_MAGNITUDE = math.floor(LEARN_DEPLOY_RATIO * NODE_MAGNITUDE)
PRETEST_MAGNITUDE = math.floor(PREPROCESS_LEARN_DEPLOY_RATIO * LEARN_MAGNITUDE)
INTRALINK_N_DEPLOY = 300
BATCH_SIZE = 128
DEPLOY_MAGNITUDE = 30000

Node_list = []
for j in range(NODE_COUNT):
    Node_environment = np.zeros(NODE_DIMENSION, NODE_MAGNITUDE)
    for n in range(NODE_DIMENSION):
        for t in range(NODE_MAGNITUDE + DEPLOY_MAGNITUDE):
            Node_environment[n,t] = random.normalvariate(mu = n, sigma = t)
    Node_list.append(Node_environment)
 

Node_test_list = [] 
for j in range(NODE_COUNT):
    Node_test_list.append(Node_list[j][:])

########################################################################
########################################################################

multilayerlink_bidirectional_tangent_storage = []
for i in range(INTERLINK_DENSITY + 1):
    multilayerlink_bidirectional_tangent_storage.append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        multilayerlink_bidirectional_tangent_storage[i].append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        for k in range(NODE_COUNT + 1):
            multilayerlink_bidirectional_tangent_storage[i][j].append([])

multilayerlink_bidirectional_bias_storage = []
for i in range(INTERLINK_DENSITY + 1):
    multilayerlink_bidirectional_bias_storage.append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        multilayerlink_bidirectional_bias_storage[i].append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        for k in range(NODE_COUNT + 1):
            multilayerlink_bidirectional_bias_storage[i][j].append([])


########################################################################
#Node_tester = Node_n_sample[:,LEARN_MAGNITUDE:]

for n in range(INTRALINK_N):
    for i in range(NODE_COUNT):
        
        Node_n_sample = Node_list[i][math.floor(NODE_MAGNITUDE * n / INTRALINK_N), math.floor(NODE_MAGNITUDE * (n + 1) / INTRALINK_N)]
        Node_learner = Node_n_sample[:,:LEARN_MAGNITUDE]
        Node_prelearner = Node_learner[:,PRETEST_MAGNITUDE:]
        Node_pretester = Node_learner[:,:PRETEST_MAGNITUDE]

        #LEARN_MAGNITUDE
        #math.floor(PRETEST_MAGNITUDE * LEARN_MAGNITUDE)
        #Node_test = Node_n_sample[:,:LEARN_MAGNITUDE]
        
        #Node_test = Node_prelearner[:,:learn_magnitude]
        #Node_test = Node_prelearner[:,:learn_magnitude]

        #Node_pretest = Node_n_sample[:,:LEARN_MAGNITUDE]
        
        inputs = keras.Input(shape=(sequence_length, Node_learner.shape[-1]))
        x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(inputs)
        for k in range(1, INTRALINK_DENSITY):
            x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(x)
        outputs = keras.layers.Dense(OUTPUT_MAGNITUDE)(x)
        Intra_D = keras.Model(inputs, outputs)
        #callbacks = [
        #    keras.callbacks.ModelCheckpoint("jena_dense.keras",
        #    save_best_only=True)
        #    ]
        Intra_D.compile(optimizer=OPTIMIZER, loss=LOSS, metrics=METRIC)
        Intra_D.fit(Node_prelearner, epochs= EPOCHS, validation_data=Node_pretester)
        #    callbacks=callbacks)
        #Intra_D = keras.models.load_model("jena_dense.keras")
        #print(f"Test MAE: {Intra_D.evaluate(test_node_5)[1]:.2f}")

        for j in range(1, INTRALINK_DENSITY + 1):
            multilayerlink_bidirectional_tangent_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[0]))  # j-1        
            multilayerlink_bidirectional_bias_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[1]))
            
########################################################################
# CONSTRUCT DEPLOYMENT ENVIRONMENT

new_multilayerlink_bidirectional_tangent_storage = []
for i in range(INTRALINK_DENSITY + 1):
    new_multilayerlink_bidirectional_tangent_storage.append([])
for i in range(INTRALINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        new_multilayerlink_bidirectional_tangent_storage[i].append([])
for i in range(INTRALINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        for k in range(NODE_COUNT + 1):
            new_multilayerlink_bidirectional_tangent_storage[i][j].append([])

new_multilayerlink_bidirectional_bias_storage = []
for i in range(INTRALINK_DENSITY + 1):
    new_multilayerlink_bidirectional_bias_storage.append([])
for i in range(INTRALINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        new_multilayerlink_bidirectional_bias_storage[i].append([])
for i in range(INTRALINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        for k in range(NODE_COUNT + 1):
            new_multilayerlink_bidirectional_bias_storage[i][j].append([])

  
########################################################################
#new_multilayerlink_bidirectional_bias_storage
#new_multilayerlink_bidirectional_tangent_storage


for n in range(INTRALINK_N_DEPLOY):
    
    for i in range(1, NODE_COUNT + 1):
    
        Node_n_sample = Node_list[i][NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * n / INTRALINK_N_DEPLOY) : NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * (n + 1) / INTRALINK_N_DEPLOY), :]
        
        #Node_prelearner = Node_n_sample[:,PRETEST_MAGNITUDE :]
        #Node_pretester = Node_n_sample[:,: PRETEST_MAGNITUDE]
        #NODE_COUNT - LEARN_MAGNITUDE
        #Node_learner = Node_n_sample[:,:LEARN_MAGNITUDE]
        #Node_prelearner = Node_learner[:,PRETEST_MAGNITUDE:]
        #Node_pretester = Node_learner[:,:PRETEST_MAGNITUDE]
        #Node_prelearner = Node_learner[:,:PRETEST_MAGNITUDE]
        #LEARN_MAGNITUDE
        #math.floor(PRETEST_MAGNITUDE * LEARN_MAGNITUDE)
        #Node_test = Node_n_sample[:,:LEARN_MAGNITUDE]
        #Node_test = Node_prelearner[:,:learn_magnitude]
        #Node_test = Node_prelearner[:,:learn_magnitude]
        #NODE_COUNT - LEARN_MAGNITUDE
        #Node_pretest = Node_n_sample[:,:LEARN_MAGNITUDE]
        
        inputs = keras.Input(shape=(sequence_length, Node_n_sample.shape[-1]))
        x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(inputs)
        for k in range(1, INTRALINK_DENSITY):
            x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(x)
        outputs = keras.layers.Dense(OUTPUT_MAGNITUDE)(x)
        Intra_D = keras.Model(inputs, outputs)
        #callbacks = [
        #    keras.callbacks.ModelCheckpoint("jena_dense.keras",
        #    save_best_only=True)
        #    ]
        Intra_D.compile(optimizer=OPTIMIZER, loss=LOSS, metrics=METRIC)
        Intra_D.fit(Node_n_sample, epochs= EPOCHS)
        #    callbacks=callbacks)
        #Intra_D = keras.models.load_model("jena_dense.keras")
        #print(f"Test MAE: {Intra_D.evaluate(test_node_5)[1]:.2f}")

        for j in range(1, INTRALINK_DENSITY + 1):
            new_multilayerlink_bidirectional_tangent_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[0]))  # j-1        
            new_multilayerlink_bidirectional_bias_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[1]))
        
#INFERENCE_MAGNITUDE
#Node_n_sample = Node_list[i][NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * n / INTRALINK_N_DEPLOY) : NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * (n + 1) / INTRALINK_N_DEPLOY), :]
  
   
for k in range(1, INTRALINK_DENSITY + 1):
    for i in range(1, NODE_COUNT + 1):
        for j in range(1, NODE_COUNT + 1):
            if i == j:
                continue
            
            print("Start INTERLINK CONSTRUCTION")

            input_tangent_size = multilayerlink_bidirectional_tangent_storage[k][i][i][0].shape
            output_tangent_size = multilayerlink_bidirectional_tangent_storage[k][j][j][0].shape
            input_bias_size = multilayerlink_bidirectional_bias_storage[k][i][i][0].shape
            output_bias_size = multilayerlink_bidirectional_bias_storage[k][j][j][0].shape
        
            Inter_Node_tangent = keras.models.Sequential()
            for i in range(INTERLINK_DENSITY - 1):
                Inter_Node_tangent.add(keras.layers.Dense(output_tangent_size[0] * output_tangent_size[1]))
            Inter_Node_tangent.add(keras.layers.Dense(output_tangent_size[1]))
            Inter_Node_tangent.compile(optimizer=OPTIMIZER, loss=LOSS, metrics=METRIC) 

            Inter_Node_bias = keras.models.Sequential()
            for i in range(INTERLINK_DENSITY):
                Inter_Node_bias.add(keras.layers.Dense(output_bias_size[0]))
            Inter_Node_bias.compile(optimizer=OPTIMIZER, loss=LOSS, metrics=METRIC)

            multilayerlink_bidirectional_tangent_storage_kii = np.array(multilayerlink_bidirectional_tangent_storage[k][i][i])
            multilayerlink_bidirectional_tangent_storage_kjj = np.array(multilayerlink_bidirectional_tangent_storage[k][j][j])

            Inter_Node_tangent.fit(multilayerlink_bidirectional_tangent_storage_kii, multilayerlink_bidirectional_tangent_storage_kjj, epochs=EPOCHS, batch_size=BATCH_SIZE)
            
            new_multilayerlink_bidirectional_tangent_storage_kii = np.array(new_multilayerlink_bidirectional_tangent_storage[k][i][i])
            new_multilayerlink_bidirectional_bias_storage_kjj = np.array(new_multilayerlink_bidirectional_bias_storage[k][j][j])
            
            Emergent_Inter_Node_tangent = Inter_Node_tangent.predict(multilayerlink_bidirectional_tangent_storage_kii) ####
            print(type(Emergent_Inter_Node_tangent[0]))
            multilayerlink_bidirectional_tangent_storage[k][i][j].append(Emergent_Inter_Node_tangent[0])
            
            multilayerlink_bidirectional_bias_storage_kii = np.array(multilayerlink_bidirectional_bias_storage[k][i][i])
            multilayerlink_bidirectional_bias_storage_kjj = np.array(multilayerlink_bidirectional_bias_storage[k][j][j])

            Inter_Node_bias.fit(multilayerlink_bidirectional_bias_storage_kii, multilayerlink_bidirectional_bias_storage_kjj, epochs=EPOCHS, batch_size=BATCH_SIZE) 
            
            new_multilayerlink_bidirectional_bias_storage_kii = np.array(new_multilayerlink_bidirectional_bias_storage[k][i][i])
            new_multilayerlink_bidirectional_bias_storage_kjj = np.array(new_multilayerlink_bidirectional_bias_storage[k][j][j])
            
            Emergent_Inter_Node_bias  = Inter_Node_bias.predict(new_multilayerlink_bidirectional_bias_storage_kii)  ####
            print(type(Emergent_Inter_Node_bias[0]))
            multilayerlink_bidirectional_bias_storage[k][i][j].append(Emergent_Inter_Node_bias[0])

            print("==========================================================================================")

import itertools

# COLLECT NODES
node_collection = []
for i in range(1, NODE_COUNT):
    node_collection.append(i)  
    
def findsubsets(s, n):
    result = list(itertools.combinations(s, n))
    return result

# TEMPORARY SOLUTION
tangent_collection = []
bias_collection = []    

#TESTLOOP
for permutation_count in range(1, NODE_COUNT): 
    permutation_counter = 0
    
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1
        
    for node_permutation_counter in range(0, permutation_counter + 99):
        tangent_collection[permutation_count].append([])
        bias_collection[permutation_count].append([]) 
        for layer_number in range(0, INTERLINK_DENSITY + 99): 
            tangent_collection[permutation_count][node_permutation_counter].append([])
            bias_collection[permutation_count][node_permutation_counter].append([]) 
            print("STORAGE INITIALIZATION")
         
# TESTLOOP   
# ABOVE: TRAIN INTERLINK ON DATAPART, TEST INTERLINK IN DATAPART
# REPEAT SAME PROCESS BELOW

inference_total = []
for permutation_count in range(1, NODE_COUNT): 
    inference_total.append([])
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1
    for permutation_counter_iter in range(0, permutation_counter + 99):
        inference_total[permutation_count].append([])

for permutation_count in range(1, NODE_COUNT): 
    permutation_counter = 0
    
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1
        
        for layer_number in range(1, INTERLINK_DENSITY + 1):  
            
            print(permutation_count)
            print(permutation_counter)
            print(node_permutation)
            print(layer_number)
            
            multilayerlink_bidirectional_tangent_storage_kii = []  
            multilayerlink_bidirectional_bias_storage_kii = []   

            for node_number in node_permutation:

                multilayerlink_bidirectional_tangent_storage_kii.append(multilayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number])
                multilayerlink_bidirectional_bias_storage_kii.append(multilayerlink_bidirectional_bias_storage[layer_number][node_number][node_number])
                size_t = multilayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number][0].shape
                size_b = multilayerlink_bidirectional_bias_storage[layer_number][node_number][node_number][0].shape
            prime_threelayerlink_bidirectional_tangent_storage_kii = np.array(multilayerlink_bidirectional_tangent_storage_kii)
            prime_threelayerlink_bidirectional_bias_storage_kii = np.array(multilayerlink_bidirectional_bias_storage_kii)
            #
            input_tangent_size = size_t
            input_bias_size = size_b  
            output_tangent_size = multilayerlink_bidirectional_tangent_storage[layer_number][NODE_COUNT][NODE_COUNT][0].shape
            output_bias_size = multilayerlink_bidirectional_bias_storage[layer_number][NODE_COUNT][NODE_COUNT][0].shape
            prime_input_tangent_size = prime_threelayerlink_bidirectional_tangent_storage_kii.shape
            prime_input_bias_size = prime_threelayerlink_bidirectional_bias_storage_kii.shape
            prime_output_tangent_size = output_tangent_size
            prime_output_bias_size = output_bias_size

            processed_input = []
            training_input_nodes = []
            testing_input_nodes = []
            bias_node = []
            
            # TANGENT
            # TWEAK UNTIL FUNCTIONAL
            layer_density = output_tangent_size[1] #* output_tangent_size[1] # or output_tangent_size[1] or output_tangent_size[0] 
            
            for node_number in node_permutation:
                
                node_input = keras.Input(shape=input_tangent_size,
                    dtype='int32',
                    name='tangent')
                preprocess_1 = keras.layers.Dense(layer_density)(node_input)
                processed_input_node = keras.layers.Dense(layer_density)(preprocess_1)
                processed_input.append(processed_input_node)
                
            #processed_input.remove(processed_input[0])
            #processed_input2 = processed_input
            processed_input_initialise = processed_input[:]
            
            #for layer in processed_input:
            #    merge = layers.concatenate(merge, layer)
            #    processed_input2.remove(processed_input2[0])
            
            if permutation_count > 1:
                merged_input = keras.layers.concatenate([processed_input[0], processed_input[1]])
                processed_input.pop(0)
                
                for i in range(permutation_count):
                    merged_input = keras.layers.concatenate([processed_input[0], merged_input])  
                    processed_input.pop(0)
                    
                    if len(processed_input) == 0:
                        break
            else:
                merged_input = processed_input[0]

            output = keras.layers.Dense(layer_density, activation=ACTIVATION)(merged_input)

            model = keras.Model(processed_input_initialise, output)
            model.compile(optimizer=OPTIMIZER,
                loss=LOSS,
                metrics=METRIC)
            
            for node_number in node_permutation:
                #print(len(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number]))
                training_input_nodes.append(np.array(multilayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number]))
                #print(threelayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number])
                #print(len(training_input_nodes))
            
            training_output_node = np.array(multilayerlink_bidirectional_tangent_storage[layer_number][NODE_COUNT][NODE_COUNT])
            
            # ([text, question], answers 
            # DEBUG
            # training_input_nodes
            #  expected shape=(None, 2, 16), found shape=(2, 16)
            
            #INFERENCE_SET
            #(2, 16)
            #(16, 16)
            #(16, 1)
            #(16,)
            #(16,)
            #(1,)
    
            # Check all dimensions
            
            #print(training_input_nodes[0][0].shape)
            #print(training_output_node.shape)
            
            # dDEBUG
            model.fit(training_input_nodes, training_output_node, epochs=EPOCHS, batch_size=BATCH_SIZE)
            
            #environment = np.array(environment)
            for node_number in node_permutation:
                testing_input_nodes.append(np.array(new_multilayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number]))
            
            environment = []
            for testing_input_node in testing_input_nodes:
                environment.append(testing_input_node)
                
            #environment = np.array(environment)
            #for node_number in node_permutation:
            #    testing_input_nodes.append(np.array(new_multilayerlink_bidirectional_tangent_storage[layer_number][node_number][node_number]))
                
           
            print("COMPUTED D_NODE_COUNT TANGENT LINK")
            D_final_link_tangent = model.predict(environment)

            tangent_collection[permutation_count][permutation_counter][layer_number].append(D_final_link_tangent[0])
            
            #print(D5_link)
            
            # BIAS
            # TWEAK UNTIL FUNCTIONAL
            processed_input = []
            
            layer_density = output_bias_size[0] # or output_bias_size[1]  

            for node_number in node_permutation:
                
                node_input = keras.Input(shape=input_bias_size,
                    dtype='int32',
                    name='tangent')
                preprocess_1 = keras.layers.Dense(layer_density)(node_input)
                processed_input_node = keras.layers.Dense(layer_density)(preprocess_1)
                processed_input.append(processed_input_node)

            processed_input_initialise = processed_input[:]
            
            if permutation_count > 1:
                merged_input = keras.layers.concatenate([processed_input[0], processed_input[1]])
                processed_input.pop(0)
                
                for i in range(permutation_count):
                    merged_input = keras.layers.concatenate([processed_input[0], merged_input])
                    processed_input.pop(0)
                    
                    if len(processed_input) == 0:
                        break
            else:
                merged_input = processed_input[0]
                
            layer_density = output_bias_size[0]

            output = keras.layers.Dense(layer_density, activation=ACTIVATION)(merged_input)
                
            model = keras.Model(processed_input_initialise, output)
            model.compile(optimizer=OPTIMIZER,
                loss=LOSS,
                metrics=METRIC)

            training_input_nodes = []
            bias_node = []
            testing_input_nodes = []
            
            for node_number in node_permutation:
                training_input_nodes.append(np.array(multilayerlink_bidirectional_bias_storage[layer_number][node_number][node_number]))
            
            for node_number in node_permutation:
                testing_input_nodes.append(np.array(new_multilayerlink_bidirectional_bias_storage[layer_number][node_number][node_number]))
            
            
            #training_input_nodes = np.array(training_input_nodes)
            training_output_node = np.array(multilayerlink_bidirectional_bias_storage[layer_number][NODE_COUNT][NODE_COUNT])
            
            #print(training_input_nodes[0][0].shape)
            #print(training_output_node.shape)
            model.fit(training_input_nodes, training_output_node)  # <-----------------------

            environment = []
            for testing_input_node in testing_input_nodes:
                environment.append(testing_input_node) # TEST SET LATER
            #environment = np.array(environment)
            
            D_final_link_bias = model.predict(environment)
            bias_collection[permutation_count][permutation_counter][layer_number].append(D_final_link_bias[0])
            
            print("COMPUTED D_NODE_COUNT BIAS LINK")




# CONSTRUCT DEPLOYMENT ENVIRONMENT
###########################################################################
###########################################################################
###########################################################################


###########################################################################
###########################################################################

def relu(x):
    return np.maximum(0, x)

inference_total = []
inference_total.append([])
for permutation_count in range(1, NODE_COUNT): 
    permutation_counter = 0
    inference_total.append([])
    node_permutations = findsubsets(node_collection, permutation_count)
    for node_permutation in node_permutations:
        inference_total[permutation_count].append([])
        permutation_counter += 1

for permutation_count in range(1, NODE_COUNT): 
    permutation_counter = 0
    node_permutations = findsubsets(node_collection, permutation_count)
    for node_permutation in node_permutations:
        for m in range(NODE_MAGNITUDE):
            sample_data = Node_list[NODE_COUNT][m] #####
            sub_result1 = relu((tangent_collection[permutation_count][permutation_counter][1][0].transpose() @ sample_data) + bias_collection[permutation_count][permutation_counter][1][0])
            for n in range(2, INTERLINK_DENSITY):
                sub_result1 = relu((tangent_collection[permutation_count][permutation_counter][n][0].transpose() @ sub_result1) + bias_collection[permutation_count][permutation_counter][n][0])
            result = relu((tangent_collection[permutation_count][permutation_counter][INTERLINK_DENSITY][0].transpose() @ sub_result1) + bias_collection[permutation_count][permutation_counter][INTERLINK_DENSITY][0])
            inference_total[permutation_count][permutation_counter].append(result[0])
        
        inference_total[permutation_count][permutation_counter] = np.array(inference_total[permutation_count][permutation_counter])
        score = np.sqrt(np.mean(np.square(inference_total[permutation_count][permutation_counter] - Node_list[NODE_COUNT][:,-1])))
        print("Nodes " + str(node_permutation) + " towards D CONVOLUTED link: " + str(score))
        permutation_counter += 1
    






exit()














#sub_result3 = ((tangent_collection[permutation_count][permutation_counter][3][0].transpose() @ sub_result2) + bias_collection[permutation_count][permutation_counter][3][0])

inference_combinatoric = []  
for permutation_count in range(1, NODE_COUNT): 
    permutation_counter = 0
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1   


for permutation_count in range(1, NODE_COUNT): 

    permutation_counter = 0
    node_permutations = findsubsets(node_collection, permutation_count)

    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1

        for m in range(NODE_MAGNITUDE):

            sample_data = Node_list[permutation_count][m]
            sub_result1 = relu((tangent_collection[permutation_count][permutation_counter][1][0].transpose() @ sample_data) + bias_collection[permutation_count][permutation_counter][1][0])
            sub_result2 = relu((tangent_collection[permutation_count][permutation_counter][2][0].transpose() @ sub_result1) + bias_collection[permutation_count][permutation_counter][2][0])
            sub_result3 = ((tangent_collection[permutation_count][permutation_counter][3][0].transpose() @ sub_result2) + bias_collection[permutation_count][permutation_counter][3][0])
            inference_total[permutation_count][permutation_counter].append(sub_result3[0])
            
        inference_total[permutation_count][permutation_counter] = np.array(inference_total[permutation_count][permutation_counter])
        #temperature_extraction_preprocess = np.eye(100)
        score = np.sqrt(np.mean(np.square(inference_total[permutation_count][permutation_counter] - temperature_extraction_preprocess)))
        print("Nodes " + str(node_permutation) + " towards D5 link: " + str(score))












for permutation_count in range(1, NODE_COUNT): 
    
    permutation_counter = 0
    node_permutations = findsubsets(node_collection, permutation_count)
    
    for node_permutation in node_permutations:

        for m in range(duration):
            sample_data = data_extraction_5_preprocess[m]
            sub_result1 = relu((tangent_collection[permutation_count][permutation_counter][1][0].transpose() @ sample_data) + bias_collection[permutation_count][permutation_counter][1][0])
            # IndexError: list index out of range occurs here but not in scaledfunctionsystem.py
            # continue later
            sub_result2 = relu((tangent_collection[permutation_count][permutation_counter][2][0].transpose() @ sub_result1) + bias_collection[permutation_count][permutation_counter][2][0])
            sub_result3 = ((tangent_collection[permutation_count][permutation_counter][3][0].transpose() @ sub_result2) + bias_collection[permutation_count][permutation_counter][3][0])
            print(sub_result3)
            print(node_permutation)
            inference_total[permutation_count][permutation_counter].append(sub_result3[0])
        
        inference_total[permutation_count][permutation_counter] = np.array(inference_total[permutation_count][permutation_counter])
        score = np.sqrt(np.sum(np.square(inference_total[permutation_count][permutation_counter] - temperature_extraction_preprocess)))
        print("Nodes " + str(node_permutation) + " towards D5 link: " + str(score))
        permutation_counter += 1
   



exit()
  
# SUGGESTIVE ROUTE OF PROGRESS
# SCALE UP SYSTEM


































print("***************************************************************************")       
print("***************************************************************************")       








new_multilayerlink_bidirectional_tangent_storage = []
for i in range(INTRALINK_DENSITY + 1):
    new_multilayerlink_bidirectional_tangent_storage.append([])
for i in range(INTRALINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        new_multilayerlink_bidirectional_tangent_storage[i].append([])
for i in range(INTRALINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        for k in range(NODE_COUNT + 1):
            new_multilayerlink_bidirectional_tangent_storage[i][j].append([])

new_multilayerlink_bidirectional_bias_storage = []
for i in range(INTRALINK_DENSITY + 1):
    new_multilayerlink_bidirectional_bias_storage.append([])
for i in range(INTRALINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        new_multilayerlink_bidirectional_bias_storage[i].append([])
for i in range(INTRALINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        for k in range(NODE_COUNT + 1):
            new_multilayerlink_bidirectional_bias_storage[i][j].append([])



for n in range(INTRALINK_N_DEPLOY):
    
    for i in range(1, NODE_COUNT + 1):
    
        Node_n_sample = Node_list[i][NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * n / INTRALINK_N_DEPLOY) : NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * (n + 1) / INTRALINK_N_DEPLOY), :]
        
        #Node_prelearner = Node_n_sample[:,PRETEST_MAGNITUDE :]
        #Node_pretester = Node_n_sample[:,: PRETEST_MAGNITUDE]
        #NODE_COUNT - LEARN_MAGNITUDE
        #Node_learner = Node_n_sample[:,:LEARN_MAGNITUDE]
        #Node_prelearner = Node_learner[:,PRETEST_MAGNITUDE:]
        #Node_pretester = Node_learner[:,:PRETEST_MAGNITUDE]
        #Node_prelearner = Node_learner[:,:PRETEST_MAGNITUDE]
        #LEARN_MAGNITUDE
        #math.floor(PRETEST_MAGNITUDE * LEARN_MAGNITUDE)
        #Node_test = Node_n_sample[:,:LEARN_MAGNITUDE]
        #Node_test = Node_prelearner[:,:learn_magnitude]
        #Node_test = Node_prelearner[:,:learn_magnitude]
        #NODE_COUNT - LEARN_MAGNITUDE
        #Node_pretest = Node_n_sample[:,:LEARN_MAGNITUDE]
        
        inputs = keras.Input(shape=(sequence_length, Node_n_sample.shape[-1]))
        x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(inputs)
        for k in range(1, INTRALINK_DENSITY):
            x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(x)
        outputs = keras.layers.Dense(OUTPUT_MAGNITUDE)(x)
        Intra_D = keras.Model(inputs, outputs)
        #callbacks = [
        #    keras.callbacks.ModelCheckpoint("jena_dense.keras",
        #    save_best_only=True)
        #    ]
        Intra_D.compile(optimizer=OPTIMIZER, loss=LOSS, metrics=METRIC)
        Intra_D.fit(Node_n_sample, epochs= EPOCHS)
        #    callbacks=callbacks)
        #Intra_D = keras.models.load_model("jena_dense.keras")
        #print(f"Test MAE: {Intra_D.evaluate(test_node_5)[1]:.2f}")

        for j in range(1, INTRALINK_DENSITY + 1):
            new_multilayerlink_bidirectional_tangent_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[0]))  # j-1        
            new_multilayerlink_bidirectional_bias_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[1]))
        
#INFERENCE_MAGNITUDE
#Node_n_sample = Node_list[i][NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * n / INTRALINK_N_DEPLOY) : NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * (n + 1) / INTRALINK_N_DEPLOY), :]



for n in range(INTRALINK_N_DEPLOY):
    for i in range(NODE_COUNT):
        
        Node_n_sample = Node_list[i][NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * n / INTRALINK_N_DEPLOY) : NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * (n + 1) / INTRALINK_N_DEPLOY), :]

        inputs = keras.Input(shape=(sequence_length, Node_n_sample.shape[-1]))
        x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(inputs)
        for k in range(1, INTRALINK_DENSITY):
            x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(x)
        outputs = keras.layers.Dense(OUTPUT_MAGNITUDE)(x)
        Intra_D = keras.Model(inputs, outputs)
        
        Intra_D.compile(optimizer=OPTIMIZER, loss=LOSS, metrics=METRIC)
        Intra_D.fit(Node_n_sample, epochs = EPOCHS)# validation_data=Node_pretester)
        #    callbacks=callbacks)
        #Intra_D = keras.models.load_model("jena_dense.keras")
        #print(f"Test MAE: {Intra_D.evaluate(test_node_5)[1]:.2f}")

        for j in range(1, INTRALINK_DENSITY + 1):
            multilayerlink_bidirectional_tangent_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[0]))  # j-1        
            multilayerlink_bidirectional_bias_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[1]))

        inputs = keras.Input(shape=(sequence_length, Node_learner.shape[-1]))
        x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(inputs)
        for k in range(1, INTRALINK_DENSITY):
            x = keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION)(x)
        outputs = keras.layers.Dense(OUTPUT_MAGNITUDE)(x)
        Intra_D = keras.Model(inputs, outputs)

        Intra_D.compile(optimizer=OPTIMIZER, loss=LOSS, metrics=METRIC)
        Intra_D.fit(Node_prelearner, epochs= EPOCHS, validation_data=Node_pretester)
        #    callbacks=callbacks)
        #Intra_D = keras.models.load_model("jena_dense.keras")
        #print(f"Test MAE: {Intra_D.evaluate(test_node_5)[1]:.2f}")
        for j in range(1, INTRALINK_DENSITY + 1):
            new_multilayerlink_bidirectional_tangent_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[0]))  # j-1        
            new_multilayerlink_bidirectional_bias_storage[j][i][i].append(np.array(Intra_D._layers[j].get_weights()[1]))
            
#LEARN_MAGNITUDE
#INTRALINK_N_DEPLOY

Node_n_sample = Node_list[i][NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * n / INTRALINK_N_DEPLOY), NODE_MAGNITUDE + math.floor(DEPLOY_MAGNITUDE * (n + 1) / INTRALINK_N_DEPLOY)]
Node_learner = Node_n_sample[:,:LEARN_MAGNITUDE]
Node_prelearner = Node_learner[:,PRETEST_MAGNITUDE:]
Node_pretester = Node_learner[:,:PRETEST_MAGNITUDE]




















exit()
   

# Node_test Node_test Node_test








Node_test = Node_n_sample[:,:LEARN_MAGNITUDE]





for k in range(1, INTERLINK_DENSITY + 1):
    for i in range(1, NODE_COUNT + 1):
        for j in range(1, NODE_COUNT + 1):




        # Node i -> Node j, Layer k
        #print("Start INTERLINK CONSTRUCTION")
            print(k)
            print(i)
            print(j)
        # layer 3, node 1 -> node 2 no entry






    for j in range(1, INTERLINK_DENSITY + 1):
        

    
#Intra_D = keras.models.Sequential()
#Intra_D.add(keras.Input(shape=(sequence_length, Node_list[i].shape[-1])))
#I#ntra_D.add(keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION,))
#Intra_D.add(keras.layers.Dense(PARAMETER_COUNT, activation=ACTIVATION))
#Intra_D.add(keras.layers.Dense(OUTPUT_MAGNITUDE))








    inputs = keras.Input(shape=(sequence_length, Node_list[i].shape[-1]))
    x = keras.layers.Dense(16, activation="relu")(inputs)
    x = keras.layers.Dense(16, activation="relu")(x)
    outputs = keras.layers.Dense(1)(x)
    Intra_D1 = keras.Model(inputs, outputs)
    
    parameter_variation_list.append([4,4,4,4])
    
    callbacks = [
        keras.callbacks.ModelCheckpoint("jena_dense.keras",
        save_best_only=True)
        ]
    
    Intra_D1.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    history = Intra_D1.fit(train_node_1,
    epochs=1,
    validation_data=val_node_1,
    callbacks=callbacks)
    
    
    
    































testlink = keras.models.Sequential()
testlink.add(keras.Input(shape=(sequence_length, data_extraction_1.shape[-1])))
testlink.add(keras.layers.Dense(16, activation=,))
testlink.add(keras.layers.Dense(16, activation='relu'))
testlink.add(keras.layers.Dense(1))








# TWEAK
multilayerlink_bidirectional_bias_storage = []
multilayerlink_bidirectional_tangent_storage = []

for i in range(INTERLINK_DENSITY + 1):
    multilayerlink_bidirectional_tangent_storage.append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        multilayerlink_bidirectional_bias_storage[i].append([])
for i in range(INTERLINK_DENSITY + 1):
    for j in range(NODE_COUNT + 1):
        for k in range(NODE_COUNT + 1):
            multilayerlink_bidirectional_bias_storage[i][j].append([])


for i in range(NODE_COUNT):
    
    data_extraction = Node_list[i]
    temperature_extraction = data_extraction[:,-1]
    num_train_samples = int(0.5 * len(data_extraction))
    num_val_samples = int(0.25 * len(data_extraction))
    num_test_samples = len(data_extraction) - num_train_samples - num_val_samples
    duration = len(data_extraction) - data_extraction
    
    sampling_rate = 6
    sequence_length = 120
    delay = sampling_rate * (sequence_length + 24 - 1)
    batch_size = 256
        
    train_node = keras.utils.timeseries_dataset_from_array(
        data_extraction,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=0,
        end_index=num_train_samples) #duration/INTRALINK_N

    val_node = keras.utils.timeseries_dataset_from_array(
        data_extraction,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples,
        end_index=num_train_samples + num_val_samples)

    test_node = keras.utils.timeseries_dataset_from_array(
        data_extraction,
        targets=temperature_extraction,
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=num_train_samples + num_val_samples)
    
    inputs = keras.Input(shape=(sequence_length, temperature_extraction.shape[-1]))
    x = keras.layers.Dense(INTERLINK_SPECTRE, activation="relu")(inputs)
    x = keras.layers.Dense(INTERLINK_SPECTRE, activation="relu")(x)
    outputs = keras.layers.Dense(1)(x)
    Intra_D = keras.Model(inputs, outputs)
    callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
    ]
    Intra_D.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    history = Intra_D.fit(train_node,
        epochs=1,
        validation_data=val_node,
        callbacks=callbacks)
    Intra_D = keras.models.load_model("jena_dense.keras")
    print(f"Test MAE: {Intra_D.evaluate(test_node)[1]:.2f}")

    for j in range(1, INTERLINK_DENSITY + 1):
        multilayerlink_bidirectional_tangent_storage[i][j][j].append(Intra_D._layers[i].get_weights()[0])          
        multilayerlink_bidirectional_bias_storage[i][j][j].append(Intra_D._layers[i].get_weights()[1])

for i in range(NODE_COUNT):
    for j in range(NODE_COUNT):
        
        
        
        




