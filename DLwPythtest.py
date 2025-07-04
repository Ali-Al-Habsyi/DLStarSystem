import numpy as np
import os
import keras
fname = os.path.join("jena_climate_2009_2016.csv")

with open(fname) as f:
    data = f.read()
    lines = data.split("\n")
    header = lines[0].split(",")
    lines = lines[1:]

print(header)
print(len(lines))

temperature = np.zeros((len(lines),))
raw_data = np.zeros((len(lines), len(header) - 1))
for i, line in enumerate(lines):
    values = [float(x) for x in line.split(",")[1:]]
    temperature[i] = values[1]
    raw_data[i, :] = values[:] 
 
num_train_samples = int(0.5 * len(raw_data))
num_val_samples = int(0.25 * len(raw_data))
num_test_samples = len(raw_data) - num_train_samples - num_val_samples

sampling_rate = 6
sequence_length = 120
delay = sampling_rate * (sequence_length + 24 - 1)
batch_size = 256

train_dataset = keras.utils.timeseries_dataset_from_array(
    raw_data[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=0,
    end_index=num_train_samples)
val_dataset = keras.utils.timeseries_dataset_from_array(
    raw_data[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples,
    end_index=num_train_samples + num_val_samples)
test_dataset = keras.utils.timeseries_dataset_from_array(
    raw_data[:-delay],
    targets=temperature[delay:],
    sampling_rate=sampling_rate,
    sequence_length=sequence_length,
    shuffle=True,
    batch_size=batch_size,
    start_index=num_train_samples + num_val_samples)

# Problem in Challots' construction

# Solution: proceed with array
link_D2D1_bias2 = keras.models.Sequential()
link_D2D1_bias2.add(keras.layers.Flatten())
link_D2D1_bias2.add(keras.layers.Dense(16, activation="relu"))
link_D2D1_bias2.add(keras.layers.Dense(1))

callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
   save_best_only=True)
]
link_D2D1_bias2.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = link_D2D1_bias2.fit(train_dataset,
    epochs=10,
    validation_data=val_dataset,
    callbacks=callbacks
    )
link_D2D1_bias2 = keras.models.load_model("jena_dense.keras")
print(f"Test MAE: {link_D2D1_bias2.evaluate(test_dataset)[1]:.2f}")
exit()

inputs = keras.Input(shape=(sequence_length, raw_data.shape[-1]))
x = keras.layers.Flatten()(inputs)
x = keras.layers.Dense(16, activation="relu")(x)
outputs = keras.layers.Dense(1)(x)
model = keras.Model(inputs, outputs)
callbacks = [
    keras.callbacks.ModelCheckpoint("jena_dense.keras",
    save_best_only=True)
]
model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
history = model.fit(train_dataset,
    epochs=10,
    validation_data=val_dataset,
    callbacks=callbacks)
model = keras.models.load_model("jena_dense.keras")
print(f"Test MAE: {model.evaluate(test_dataset)[1]:.2f}")
#print(test_dataset)

exit()






#dataset = keras.utils.timeseries_dataset_from_array(
#    input_data, targets, sequence_length=10)
link = keras.models.Sequential()
for batch in test_dataset:
    inputs, targets = batch
    link.add(keras.layers.Dense(16))
    link.add(keras.layers.Dense(16))
    link.add(keras.layers.Dense(1))
    link.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    print(inputs) # First sequence: steps [0-9]
  # Corresponding target: step 10
  
#  print(targets)
#  break










inputs = keras.Input(shape=(sequence_length, raw_data.shape[-1]))
x = keras.layers.Flatten()(inputs)
x = keras.layers.Dense(16, activation="relu")(x)
outputs = keras.layers.Dense(1)(x)

#model = keras.Model(inputs, outputs)
#callbacks = [
#    keras.callbacks.ModelCheckpoint("jena_dense.keras",
#    save_best_only=True)
#]

link = keras.models.Sequential()
link.add(keras.layers.Dense(16))
link.add(keras.layers.Dense(16))
link.add(keras.layers.Dense(1))
link.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

#history = link.fit(train_dataset,
#    epochs=10,
#    validation_data=val_dataset,
#    callbacks=callbacks)

link_D2D1_bias2.fit(link_D1_bias_layer2_batch, link_D2_bias_layer2_batch, epochs=5, batch_size=128)

#link = keras.models.load_model("jena_dense.keras")
#print(f"Test MAE: {model.evaluate(test_dataset)[1]:.2f}")