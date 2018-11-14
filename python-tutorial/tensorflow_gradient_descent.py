import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#超参数
LR = 0.1
TRIN_STEP = 100
REAL_W = 1.2
REAL_B = 2.5
INIT_W = 5
INIT_B = 4

#占位符
tf_x=tf.placeholder(tf.float32,[None,1])
tf_y=tf.placeholder(tf.float32,[None,1])


#定义变量
w=tf.Variable(initial_value=INIT_W,dtype=tf.float32)
b=tf.Variable(initial_value=INIT_B,dtype=tf.float32)

#定义模型
y=tf.matmul(tf_x,w)+b

#损失函数
loss=tf.losses.mean_squared_error(tf_y,y)
train_step=tf.train.AdamOptimizer(LR).minimize(loss)

#数据
x_data=np.linspace(-1,1,200)[:,np.newaxis]#(200,)->(200,1)
noise=np.random.normal(0,1,x_data.shape)#200个（0，1）之间的数
y_data=1.2*x_data+2.5+noise

#训练
sess=tf.Session()
sess.run(tf.global_variables_initializer())

w_list=[]
b_list=[]
loss_list=[]

for step in range(TRIN_STEP):
    w_,b_,loss_,_=sess.run([w,b,loss,train_step],feed_dict={tf_x:x_data,tf_y:y_data})
    w_list.append(w_)
    b_list.append(b_)
    loss_list.append(loss_)
y_pred=sess.run(y,feed_dict={tf_x:x_data,tf_y:y_data})

#数据拟合可视化
plt.figure(1)
plt.scatter(x_data,y_data,c='r',alpha=0.5)
plt.plot(x_data,y_pred,lw=2)

#梯度下降可视化
fig=plt.figure(2)
ax=Axes3D(fig)
w_3D,b_3D=np.meshgrid(np.linspace(-2,7,30),np.linspace(-2,7,30))#参数空间，二维矩阵

loss_3D=np.array([np.mean(np.square((x_data * w_ + b_) - y_data)) for w_,b_ in zip(w_3D.ravel(),b_3D.ravel())]).reshape(w_3D.shape)
ax.plot_surface(w_3D,b_3D,loss_3D,cmap=plt.get_cmap('rainbow'))
# weight=np.array(w_list.ravel())
# bias=np.array(b_list.ravel())

ax.scatter(w_list[0],b_list[0],zs=loss_list[0],s=300,c='r')#初始化参数空间
ax.set_xlabel('w')
ax.set_ylabel('b')
ax.plot(w_list,b_list,zd=loss_list,zdir='z',c='r',lw=2)
plt.show()