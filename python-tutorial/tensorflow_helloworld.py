import tensorflow as tf
import numpy as np

#创建数据
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3

#搭建模型
w=tf.Variable(tf.random_uniform([1],-1.0,1.0))
b=tf.Variable(tf.zeros([1]))
y=w*x_data+b

#损失函数/代价函数
loss = tf.reduce_mean(tf.square(y_data-y))

#梯度下降
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

#训练模型
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(100):
        sess.run(train_step)
        if step % 20 == 0:
            print(step,sess.run(w),sess.run(b))