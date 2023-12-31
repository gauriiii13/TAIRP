import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from cv2 import imshow
from PIL import Image
import tensorflow as tf
tf.random.set_seed(3)
from tensorflow import keras
from keras.datasets import mnist
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint

#loading dataset
(X_train, Y_train),(X_test, Y_test)=mnist.load_data()

#scaling the values
X_train = np.expand_dims(X_train, axis=-1) / 255.0
X_test = np.expand_dims(X_test, axis=-1) / 255.0

#setting up the layers of neural network
model= keras.Sequential([
                          Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
                          MaxPooling2D((2,2)),
                          Conv2D(64,(3,3),activation='relu'),
                          MaxPooling2D((2,2)),
                          Flatten(),
                          Dense(128,activation='relu'),
                          Dropout(0.5),
                          Dense(10,activation='softmax')
])

model.compile(
               optimizer=Adam(learning_rate=0.001),
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy']
)

earlystopping= EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
modelcheckpoint= ModelCheckpoint('Model.h5', save_best_only=True)

# Train the model
history = model.fit(X_train, Y_train,
                    epochs=20,
                    batch_size=64,
                    validation_data=(X_test, Y_test),
                    callbacks=[earlystopping, modelcheckpoint])

model.load_weights('Model.h5')

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, Y_test)
print("Test accuracy:",test_acc)

