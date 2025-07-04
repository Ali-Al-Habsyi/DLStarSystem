from re import L
import numpy as np

import itertools

from StarSystems.index import NETWORK_ORDER

# COLLECT NODES

score = 999

def findsubsets(s, n):
    return list(itertools.combinations(s, n))

permutation_count = 1
node_permutations = findsubsets(node_collection, permutation_count)
node_permutation = node_permutations[0]
print("Nodes " + str(node_permutation) +" towards D5 link: " + str(score))

#exit()
T = np.array([np.array([[1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.]]),
 np.array([[1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.],
  [1.]])])

print(len([]))

exit()
print(T.transpose())
print(T)

M = T.transpose() @ T 





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
        
################################################################################################

#data_extraction_5_preprocess = raw_data[:-delay, [12, 13]]
################################################################################################
 


