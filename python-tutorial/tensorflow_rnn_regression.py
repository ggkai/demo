'''
用sin曲线预测cos曲线
疑问：为什么loss降不下去，如果调整initial_state
'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#超参数
TIME_STEP = 10
INPUT_SIZE = 1
CELL_SIZE = 32
BATCH_SIZE = 1
TRAIN_STEP = 50
LR = 0.01

#造数据
def generation_data(step):
    steps = np.linspace(step*np.pi,(step+1)*np.pi, TIME_STEP, dtype=np.float32)
    x_sin = np.sin(steps)[np.newaxis,:,np.newaxis] #(batch_size,time_step,input_size)
    y_cos = np.cos(steps)[np.newaxis,:,np.newaxis] #(batch_size,time_step,input_size)
    return steps,x_sin,y_cos

#占位符
x=tf.placeholder(tf.float32,shape=[None,TIME_STEP,INPUT_SIZE])#(batch_size,time_step,input_size)
y=tf.placeholder(tf.float32,shape=[None,TIME_STEP,INPUT_SIZE])#(batch_size,time_step,input_size)

#构建rnn
rnn_cell = tf.nn.rnn_cell.BasicRNNCell(num_units=CELL_SIZE) #初始化RNNCell的神经元数量，输入2D
init_state=rnn_cell.zero_state(batch_size=BATCH_SIZE,dtype=tf.float32) #零值初始化RNNCell网络的参数，c0、h0向量，返回[batch_size, state_size]
outputs,state=tf.nn.dynamic_rnn(cell=rnn_cell,inputs=x,initial_state=init_state,dtype=tf.float32,time_major=False)#构建rnn，输出 3D(batch, time step, input)

#输出3D转2D
to_2D=tf.reshape(outputs,[-1,CELL_SIZE])

#输出层
out_layer=tf.layers.dense(to_2D,INPUT_SIZE)

#输出2D转3D
to_3D=tf.reshape(out_layer,[-1,TIME_STEP,INPUT_SIZE])

#损失函数
loss=tf.losses.mean_squared_error(labels=y,predictions=to_3D)#labels为3D，predictions为3D

#优化器
train_step=tf.train.AdamOptimizer(LR).minimize(loss)

#绘图，进入交互模式
plt.figure(1,figsize=(10,5))
plt.ion()

#训练模型
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(TRAIN_STEP):
    #训练数据
    steps,x_sin,y_cos=generation_data(step)
    #进行训练
    _,pred,loss_min=sess.run([train_step,to_3D,loss],feed_dict={x:x_sin,y:y_cos})
    #绘图
    plt.plot(steps,y_cos.flatten(),'r-')
    plt.plot(steps,pred.flatten(),'b-')
    # plt.draw()
    plt.pause(0.1)
plt.ioff()
plt.show()

print(loss_min)