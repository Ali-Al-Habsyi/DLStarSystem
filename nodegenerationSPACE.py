################################################################################
# TOWARDS MACHINE ONE
# VIRTUAL DEVICES: NODE-GENERATION VIA NASAEARTH
################################################################################
# --> (CURRENT) --> COLLECTOR OVER NASAEARTH
# DATA STORED, BUILD COLLECTOR MANUALLY
# NODE-GENERATOR EXAMPLE
#######################################

# Pursue the below loader to full extent
# First

import numpy
import earthaccess
import dlc2kinematics
import h5py

earthaccess.login()



results = earthaccess.search_data(
    short_name='ATL06',
    bounding_box=(-10, 20, 10, 50),
    temporal=("1999-02", "2019-03"),
    count=10
)


import numpy as np
#f = h5py.File('data_first.h5', 'r')



f_new = h5py.File('data_first.h5', 'r')
f = h5py.File('data_second.h5', 'r')

#print(type(f2))
#for key in f.keys():
  #  print(key) #Names of the root level object names in HDF5 file - can be groups or datasets.
  #  print(type(f[key])) # get the object type: usually group or dataset

# h5 file loader

file_name = 'data_third.h5'
#h5dataset_collection = []  
f = h5py.File(file_name, 'r')
file_keys = f.keys()

# Summarize in looped loop
for key in file_keys:
    
    for item in f[key].items():
        print(type(item[1]))
        
        if isinstance(item[1], h5py._hl.group.Group): 
            length = len(item[1].keys())
            print("=========================================")


            if length > 0:
                for key in item[1].keys():
                    print(type(item[1][key]))  
                    
                    if isinstance(item[1][key], h5py._hl.group.Group): 
                    
                    
                        for keynew in item[1][key]:
                            
                            if isinstance(item[1][key][keynew], h5py._hl.group.Group): 
                                
                                if length > 0:
                                    for keynewnew in item[1][key][keynew].keys():
                                        print(type(item[1][key][keynew][keynewnew]))
                                
                            if isinstance(item[1][key][keynew], h5py._hl.dataset.Dataset): 
                                print(item[1][key][keynew][()]) 
                                print("depthiterate")
                                
                    if isinstance(item[1][key], h5py._hl.dataset.Dataset): 
        
                        print(item[1][key][()]) 
                        
                    
        if isinstance(item[1], h5py._hl.dataset.Dataset): 
        
            print(item[1][()]) 
                        
                  
print("************************************************************************")
    
global h5dataset_collection

h5dataset_collection = []
    
def outer_loop(item):     
    print("checkcheck")
    if isinstance(item, h5py._hl.group.Group): 

        for key in item.keys():
            
            outer_loop(item[key])
            
    if isinstance(item, h5py._hl.dataset.Dataset): 
        print(item[()])
        h5dataset_collection.append(item[()])
        

for key in file_keys:
    
    for item in f[key].items():
        print("check")
        outer_loop(item[1])


#h5dataset_collection = np.array(h5dataset_collection)
#print(h5dataset_collection.shape)
print(h5dataset_collection)  

print("************************************************************************")

h5dataset_collection = []
    
def outer_loop(item):     
    print("checkcheck")
    if isinstance(item, h5py._hl.group.Group): 

        for key in item.keys():
            
            outer_loop(item[key])
            
    if isinstance(item, h5py._hl.dataset.Dataset): 
        print(item[()])
        h5dataset_collection.append(item[()])
        

for key in file_keys:
    
    for item in f[key].items():
        print("check")
        outer_loop(item[1])

exit()

print("************************************************************************")

# nc collector













print("************************************************************************")
















# pursue the below
# datatype nc
# datatype 
# length = len(item[1].keys())
# print("=========================================")


if length > 0:
    for key in item[1].keys():
        print(type(item[1][key]))  
        
        if isinstance(item[1][key], h5py._hl.group.Group): 
        
        
            for keynew in item[1][key]:
                
                if isinstance(item[1][key][keynew], h5py._hl.group.Group): 
                    
                    if length > 0:
                        for keynewnew in item[1][key][keynew].keys():
                            print(type(item[1][key][keynew][keynewnew]))
                    
                if isinstance(item[1][key][keynew], h5py._hl.dataset.Dataset): 
                    
                    print(item[1][key][keynew][()]) 
                    print("depthiterate")
                    
        if isinstance(item[1][key], h5py._hl.dataset.Dataset): 

            #print(item[1][key][()]) 
            h5dataset_collection.append(item)


print("************************************************************************")

# NC collector








print("************************************************************************")




exit()



