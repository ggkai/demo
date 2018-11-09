import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
from mpl_toolkits.mplot3d import Axes3D#3D绘图
from matplotlib import cm
import numpy as np

#设置超参数
BATCH_SIZE = 64
TRAIN_STEP = 1000
# TRAIN_EPOCHS = 10
LR = 0.02
TEST_IMAGE_NUM = 5
UNITES_0 = 784
UNITES_1 = 256
UNITES_2 = 64
UNITES_3 = 12
UNITES_4 = 3

#读取数据
mnist=input_data.read_data_sets('./mnist_data',one_hot=True)
test_x=mnist.test.images[:200]
test_y=mnist.test.labels[:200]


#占位符
tf_x=tf.placeholder(tf.float32,[None,28*28])

#encoder
encoder_layer_1=tf.layers.dense(inputs=tf_x,units=UNITES_1,activation=tf.nn.tanh)
encoder_layer_2=tf.layers.dense(inputs=encoder_layer_1,units=UNITES_2,activation=tf.nn.tanh)
encoder_layer_3=tf.layers.dense(inputs=encoder_layer_2,units=UNITES_3,activation=tf.nn.tanh)
encoder_layer_4=tf.layers.dense(inputs=encoder_layer_3,units=UNITES_4,activation=None)

#decoder
decoder_layer_1=tf.layers.dense(inputs=encoder_layer_4,units=UNITES_3,activation=tf.nn.tanh)
decoder_layer_2=tf.layers.dense(inputs=decoder_layer_1,units=UNITES_2,activation=tf.nn.tanh)
decoder_layer_3=tf.layers.dense(inputs=decoder_layer_2,units=UNITES_1,activation=tf.nn.tanh)
decoder_layer_4=tf.layers.dense(inputs=decoder_layer_1,units=UNITES_0,activation=tf.nn.tanh)#改为sigmoid好像也不行

#损失函数
loss=tf.losses.mean_squared_error(labels=tf_x,predictions=decoder_layer_4)#输入和输出比较
train_step=tf.train.AdamOptimizer(LR).minimize(loss)

#训练
sess=tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(TRAIN_STEP):
    batch_x,batch_y=mnist.train.next_batch(BATCH_SIZE)
    _,loss_,=sess.run([train_step,loss],feed_dict={tf_x:batch_x})
    if step%50==0:
        print('train loss:',loss_)
#测试
test_loss=sess.run(loss,feed_dict={tf_x:test_x})
print('test loss:',test_loss)

#显示部分输入图片和decoder图片
fig1, ax = plt.subplots(nrows=2, ncols=5)  # 创建figure 1，有2个axes，每个axes5个subplot
test_images=mnist.test.images[:TEST_IMAGE_NUM]
decoder_images=sess.run(decoder_layer_4,feed_dict={tf_x:test_images})
print(decoder_images.shape)
for i in range(TEST_IMAGE_NUM):
    ax[0][i].imshow(np.reshape(test_images[i], (28, 28)))
    ax[1][i].imshow(np.reshape(decoder_images[i],(28,28)))

# #3维显示encoder
# encoder_images=sess.run(encoder_layer_4,feed_dict={tf_x:test_x})#获得encoder数据(batch,UNITES_4)，即(200,3)
# fig2=plt.figure(2)#创建画布
# ax2=Axes3D(fig2)#添加第三个轴
# x_=encoder_images[:,0]#第一维的encoder
# y_=encoder_images[:,1]
# z_=encoder_images[:,2]
#
# ax2.set_xlim(x_.min(),x_.max())
# ax2.set_ylim(y_.min(),y_.max())
# ax2.set_zlim(z_.min(),z_.max())
# color=cm.rainbow(np.linspace(0,10,9))
# plt.scatter(x_,y_,z_,c=color)
# plt.show()
#
# #2维显示encoder
# encoder_result = sess.run(encoder_op, feed_dict={X: mnist.test.images})
# plt.scatter(encoder_result[:, 0], encoder_result[:, 1], c=mnist.test.labels)
# plt.colorbar()
# plt.show()