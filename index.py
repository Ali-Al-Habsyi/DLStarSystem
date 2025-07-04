import itertools


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
        print(tangent_collection[permutation_count][node_permutation_counter])
        print(bias_collection[permutation_count][node_permutation_counter])
        print(INTERLINK_DENSITY + 1)
        for layer_number in range(0, INTERLINK_DENSITY + 1):  
            print("-")
            
            print(tangent_collection)
            print(bias_collection)
            print(INTERLINK_DENSITY + 1)
                
            
    node_permutation_counter += 1
            
  #  permutation_counter = 0




exit()

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
            bias_collection[permutation_count].append([]) 

        node_permutation_counter += 1
      

# tangent_collection[permutation_count][node_permutation_counter][layer_number]
# dimensions (NETWORK_ORDER + 1, len( findsubsets(node_collection, permutation_count) ), INTERLINK_DENSITY + 1)
            
exit()

# Fix storage

outer_loop = 0
for permutation_count in range(1, NETWORK_ORDER + 1): 


    node_permutation_counter
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1
        tangent_collection[permutation_count].append([])
        
        tangent_collection[permutation_count][permutation_counter].append([])
        bias_collection[permutation_count][permutation_counter].append([]) 
        
        for layer_number in range(0, INTERLINK_DENSITY + 1):  
            tangent_collection[permutation_count][permutation_counter].append([])
            
            tangent_collection[permutation_count][node_permutation_counter][layer_number]
        
        node_permutation_counter += 1
   
   
    
    
    


exit()



print(permutation_count)
print(tangent_collection)
print(len(tangent_collection))
print("-----------------------------------------------------------")
print(tangent_collection[permutation_count])
print(tangent_collection)
print(permutation_count)
print(len(tangent_collection))
print(str(outer_loop) + "debug")

















outer_loop = 0
for permutation_count in range(1, NETWORK_ORDER): 

    permutation_counter = 0
    print(permutation_count)
    print(tangent_collection)
    print(len(tangent_collection))
    print("-----------------------------------------------------------")
    print(tangent_collection[permutation_count])
    print(tangent_collection)
    print(permutation_count)
    print(len(tangent_collection))
    print(str(outer_loop) + "debug")
    
    
    tangent_collection[permutation_count].append([])
    bias_collection[permutation_count].append([]) 
    
    for node_permutation in findsubsets(node_collection, permutation_count):
        permutation_counter += 1
        tangent_collection[permutation_count].append([])
        bias_collection[permutation_count].append([])
        
        tangent_collection[permutation_count][permutation_counter].append([])
        bias_collection[permutation_count][permutation_counter].append([]) 
        
        for layer_number in range(1, INTERLINK_DENSITY + 1):  
            tangent_collection[permutation_count][permutation_counter].append([])
            bias_collection[permutation_count][permutation_counter].append([]) 
    outer_loop += 1
#model_collection[permutation_count][loop_counter][layer_number]

tangent_collection[permutation_count][permutation_counter][layer_number]
bias_collection[permutation_count][permutation_counter][layer_number]

for permutation_count in range(0, NETWORK_ORDER): 
    for node_permutation in findsubsets(node_collection, permutation_count):
        for layer_number in range(0, INTERLINK_DENSITY + 1):  
            print(tangent_collection[permutation_count][permutation_counter][layer_number])
            print(bias_collection[permutation_count][permutation_counter][layer_number])

#