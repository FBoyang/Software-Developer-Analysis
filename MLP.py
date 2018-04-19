import numpy as np
import seaborn as sns; sns.set()
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import sys
import csv

import tensorflow as tf 


df = pd.read_csv('one_hot.csv')

target = df.iloc[:, 0].astype(np.float32)
target = target.values.reshape(-1, 1)
data = df.iloc[:, df.columns != 'IsSoftwareDev'].astype(np.float32)


learning_rate = 0.001
batch_size = 128
#get label and data

'''
label = df.iloc[:, df.columns.get_loc('points')].astype(np.float32)
label = label.values.reshape(-1, 1)
data= df.drop(['points'], axis = 1).astype(np.float32).values
'''

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.3)
n_hidden_1 = 256
n_hidden_2 = 256
n_input = data.shape[1]

'''
X_train = pd.DataFrame(X_train, columns = data.columns)
X_test = pd.DataFrame(X_test, columns = data.columns)
y_train = pd.DataFrame(y_train, columns = label.columns)
y_test = pd.DataFrame(y_test, columns = label.columns)
'''
X = tf.placeholder('float', [None, n_input])
Y = tf.placeholder('float', [None, 1])

#Store layers weight & bias
weights = {
	'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
	'h2': tf.Variable(tf.random_normal([n_hidden_1 ,n_hidden_2])),
	'out': tf.Variable(tf.random_normal([n_hidden_2, 1]))
}

biases = {
	'b1': tf.Variable(tf.random_normal([n_hidden_1])),
	'b2': tf.Variable(tf.random_normal([n_hidden_2])),
	'out': tf.Variable(tf.random_normal([1]))
}

def MLP(x):
	layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
	layer_1 = tf.nn.sigmoid(layer_1)
	layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
	layer_2 = tf.nn.sigmoid(layer_2)
	out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
	out_layer = tf.nn.sigmoid(out_layer)
	return out_layer

logits = MLP(X)

def binary_transfer(x):
	if(x > 0.5):
		return 1
	else:
		return 0

#Define loss and optimizer
loss_op = tf.nn.l2_loss(logits - Y, name = "squared_error_cost")
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate)
train_op = optimizer.minimize(loss_op)
#initializing the variable
init = tf.global_variables_initializer()


with tf.Session() as sess:
	sess.run(init)
	avg_cost = 0
	#Training cycle
	with open('loss.csv', 'w', newline ='\n') as file:
		writer = csv.writer(file, delimiter = ',')
		for epoch in range(10000):
			start = (epoch * batch_size) % X_train.shape[0]
			end = min(start + batch_size, X_train.shape[0])
			batch_x = X_train[start: end]
			batch_y = y_train[start: end]
			# run optimization op (backprop) and cost op (to get loss value)
			_, loss = sess.run([train_op, loss_op], feed_dict = {X: batch_x, Y: batch_y})
			#Compute average loss

			if(epoch % 100 == 0):
				writer.writerow(['%04d' % (epoch + 1)] + ['{:.9f}'.format(loss)])
		
		test_error = tf.nn.l2_loss(logits - Y) / (X_test.shape[0])
		writer.writerow([test_error.eval({X: X_test, Y: y_test})])

	np.savetxt("prediction.csv",logits.eval({X: data, Y: target}), delimiter = ',')