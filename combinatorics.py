



# Python Program to Print 
# all subsets of given size of a set
 
import itertools
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
 
# Driver Code
s = [1, 2, 3, 4, 5]
n = 3
 
print(findsubsets(s, n))

for subset in findsubsets(s, n):
    print(subset)
    for i in subset:
        findsubsets(s, i)
       
       
       
       

#n = 3
 
#print(findsubsets(s, n))

#for subset in findsubsets(s, n):
 #   print(subset)
 #   for i in subset:
 #       findsubsets(s, i)


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

# DIFFICULTY: EITHER MERGE DATA, OR USE MERGE NeuralNet

# ORGANIZE LOOP ORDER
#for z in range(1, INTERLINK_DENSITY + 1):

merged_inputnode_tangent_interintra = []
merged_inputnode_bias_interintra = []
merged_inputnode_tangent_interintra
merged_inputnode_tangent_interintra

for permutation_count in range(1, NETWORK_ORDER): 
    for node_permutation in findsubsets(node_collection, permutation_count):
        for l_inter in range(1, INTERLINK_DENSITY + 1):
            # INTERLINK LAYER k INTRALINK LAYER m NODE i -> NODE j
            for l_intra in range(1, INTERLINK_DENSITY + 1):
                print("----")
                print(findsubsets(node_collection, permutation_count))
                print(permutation_count)
                print(node_permutation)
                print(l_inter)
                print(l_intra) 
                print("----")
#print(s)
