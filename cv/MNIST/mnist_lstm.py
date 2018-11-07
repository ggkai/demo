#导入包
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#设置超参数
BATCH_SIZE=64 #批处理数量
TIME_STEP=28 #rnn时间步长，即长度
INPUT_SIZE=28 #rnn输入尺寸，即宽度
TRAINGING_STEP=1000#训练次数
LR=0.01 #学习速率

#从本地读取mnist数据
mnist=input_data.read_data_sets('./mnist_data',one_hot=True)
'''
训练集数据：mnist.train.images（55000，784）
训练集标签：mnist.train.labels（55000,10）
测试集数据：mnist.test.images（10000,784）
测试集标签：mnist.test.labels（10000,10）
验证集数据：mnist.validation.images（5000，784）
验证集标签：mnist.validation.labels（5000，10）
'''

#占位符
tf_x=tf.placeholder(tf.float32,[None,TIME_STEP*INPUT_SIZE]) #(batch，28*28=784)
tf_y=tf.placeholder(tf.int32,[None,10]) #(batch,10)#注意数据类型

#RNN
rnn_cell=tf.nn.rnn_cell.BasicLSTMCell(num_units=256) #hidden unit

x_reshape=tf.reshape(tf_x,[-1,TIME_STEP,INPUT_SIZE])# (batch, height, width)
outputs,state=tf.nn.dynamic_rnn(cell=rnn_cell,inputs=x_reshape,initial_state=None,dtype=tf.float32,time_major=False) #input数据要求(timestep, batch, input)

output=tf.layers.dense(inputs=outputs[:,-1,:],units=10)

#损失函数
loss=tf.losses.softmax_cross_entropy(onehot_labels=tf_y,logits=output)

#优化器
train_step=tf.train.AdamOptimizer(LR).minimize(loss)

#计算准确率
accuracy=tf.metrics.accuracy(labels=tf.argmax(tf_y,axis=1),predictions=tf.argmax(output,axis=1))[1]# 返回两个值，取第一个，即acc

#会话
sess=tf.Session()

#全局变量、局部变量初始化
init_op=tf.group(tf.global_variables_initializer(),tf.local_variables_initializer())
sess.run(init_op)

#训练
for step in range(TRAINGING_STEP):
    #随机批量样本
    batch_x,batch_y=mnist.train.next_batch(BATCH_SIZE)
    _,loss_=sess.run([train_step,loss],feed_dict={tf_x:batch_x,tf_y:batch_y})#返回两个值，取第二个，即loss，注意命名不能重复
    if step%50==0:
        #测试集准确率
        acc=sess.run(accuracy,feed_dict={tf_x:mnist.test.images,tf_y:mnist.test.labels})
        print('train loss:',loss_,'test acc:',acc)