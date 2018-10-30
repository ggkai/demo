import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#添加层函数
def add_layer(inputs,in_size,out_size,activation_function=None):
    w=tf.Variable(tf.random_normal([in_size,out_size]))
    b=tf.Variable(tf.zeros([1,out_size])+0.1)
    y_=tf.matmul(inputs,w)+b
    if activation_function is None:
        outputs=y_
    else:
        outputs=activation_function(y_)
    return outputs
#创建数据
x_data=np.linspace(-1,1,300)[:,np.newaxis]
noise=np.random.normal(loc=0,scale=0.05,size=x_data.shape)
y_data=np.square(x_data)-0.5+noise

#创建placeholder
xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])

#输入层
layer_1=add_layer(xs,1,10,activation_function=tf.nn.relu) #(300,1)*(1*10)->(300,10)

#输出层
prediction=add_layer(layer_1,10,1,activation_function=None) #(300,10)*(10,1)->(300,1)

#代价函数
loss=tf.reduce_mean(tf.square(prediction-ys))

#可视化
fig=plt.figure()#创建画布
ax=fig.add_subplot(1,1,1)#创建子图
ax.scatter(x_data,y_data) #散点图
plt.ion()#持续刷新axes
plt.show()

#训练
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) #初始化变量
    for i in range(1000):#学习循环
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if i %10 == 0:
            print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
            prediction_value=sess.run(prediction,feed_dict={xs:x_data})
            try:
                ax.lines.remove(lines[0])
            except:
                pass
            lines=ax.plot(x_data,prediction_value)#画曲线
            plt.pause(0.1)