import tensorflow as tf
import numpy as np

#导入数据，报错
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)

# 已经下载好了数据
print(mnist.train.images.shape,mnist.train.labels.shape)    #训练集数据的维度
print('labels',mnist.validation.labels[0:10,:])
print('images',mnist.validation.images[0:10,:])

# 构建计算图
w=tf.Variable(tf.zeros([784,10]))
bias=tf.Variable(tf.zeros([10]))

x_data=tf.placeholder(tf.float32,[None,784])
y_data=tf.placeholder(tf.float32,[None,10])
#softmax激活
y=tf.nn.softmax(tf.matmul(x_data,w)+bias)
#按行，两个分布的交叉熵，平均值
cross_entropy=tf.reduce_mean(-tf.reduce_sum(y_data*tf.log(y),axis=1))
#优化器+交叉熵
train_graph=tf.train.GradientDescentOptimizer(0.15).minimize(cross_entropy)

# 构建会话
with tf.Session() as sess:
    #变量初始化
    sess.run(tf.global_variables_initializer())
    for i in range(1001):
        if i%50==0:
            #比较预测值和实际值，返回布尔值
            match=tf.equal(tf.argmax(y,axis=1),tf.argmax(y_data,axis=1))
            #计算准确率，x_data传到y的计算图中
            train_acc=sess.run(match,feed_dict={x_data:mnist.train.images,y_data:mnist.train.labels})
            print(i,sum(train_acc)/len(train_acc))
        #随机取样本
        x_s,y_s=mnist.train.next_batch(100)
        #训练模型
        sess.run(train_graph,feed_dict={x_data:x_s,y_data:y_s})
    #测试数据去预测
    #另一种写法：sess.run(y,feed_dict={x_data:mnist.validation.images})
    y=tf.nn.softmax(tf.matmul(mnist.validation.images,w)+bias)
    test_acc=sess.run(match,feed_dict={x_data:mnist.validation.images,y_data:mnist.validation.labels})
    print('预测值：',sum(test_acc)/len(test_acc))