if isinstance(item[1][key], h5py._hl.group.Group): 


    for keynew in item[1][key]:
        
        if isinstance(item[1][key][keynew], h5py._hl.group.Group): 
            
            if length > 0:
                for keynewnew in item[1][key][keynew].keys():
                    print(type(item[1][key][keynew][keynewnew]))
            
        if isinstance(item[1][key][keynew], h5py._hl.dataset.Dataset): 
            print(item[1][key][keynew][()]) 
            print("depthiterate")
            
    if isinstance(item[1][key], h5py._hl.dataset.Dataset): 

        print(item[1][key][()]) 



















exit()


def inner_loop(item):

    if isinstance(item[1], h5py._hl.dataset.Dataset): 
        
        h5dataset_collection.append(item[1][()]) 

    if isinstance(item[1], h5py._hl.group.Group): 
        # group for groupkeys 
        
        
        
        
        for item_iterate in item[1].items():  
            inner_loop(item_iterate)  
            
    return
        
#    h5dataset_collection.append(item[1][()]) 
    #if type(item_iterate[1]) == "<class 'h5py._hl.group.Group'>": 
    # if isinstance(item[1], h5py._hl.group.Group):           
    #     
        
        #if isinstance(item[1], h5py._hl.dataset.Dataset): 
    #    h5dataset_collection.append(item[1][()]) 
    #if isinstance(item[1], h5py._hl.group.Group):
    #    inner_loop(item)
        

#isinstance(x, h5py._hl.dataset.Dataset)   
#isinstance(x, h5py._hl.group.Group)       

   
   
   
        
for key in file_keys:
    
    for item in f[key].items():
        print(type(item[1]))
        #print(type(type(item[1])))

        if isinstance(item[1], h5py._hl.dataset.Dataset): 
            h5dataset_collection.append(item[1][()]) 
        
        if isinstance(item[1], h5py._hl.group.Group):
            inner_loop(item[1])
            
        
                
                
print(len(h5dataset_collection))            
print(h5dataset_collection)      
                
exit()           
                
                
                
                
                
                
                
       

            
                
                        
                        
                        
                             

# nc file loader


from scipy.io import netcdf
  
file2read = netcdf.NetCDFFile(path+'state.nc','r')
var = file2read.keys()[0]
temp = file2read.variables[var] # var can be 'Theta', 'S', 'V', 'U' etc..
data = temp[:]*1
file2read.close()
        
#if item in thing.items():   

#print(item)
print("=======================================")
print("=======================================")
print("=======================================")
print("=======================================")
#print(thing)

#thingiterate in thing[1].items():  

#for thingiterate in thing[1].items():
#    print("=======================================")
#    print(thingiterate)
#    print(thingiterate[1][()])
#    print(len(thingiterate[1][()]))
#    print(type(thingiterate[1]))


exit()



for thing in f['gt3r'].items():
    for thingiterate in thing[1].items():
        print("=======================================")
        print(thingiterate)
        print(thingiterate[1][()])
        print(len(thingiterate[1][()]))
        print(type(thingiterate[1]))
        
        
        
            

# h5 file loader

##


#file_name = 













#print(thingiterate[1])
            



#print(thingiterate[1].keys())
#group = f[key]


#f.close()
#print(data)    
exit()


# This assumes group[some_key_inside_the_group] is a dataset, 
# and returns a np.array:

#Do whatever you want with data

#After you are done
f.close()
    
print(f2.keys())
print(f2['gt3l'])
#print(f2['orbit_info'])
#print(f2['ancillary_data'])
#print(f2['gt3l'])  #<HDF5 group "/orbit_info" (9 members)>
for thing in f2['gt3l'].items():
    print("=======================================")
    for thingiterate in thing[1].items():
        print(thingiterate[1])
        print(thingiterate[1].keys())
        
        #for thingiterateiterate in thingiterate[1]:
        #    print(thingiterateiterate)
        #    #print(thingiterateiterate.keys())
        #    print(thingiterateiterate['dataset'])
    #print()
    #print(thing[0])
        
        #for thingiterate in thing.items():
        #    print(thingiterate)


ds = get_dataset()

# OK - f2 is out of scope, but the dataset reference keeps it open:
ds[0]

del ds 



exit()
# Getting the data
#data = list(file[a_group_key])
print("===============================================")
print("===============================================")
print("===============================================")
print("===============================================")
print("===============================================")
print("===============================================")
#print(file)  
#file[a_group_key]

#Open the H5 file in read mode
#with h5py.File('data.h5', 'r') as file:

#    print(&quot;Keys: %s&quot; % file.keys())
#    a_group_key = list(file.keys())[0]

# Getting the data
#    data = list(file[a_group_key])
#    print(data)



