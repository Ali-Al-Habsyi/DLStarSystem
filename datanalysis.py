import keras


# small datasets
# Time series data better, otherwise assume underlying unity in observation index
# D1
(train_data_1, train_labels_1), (test_data_1, test_labels_1) = keras.datasets.boston_housing.load_data()
train_data_1 = train_data_1[:,:10]
print(train_data_1.shape)

#train_data_1



#D2

#(train_data_1, train_labels_1), (test_data_1, test_labels_1) = keras.datasets.boston_housing.load_data()
#

#print(train_data_1[0])

exit()

#(train_images_2, train_labels_2), (test_images_2, test_labels_2) = keras.datasets.mnist.load_data()
#train_images_2 = train_images_2.reshape((60000, 28 * 28))
#train_images_2 = train_images_2.astype('float32') / 255
#print(train_images_2.shape)