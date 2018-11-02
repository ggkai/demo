import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

#设置随机种子
tf.set_random_seed(1)
np.random.seed(1)

# fake data class 0
n_data = np.ones((100, 2))
x0 = np.random.normal(2*n_data, 1)      # x shape=(100, 2)
y0 = np.zeros(100)                      # y shape=(100, )

# fake data class 1
x1 = np.random.normal(-2*n_data, 1)     # x shape=(100, 2)
y1 = np.ones(100)                       # y shape=(100, )

# 训练数据
x_data = np.vstack((x0, x1))  # shape (200, 2)
y_data = np.hstack((y0, y1))  # shape (200, )

# plot data
plt.subplot(1,2,1)
plt.scatter(x0[:,0], x0[:,1])
plt.scatter(x1[:,0], x1[:,1])
plt.xlabel('原始数据')
plt.show()

#占位符
x = tf.placeholder(tf.float32, x_data.shape)
y = tf.placeholder(tf.int32, y_data.shape)

#输入层
l1 = tf.layers.dense(x, 10, tf.nn.relu) #输出10维

#输出层
output = tf.layers.dense(l1, 2) #输出2维

#代价函数
loss = tf.losses.sparse_softmax_cross_entropy(labels=y, logits=output)

#计算精确度
accuracy = tf.metrics.accuracy(labels=tf.squeeze(y), predictions=tf.argmax(output, axis=1))[1]

#优化器
train_step=tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(loss)

#训练
with tf.Session() as sess:
    init_Var=tf.group(tf.global_variables_initializer(),tf.local_variables_initializer())
    sess.run(init_Var)
    plt.ion() #进入交互模式
    plt.subplot(1, 2, 2)
    for step in range(100):
        # train and net output
        _, acc, pred = sess.run([train_step, accuracy, output], {x:x_data, y:y_data}) #多值输出
        if step % 2 == 0: # 绘制学习过程
            print(acc)
            plt.cla() #清理axes，避免重叠
            plt.scatter(x_data[:, 0], x_data[:, 1], c=pred.argmax(1), s=100, lw=0, cmap='RdYlGn')
            plt.text(1.5, -4, 'Accuracy=%.2f' % acc, fontdict={'size': 12, 'color': 'red'})
            plt.pause(0.1)
    plt.ioff()  # 关闭交互模式
    plt.show()  # 显示
    # plt.close()
    print('done')