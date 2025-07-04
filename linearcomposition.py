# A Network with Scikit-Learn

import os
os.environ["KERAS_BACKEND"] = "tensorflow"
import tensorflow as tf
import pandas as pd
import keras
from keras.utils import FeatureSpace
import numpy as np
from sklearn.linear_model import LinearRegression
from sys import argv

NETWORK_ORDER = 13

############### TEMPLATE DATASET PROVIDED BY Cleveland Clinic Foundation for Heart Disease

file_url = "http://storage.googleapis.com/download.tensorflow.org/data/heart.csv"
dataframe = pd.read_csv(file_url)
dataframe = dataframe.drop(columns=['thal'])
node_count = dataframe.shape[1]
assert node_count == NETWORK_ORDER

LinReg_matrix = []
for i in range(NETWORK_ORDER):
    LinReg_matrix.append([])
    for j in range(NETWORK_ORDER):
        LinReg_matrix[i].append([])
        x = np.array(dataframe.iloc[:,[i]])
        y = np.array(dataframe.iloc[:,[j]])
        reg = LinearRegression().fit(x, y)     
        LinReg_matrix[i][j] = reg

def driver(argv):
    known_aspect = int(argv[1])
    inference = int(argv[2])     
    observation = float(argv[3]) 
    LinReg_matrix[known_aspect][inference]
    inferential_value = LinReg_matrix[known_aspect][inference].predict(np.array([[observation]]))
    process_score = LinReg_matrix[known_aspect][inference].score(x, y)
    
    print("\n")
    print("HEALTH CATALOGUE:")
    for i in range(len(dataframe.columns)):
        print(str(i) + " : " + dataframe.columns[i])
    print("\n")
    print("COMPUTATION:")
    print("inferrer: " + str(known_aspect))
    print("inferree: " + str(inference))
    print("observation: " + str(observation))
    print("inference: " + str(inferential_value[0][0]))
    print("inference performance on learning set: " + str(process_score))
    print("\n")

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: python linearcomposition.py [#known_aspect] [#inference] [observation]")
    else:
        driver(argv)


# Generalize the above to broader data-environments    
# The process of inference is Learning. We need good infrastracture more so, lots of code, lots of data
# The art lay in proper structure in programs, thus next step: bring structure to the above and generalize over NETWORK_ORDER
# And give performance visualizations upon complete construction
# continue on Thursday Oct 3.