#CELL ONE 
# DO NOT CHANGE THIS CELL
# We first import TensorFlow and other libraries
import sys

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense


#CELL 2 
# DO NOT CHANGE THIS CELL
# This script requires TensorFlow 2 and Python 3.
if tf.__version__.split('.')[0] != '2':
    raise Exception((f"The script is developed and tested for tensorflow 2. "
                     f"Current version: {tf.__version__}"))

if sys.version_info.major < 3:
    raise Exception((f"The script is developed and tested for Python 3. "
                     f"Current version: {sys.version_info.major}"))

#CELL 3

# DO NOT CHANGE THIS CELL
# We then set up some functions and local variables
predictions = []
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    predictions.append(model.predict(xs))
callbacks = myCallback()

# We then define the xs (inputs) and ys (outputs)
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)


#CELL 4 
# PLEASE COMPELTE THIS CELL

SHAPE =[1] # definition of the shape of the input
LOSS = "mean_squared_error" # definition of the loss function 

# Define your model type
model = Sequential([Dense(units=1, input_shape=SHAPE)])
    
# Compile your model with choice of optimizer and loss function
model.compile(optimizer='sgd', loss=LOSS) # I need to do some research in regard of the under the hood implmentation of the optmizers and the differences 

# Plotting the different numbers ,
EPOCH_NUMBERS=[1,25,50,150,300] # Update me to see other Epochs
plt.plot(xs,ys,label = "Ys")
for EPOCH in EPOCH_NUMBERS:
    plt.plot(xs,predictions[EPOCH-1],label = "Epoch = " + str(EPOCH))
plt.legend()
plt.show()


