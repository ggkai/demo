import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#设置随机种子
tf.set_random_seed(1)
np.random.seed(1)

#参数
N_SAMPLES=20#样本数量
N_HIDDEN=300#输出的大小
LR=0.01#学习速率

#创建数据
train_x=np.linspace(-1,1,N_SAMPLES)[:,np.newaxis]#(20.)转为(20,1)
train_y=train_x+0.3*np.random.randn(N_SAMPLES)[:,np.newaxis]#(20.)转为(20,1)

test_x=train_x.copy()
test_y=test_x+0.3*np.random.randn(N_SAMPLES)[:,np.newaxis]

#绘制图
plt.subplot(1,3,1)
plt.scatter(train_x,train_y,c='magenta',s=50,alpha=0.5,label='train')#训练数据绘图
plt.scatter(test_x,test_y,c='c',s=50,alpha=0.5,label='test')#test数据绘图
plt.ylim(-2.5,2.5)#y轴的最大最小值
plt.title('all data')


#占位符
tf_x=tf.placeholder(tf.float32,[None,1])
tf_y=tf.placeholder(tf.float32,[None,1])
tf_is_training=tf.placeholder(tf.bool,None)

#overfitting
o1=tf.layers.dense(inputs=tf_x,units=N_HIDDEN,activation=tf.nn.relu)#隐藏层
o2=tf.layers.dense(inputs=o1,units=N_HIDDEN,activation=tf.nn.relu)#隐藏层
o_out=tf.layers.dense(inputs=o2,units=1)#输出层
overfit_loss=tf.losses.mean_squared_error(tf_y,o_out)#损失函数
overfit_train=tf.train.AdamOptimizer(LR).minimize(overfit_loss)#优化器

#dropout
d1=tf.layers.dense(inputs=tf_x,units=N_HIDDEN,activation=tf.nn.relu)#隐藏层
d2=tf.layers.dropout(inputs=d1,rate=0.5,training=tf_is_training)#dropout层
d3=tf.layers.dense(inputs=d2,units=N_HIDDEN,activation=tf.nn.relu)#隐藏层
d4=tf.layers.dropout(inputs=d3,rate=0.5,training=tf_is_training)#dropout层
d_out=tf.layers.dense(inputs=d4,units=1)
dropout_loss=tf.losses.mean_squared_error(tf_y,d_out)#损失函数
dropout_train=tf.train.AdamOptimizer(LR).minimize(dropout_loss)#优化器

#训练
sess=tf.Session()
sess.run(tf.global_variables_initializer())
plt.ion()#绘图交互模式


for i in range(500):
    sess.run([overfit_train,dropout_train],feed_dict={tf_x:train_x,tf_y:train_y,tf_is_training:True})
    if i %10==0:
        plt.subplot(1, 3, 2)
        plt.cla()
        train_overfit_loss_, train_dropout_loss_, train_o_out_, train_d_out_=sess.run([overfit_loss,dropout_loss,o_out,d_out],feed_dict={tf_x:train_x,tf_y:train_y,tf_is_training:False})
        plt.scatter(train_x,train_y,c='m',s=50,alpha=0.5,label='train data')
        plt.plot(train_x,train_o_out_,'r-',lw=3,label='overfitting')
        plt.plot(train_x,train_d_out_,'b--',lw=3,label='dropout')
        plt.text(x=-1,y=-1.5,s='overfitting loss=%.4f'%train_overfit_loss_,fontdict={'size':20,'color':'red'})
        plt.text(x=-1,y=-1.8,s='dropout loss=%.4f'%train_dropout_loss_,fontdict={'size':20,'color':'red'})
        plt.legend(loc='upper left')#添加图例
        plt.ylim((-2,2))
        plt.title('train data')
        plt.pause(0.1)

        plt.subplot(1,3,3)
        plt.cla()
        test_overfit_loss_, test_dropout_loss_, test_o_out_, test_d_out_ = sess.run([overfit_loss, dropout_loss, o_out, d_out],
                                                                feed_dict={tf_x: test_x, tf_y: test_y,
                                                                           tf_is_training: False})
        plt.scatter(test_x, test_y, c='c', s=50, alpha=0.5, label='test data')
        plt.plot(test_x, test_o_out_, 'r-', lw=3, label='overfitting')
        plt.plot(test_x, test_d_out_, 'b--', lw=3, label='dropout')
        plt.text(x=-1, y=-1.5, s='overfitting loss=%.4f' % test_overfit_loss_, fontdict={'size': 20, 'color': 'red'})
        plt.text(x=-1, y=-1.8, s='dropout loss=%.4f' % test_dropout_loss_, fontdict={'size': 20, 'color': 'red'})
        plt.legend(loc='upper left')  # 添加图例
        plt.ylim((-2, 2))
        plt.title('test data')
        plt.pause(0.1)
plt.ioff()
plt.show()