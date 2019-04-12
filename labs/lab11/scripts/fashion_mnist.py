from __future__ import absolute_import, division, print_function

import os
import random
import sys
import math

# TensorFlow and tf.keras
import tensorflow as tf
import cv2
from tensorflow import keras
from PIL import Image
from PIL import ImageOps

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

def plot_image(i, predictions_array, true_label, img):
	predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
	plt.grid(False)
	plt.xticks([])
	plt.yticks([])
	
	plt.imshow(img, cmap=plt.cm.binary)

	predicted_label = np.argmax(predictions_array)
	if predicted_label == true_label:
		color = 'blue'
	else:
		color = 'red'
	
	plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
																100*np.max(predictions_array),
																class_names[true_label]),
																color=color)

def plot_value_array(i, predictions_array, true_label):
	predictions_array, true_label = predictions_array[i], true_label[i]
	plt.grid(False)
	plt.xticks([])
	plt.yticks([])
	thisplot = plt.bar(range(10), predictions_array, color="#777777")
	plt.ylim([0, 1]) 
	predicted_label = np.argmax(predictions_array)
 
	thisplot[predicted_label].set_color('red')
	thisplot[true_label].set_color('blue')

# load training/test data
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# class_names 0-9
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
							 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# normalize images
train_images = train_images / 255.0
test_images = test_images / 255.0

# build model
model = keras.Sequential([
		keras.layers.Flatten(input_shape=(28, 28)),
		keras.layers.Dense(128, activation=tf.nn.relu),
		keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
							loss='sparse_categorical_crossentropy',
							metrics=['accuracy'])

# train model
model.fit(train_images, train_labels, epochs=2)
'''
# test model
test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

# predict testing data
predictions = model.predict(test_images)

# print which prediction the model guessed (highest confidence)
print(np.argmax(predictions[0]))

# print actual label 
print(test_labels[0])

# Checkpoint 2 code 

# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red

num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
offset = 0#9000 # my addition
for i in range(num_images):
	plt.subplot(num_rows, 2*num_cols, 2*i+1)
	plot_image(i+offset, predictions, test_labels, test_images)
	plt.subplot(num_rows, 2*num_cols, 2*i+2)
	plot_value_array(i+offset, predictions, test_labels)
plt.show()
'''
# Checkpoint 3 code - use 3 new images and see how the model classifies them

img_name_list = os.listdir('./')
img_name_list = sorted([name for name in img_name_list if 'jpg' in name.lower()])
img_list = [cv2.imread(name, cv2.IMREAD_GRAYSCALE) for name in img_name_list]
print("before resize")
print([im.shape for im in img_list])
img_list = [cv2.resize(im, (28, 28), interpolation = cv2.INTER_AREA) for im in img_list]
img_list = [cv2.bitwise_not(im) for im in img_list]
img_list = [(im / 255) for im in img_list]
print("after resize")
print([im.shape for im in img_list])
img_list = np.asarray(img_list)

cv2.imwrite("ankle_boot_small.jpg", img_list[0] * 255)
cv2.imwrite("pullover_small.jpg", img_list[1] * 255)
cv2.imwrite("tshirt_small.jpg", img_list[2] * 255)

predictions = model.predict(img_list)
test_labels = [9, 2, 0]

# test model
test_loss, test_acc = model.evaluate(img_list, test_labels)

print('Test accuracy:', test_acc)

num_rows = 1
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
offset = 0 # my addition
for i in range(num_images):
	plt.subplot(num_rows, 2*num_cols, 2*i+1)
	plot_image(i+offset, predictions, test_labels, img_list)
	plt.subplot(num_rows, 2*num_cols, 2*i+2)
	plot_value_array(i+offset, predictions, test_labels)
	print(predictions[i])
	print(np.argmax(predictions[i]))
	print(class_names[np.argmax(predictions[i])])
plt.show()

