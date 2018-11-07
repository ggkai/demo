from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

batch_size = 100
hidden1_nodes = 200
with tf.name_scope('Input'):
    x = tf.placeholder(tf.float32,shape=(None,784))
    y = tf.placeholder(tf.float32,shape=(None,10))
with tf.name_scope('Inference'):
    w1 = tf.Variable(tf.random_normal([784,hidden1_nodes],stddev=0.1))
    w2 = tf.Variable(tf.random_normal([hidden1_nodes,10],stddev=0.1))
    b1 = tf.Variable(tf.random_normal([hidden1_nodes],stddev=0.1))
    b2 = tf.Variable(tf.random_normal([10],stddev=0.1))
    hidden = tf.nn.relu(tf.matmul(x,w1)+b1)
    y_predict = tf.nn.relu(tf.matmul(hidden,w2)+b2)

with tf.name_scope('Loss'):
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_predict))
with tf.name_scope('Train'):
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
with tf.name_scope('Accuracy'):
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_predict, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(10000):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
        if i%1000==0:
            print ('Phase'+str(i/1000+1)+':',sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))
writer = tf.summary.FileWriter("./mnist_nn_log",sess.graph)
writer.close()