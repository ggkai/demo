'''
二、训练和保存模型
'''
# 导入包
import tensorflow as tf

# 模型保存前，清除所有变量
tf.reset_default_graph()

# 获取数据
path_train = './OCR_data/trainImages/'
path_test = './OCR_data/testImages/'

data_train, labels_train = ImgTrans(path=path_train).getImgData()
data_test, labels_test = ImgTrans(path=path_test).getImgData()

# 标签数据独热编码
labels_train_onehot = tf.one_hot(labels_train, 10)
labels_test_onehot = tf.one_hot(labels_test, 10)

# 构建计算图
w = tf.Variable(tf.zeros([784, 10]), name='w')
bias = tf.Variable(tf.zeros([10]), name='bias')

# x_data=tf.placeholder(tf.float32,[None,784])
# y_data=tf.placeholder(tf.float32,[None,10])

# 动态学习速率
global_step = tf.Variable(0, trainable=False)  # false表示这个变量不更新
learning_rate = tf.train.exponential_decay(0.1, global_step, 50, 0.96)

# softmax激活函数
y = tf.nn.softmax(tf.matmul(data_train, w) + bias)

# 交叉熵目标函数
cross_entropy = tf.reduce_mean(-tf.reduce_sum(labels_train_onehot * tf.log(y), axis=1))  # 按行，两个分布的交叉熵，平均值

# 优化器，最小交叉熵
train = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy, global_step=global_step)  # 动态学习速率

# 构建会话
with tf.Session() as sess:
    # 变量初始化
    sess.run(tf.global_variables_initializer())
    for i in range(501):
        if i % 50 == 0:
            # 比较函数
            match = tf.equal(tf.argmax(y, axis=1), tf.argmax(labels_train_onehot, axis=1))  # 比较预测值和实际值，返回布尔值
            # 计算准确率
            acc = sess.run(match)
            # 打印准确率
            print(i, sum(acc) / len(acc), sess.run(learning_rate))
        # 执行独热编码操作
        # labels_tr,labels_te = sess.run([labels_train_onehot,labels_test_onehot])

        # 执行训练模型
        sess.run(train)
    # 测试集效果
    val_y = tf.nn.softmax(tf.matmul(data_test, w) + bias)
    val_match = tf.equal(tf.argmax(val_y, axis=1), tf.argmax(labels_test_onehot, axis=1))
    val_acc = sess.run(val_match)
    print('测试值', sum(val_acc) / len(val_acc))

    # 创建Saver实例，在会话中保存模型
    saver = tf.train.Saver()
    saver.save(sess, './OCR_model/train_model')

    # 问题1:feed_dict不能用tensor对象
    # 问题2:随机去样本只能针对无法针对np.ndarray
    # 问题3:labels_tr,labels_te = sess.run([labels_train_onehot,labels_test_onehot])？？？
    # 问题4:独热编码编程10维？tf.onehot(x,10)查看labels_train_onehot.shape


'''
模型调用
'''

# 导入包
import tensorflow as tf

# 获取数据
path_test='./OCR_data/testImages/'
data_test,labels_test=ImgTrans(path=path_test).getImgData()
labels_test_onehot=tf.one_hot(labels_test,10)

#构建计算图
sess=tf.Session()

#导入计算图
saver=tf.train.import_meta_graph('./OCR_model/train_model.meta')

#导入计算图参数
saver.restore(sess,tf.train.latest_checkpoint('./OCR_model/'))

#获得模型
graph = tf.get_default_graph()

#测试效果
w = graph.get_tensor_by_name('w:0')
b = graph.get_tensor_by_name('bias:0')
test_pre = tf.nn.softmax(tf.matmul(data_test,w)+b)
test_match=tf.equal(tf.argmax(val_y,axis=1),tf.argmax(labels_test_onehot,axis=1))
test_acc=sess.run(test_match)
print('测试值',sum(test_acc)/len(test_acc))

