import tensorflow as tf
from sklearn.model_selection import train_test_split
import random
import numpy as np

# 数据集划分
train_x, test_x, train_y, test_y = train_test_split(data)

# 占位符
x = tf.placeholder(tf.float32, shape=[None, 784], name='x_data')
y_ = tf.placeholder(tf.float32, shape=[None, 10], mame='y_data')


# 定义权重变量函数
def weight_Variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


# 定义偏置项变量函数
def bias_Variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# 定义卷积函数
def conv2d(x, w):
    return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')


# 定义池化函数
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# 定义dropout函数
def dropout(self, x, keep):  # 随机让某些权重不更新，保持某个数
    return tf.nn.dropout(x, keep)


def cnnLayer():
    # 第一层卷积
    x_flat = tf.reshape(x, [-1, 28, 28, 1])  # 将784转为28*28
    w_conv1 = weight_Variable([5, 5, 1, 32])
    b_conv1 = bias_Variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_flat, w_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    # 第二层卷积
    w_conv2 = weight_Variable([5, 5, 32, 64])
    b_conv2 = bias_Variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    # 第三层卷积
    w_conv2 = weight_Variable([5, 5, 32, 64])
    b_conv2 = bias_Variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    # 全链接层
    w_fcl = weight_Variable([7 * 7 * 64, 1024])  # 1024个节点
    b_fcl = weight_Variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fcl = tf.nn.relu(tf.matmul(h_pool2_flat, w_fcl) + b_fcl)

    # dropout层
    keep_prob = tf.placeholder(tf.float32)
    h_fcl_drop = tf.nn.dropout(h_fcl, keep_prob)

    # softmax输出层
    w_fc2 = weight_Variable([1024, 10])
    b_fc2 = bias_Variable([10])
    y_conv = tf.nn.softmax(tf.matmul(h_fcl_drop, w_fc2) + b_fc2)

    # 训练
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))  # 定义损失函数
    # train_step=tf.train.AdadeltaOptimizer(1e-4).minimize(cross_entropy)#优化器
    train_step = tf.train.GradientDescentOptimizer(0.15).minimize(cross_entropy)

    sess = tf.Session()  # 构建会话
    sess.run(tf.global_variables_initializer())  # 变量初始化
    for i in range(1001):
        batch = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
        if i % 10 == 0:
            pre = tf.equal(tf.argmax(y_conv, axis=1), tf.argmax(y_, axis=1))  # 输出和实际值比较
            acc = sess.run(pre, feed_dict={x: mnist.validation.images, y_: mnist.validation.labels, keep_prob: 1.0})
            print(sum(acc) / len(acc))  # 打印输出
    sess.close()