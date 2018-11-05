#导入包
import tensorflow as tf
# import numpy as np
# import matplotlib.pylab as plt
from tensorflow.examples.tutorials.mnist import input_data

#设置超参数
BATCH_SIZE=64 #批处理数量
TIME_STEP=28 #rnn时间步长，即长度
INPUT_SIZE=28 #rnn输入尺寸，即宽度
TRAINGING_STEP=1000#训练次数
LR=0.01 #学习速率

#从本地读取mnist数据
mnist=input_data.read_data_sets('./mnist_data',one_hot=True)

#占位符
x=tf.placeholder(tf.float32,[None,TIME_STEP*INPUT_SIZE]) #(batch，28*28=784)
tf_x=tf.reshape(x,[-1,TIME_STEP,BATCH_SIZE,1])# (-1,28,28,1)
tf_y=tf.placeholder(tf.float32,[None,10]) #(10,)

#RNN
rnn_cell=tf.nn.rnn_cell.BasicLSTMCell(num_units=256) #hidden size

outputs,state=tf.nn.dynamic_rnn(rnn_cell,tf_x,initial_state=None,dtype=tf.float32) #(time step, batch, input)

output=tf.layer.dense(outputs[:,-1,:],10)

loss=tf.losses.softmax_cross_entropy(onehot_labels=tf_y,logits=output)

train_step=tf.train.AdamOptimizer(LR).minimize(loss)

accuracy=tf.metrics.accuracy(labels=tf.argmax(tf_y,axis=1),predictions=tf.argmax(output,axis=1),)[1]

sess=tf.Session()

init_op=tf.group(tf.global_variables_initializer(),tf.local_variables_initializer())

sess.run(init_op)

for step in range(500):
    batch_x,batch_y=mnist.train.next_batch(BATCH_SIZE)
    _,loss=sess.run([train_step,loss],feed_dict={tf_x:batch_x,tf_y:batch_y})
    if step%50==0:
        acc=sess.run(accuracy,feed_dict={tf_x:mnist.test.images[:2000],tf_y:mnist.test.labels[:2000]})
        print(acc)