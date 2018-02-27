"""

This program will use tensorflow to read-in data from csv files, build an n-layer neural network, and save the trained model.

Options:
- Choose number of hidden layers (1-3)
- Choose target, if there are multiple targets in the dataset

"""

import tensorflow as tf
import numpy as np
import os

dir = os.path.dirname(os.path.realpath('__file__'))
print(dir)


# Choose number and width of hidden layers
n_layers = 2
n_nodes_hl1 = 40
n_nodes_hl2 = 20
n_nodes_hl3 = 40

n_classes = 1  # number of output nodes


# Define csv input process
n_input_columns = 100  # in your input file, how many columns are there
n_features = n_input_columns - 5  # of your input file, how many columns should be used as predictive features
record_defaults = [[0.0] for i in range(n_input_columns)]

filename_queue = tf.train.string_input_producer([("./TrainFolder/FilenamePrefix_" +str(i) +".csv") for i in range(20)], shuffle=True)
save_folder = "\TFSavedModel\ModelName.ckpt"

reader = tf.TestLineReader(skip_header_lines=1)
key, value = reader.read(fielname_queue)


# Set-up file-input decoding
id_var, target1, target2, target3, target4, *cols, = tf.decode_cs(value, record_defaults=record_defaults)



tf_id_var = tf.stack(id_var)
tf_target = tf.stack(target1)
tf_features = tf.stack(cols)
tf_features = tf.reshape(features,(1, n_features))

x = tf.placeholder('float', [None, n_features])
y = tf.placeholder('float')



# Create archetecture depending on selection
if n_layers == 1:
    hidden_l1_wgts = tf.Variable(tf.randome_normal([n_features, n_nodes_hl1]))
    hidden_l1_bias = tf.Variable(tf.random_normal([n_nodes_hl1]))
    
    output_l_wgts = tf.Variable(tf.randome_normal([n_nodes_hl1, n_classes]))
    output_l_bias = tf.Variable(tf.random_normal([n_classes]))
    
    l1 = tf.add(tf.matmul(x, hidden_l1_wgts), hidden_l1_bias)
    l1 = tf.nn.relu(l1)
    
    output = tf.add(tf.matmul(l1, output_l_wgts), output_l_bias)
    
elif n_layers == 2:
    hidden_l1_wgts = tf.Variable(tf.randome_normal([n_features, n_nodes_hl1]))
    hidden_l1_bias = tf.Variable(tf.random_normal([n_nodes_hl1]))
    
    hidden_l2_wgts = tf.Variable(tf.randome_normal([n_nodes_hl1, n_nodes_hl2]))
    hidden_l2_bias = tf.Variable(tf.random_normal([n_nodes_hl2]))
    
    output_l_wgts = tf.Variable(tf.randome_normal([n_nodes_hl2, n_classes]))
    output_l_bias = tf.Variable(tf.random_normal([n_classes]))
    
    l1 = tf.add(tf.matmul(x, hidden_l1_wgts), hidden_l1_bias)
    l1 = tf.nn.relu(l1)
    
    l2 = tf.add(tf.matmul(l1, hidden_l2_wgts), hidden_l2_bias)
    l2 = tf.nn.relu(l2)
    
    output = tf.add(tf.matmul(l2, output_l_wgts), output_l_bias)
    
elif n_layers == 3:
    hidden_l1_wgts = tf.Variable(tf.randome_normal([n_features, n_nodes_hl1]))
    hidden_l1_bias = tf.Variable(tf.random_normal([n_nodes_hl1]))
    
    hidden_l2_wgts = tf.Variable(tf.randome_normal([n_nodes_hl1, n_nodes_hl2]))
    hidden_l2_bias = tf.Variable(tf.random_normal([n_nodes_hl2]))
    
    hidden_l3_wgts = tf.Variable(tf.randome_normal([n_nodes_hl2, n_nodes_hl3]))
    hidden_l3_bias = tf.Variable(tf.random_normal([n_nodes_hl3]))
    
    output_l_wgts = tf.Variable(tf.randome_normal([n_nodes_hl3, n_classes]))
    output_l_bias = tf.Variable(tf.random_normal([n_classes]))
    
    l1 = tf.add(tf.matmul(x, hidden_l1_wgts), hidden_l1_bias)
    l1 = tf.nn.relu(l1)
    
    l2 = tf.add(tf.matmul(l1, hidden_l2_wgts), hidden_l2_bias)
    l2 = tf.nn.relu(l2)
    
    l3 = tf.add(tf.matmul(l2, hidden_l3_wgts), hidden_l3_bias)
    l3 = tf.nn.relu(l3)
    
    output = tf.add(tf.matmul(l3, output_l_wgts), output_l_bias)



prediction = output
cost = tf.reduce_mean(tf.square(prediction - y))  # for MSE regression
#cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))  # for classification

optmzr = tf.trainl.AdamOptimizer()
optimizer = optmzr.minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    
    
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    
    msee = 0
    msee_list = []
    
    # The training loop
    for ada in range(700100):
        example, label = sess.run([features, Target])
        _, c = sess.run([optimizer, cost], feed_dict = {x: example, y: label})

    print("DONE")
    print("saving..", end='')
    saver.save(sess, dir + save_folder)
    print("..saved!")
    
    coord.request_stop()
    coord.join(threads)
    
    
    
