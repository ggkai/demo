import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# hyper Parameters
N_SAMPLE = 2000
BATCH_SIZE = 64
EPOCH = 12
LR = 0.03
N_HIDDEN = 80
ACTIVATION = tf.nn.tanh
EPSILON=1e-3

#train data
train_x=np.linspace(-7,10,N_SAMPLE)[:,np.newaxis]
np.random.shuffle(train_x)
noise=np.random.normal(0,2,train_x.shape)
train_y=np.square(train_x)-5+noise
train_data=np.hstack((train_x,train_y))

# plot train data
plt.figure(1)
plt.scatter(train_x, train_y, c='#FF9359', s=50, alpha=0.5, label='train data')
plt.legend(loc='upper left')

#test data
test_x=np.linspace(-7,10,200)[:,np.newaxis]
noise=np.random.normal(0,2,test_x.shape)
test_y=np.square(test_x)-5+noise

#tensorflow placeholder
tf_x=tf.placeholder(tf.float32,[None,1])
tf_y=tf.placeholder(tf.float32,[None,1])
tf_is_train=tf.placeholder(tf.bool,None)

#input layer
layer1=tf.layers.dense(inputs=tf_x,units=N_HIDDEN,activation=ACTIVATION)

#batch normalization layer
'''tf.nn.batch_normalization()'''
beta = tf.Variable(tf.constant(0.0, shape=[layer1.shape[-1]]), trainable=True)
gamma = tf.Variable(tf.constant(1.0, shape=[layer1.shape[-1]]), trainable=True)
axises = np.arange(len(layer1.shape) - 1)
axis=list(range(len(layer1.shape)-1))
batch_mean, batch_var = tf.nn.moments(layer1,axis)
normed_1 = tf.nn.batch_normalization(x=layer1, mean=batch_mean, variance=batch_var,
                                   offset=beta, scale=gamma, variance_epsilon=EPSILON)
'''tf.layers.batch_normalization()'''
normed_2=tf.layers.batch_normalization(layer1,training=tf_is_train)

'''tf.contrib.layers.batch_norm()'''
normed_3=tf.contrib.layers.batch_norm(layer1,is_training=tf_is_train)

#output layer
out=tf.layers.dense(inputs=normed_1,units=1,activation=ACTIVATION)

#train
loss=tf.losses.mean_squared_error(tf_y,out)
train_step=tf.train.AdamOptimizer(LR).minimize(loss)

sess=tf.Session()
sess.run(tf.global_variables_initializer())
for epoch in range(EPOCH):
    print('Epoch: ', epoch)
    np.random.shuffle(train_data)
    step = 0
    in_epoch = True
    while in_epoch:
        b_s, b_e = (step*BATCH_SIZE) % len(train_data), ((step+1)*BATCH_SIZE) % len(train_data) # batch index
        step += 1
        if b_e < b_s:
            b_e = len(train_data)
            in_epoch = False
        b_x, b_y = train_data[b_s: b_e, 0:1], train_data[b_s: b_e, 1:2]
        _,loss_=sess.run([train_step,loss], feed_dict={tf_x: b_x, tf_y: b_y,tf_is_train:True})
        print(step,'step:',loss_)

#test
loss_test,out_test=sess.run([loss,out],feed_dict={tf_x:test_x,tf_y:test_y,tf_is_train:False})
print('test loss:',loss_test)


#plot test
plt.figure(2)
plt.scatter(test_x,test_y)
plt.plot(test_x,out_test)
plt.show()
