import keras
import pandas as pd
from zipfile import ZipFile
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

link_D1_tangent_layer1_batch = []
link_D2_tangent_layer1_batch = []
link_D1_bias_layer1_batch = []
link_D2_bias_layer1_batch = []

(train_data_1, train_labels_1), (test_data_1, test_labels_1) = keras.datasets.boston_housing.load_data()

for i in range(10):
    link_D1_tangent_layer1_batch.append(np.eye(100))
    link_D2_tangent_layer1_batch.append(np.eye(100))
    link_D1_bias_layer1_batch.append(np.eye(100))
    link_D2_bias_layer1_batch.append(np.eye(100))
   
link_D1_tangent_layer1_batch = np.array(link_D1_tangent_layer1_batch)
link_D2_tangent_layer1_batch = np.array(link_D2_tangent_layer1_batch)
link_D1_bias_layer1_batch = np.array(link_D1_bias_layer1_batch)
link_D2_bias_layer1_batch = np.array(link_D2_bias_layer1_batch)