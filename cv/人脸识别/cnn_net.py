import tensorflow as tf
from sklearn.model_selection import train_test_split
import random
import numpy as np
from getimgdata import GetImgData
import os

# 数据集划分
path='./data/small_img_gray'
imgs,labels,num_name=GetImgData(dir=path).read_img()
train_x, test_x, train_y, test_y = train_test_split(imgs,labels,test_size=0.2,random_state=10)

# 创建模型存储文件
if not os.path.exists('./train_model'):
    os.mkdir('./train_model')

class CnnNet:
    def __init__(self,imgs=train_x,labels=train_y,keep_prob_5=0.5,keep_prob_7=0.75,modelfile='./train_model'):
        '''
        :param imgs: 训练数据(560,64,64)
        :param labels: 训练标签(560,7)
        :param keep_prob_5: dropout参数
        :param modelfile: 模型文件保存路径
        '''
        tf.reset_default_graph()
        self.xdata=imgs
        self.labels=labels
        self.size=imgs.shape[1] #图片宽度
        self.outnode=labels.shape[1] #输出神经元的个数
        self.x=tf.placeholder(tf.float32,shape=[None,self.size,self.size,1],name='x_data') #占位符
        self.y_=tf.placeholder(tf.float32,shape=[None,self.outnode],name='y_data') #占位符
        self.modelfile=modelfile
        self.keep_prob_5=keep_prob_5
        self.keep_prob_7=keep_prob_7

    def weight_Variable(self,shape):
        '''
        定义权重变量函数
        :param shape: 形状
        :return: 返回权重变量
        '''
        initial = tf.random_normal(shape=shape,stddev=0.01) #w值随机初始化，shape为shape
        return tf.Variable(initial)

    def bias_Variable(self,shape):
        '''
        定义偏置项变量函数
        :param shape: 形状
        :return: 返回偏置项变量
        '''
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)

    def conv2d(self,x,w):
        '''
        定义卷积函数
        :param w: 权重
        :return:
        '''
        return tf.nn.conv2d(input=x,filter=w, strides=[1, 1, 1, 1], padding='SAME') #filter取w的shape


    def max_pool_2x2(self,x):
        '''
        定义池化函数
        :return:
        '''
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    def dropout(self,x, keep_prob):
        '''
        定义dropout函数，随机让某些权重不更新，保持某个数
        :param keep: 保留比例
        :return: 返回留下来的
        '''
        return tf.nn.dropout(x, keep_prob)

    def cnnLayer(self):
        # 第一层卷积
        # 输入train_x的shape:(560,64,64)
        w1 = self.weight_Variable([3,3,1,32]) # 32个卷积核（3，3，1）
        b1 = self.bias_Variable([32]) # 32个偏置项
        conv1 = tf.nn.relu(self.conv2d(self.x, w1) + b1) #卷积层，输出（62，62，32）
        pool1 = self.max_pool_2x2(conv1) #池化层，输出（31，31，32）

        # 第二层卷积
        w2 = self.weight_Variable([3,3,32,64]) #64个卷积核（3，3，32）
        b2 = self.bias_Variable([64]) #64个偏置项
        conv2 = tf.nn.relu(self.conv2d(pool1, w2) + b2) #卷积层，输出（29，29，64）
        pool2 = self.max_pool_2x2(conv2) #池化层，输出（14，14，64）

        # 第三层卷积
        w3 = self.weight_Variable([3,3,64,64]) #64个卷积核（3，3，64）
        b3 = self.bias_Variable([64]) #64个偏置项
        conv3 = tf.nn.relu(self.conv2d(pool2, w3) + b3) #池化层，输出（12，12，64）
        pool3 = self.max_pool_2x2(conv3) #池化层，输出（5，5，64）

        # 全链接层
        w_fcl1 = self.weight_Variable([8*8*64,512])  # 512个节点
        b_fcl1 = self.weight_Variable([512])
        pool3_flat = tf.reshape(pool3,[-1,8*8*64]) #转换为[1,8*8*64]的形状
        fcl1 = tf.nn.relu(tf.matmul(pool3_flat, w_fcl1) + b_fcl1)

        # dropout层
        drop1 = self.dropout(fcl1,self.keep_prob_7)

        # softmax输出层
        w_out = self.weight_Variable([512, self.outnode])
        b_out = self.bias_Variable([self.outnode])
        y_out = tf.add(tf.matmul(drop1, w_out),b_out,name='out_data')
        return y_out

    def cnnTrain(self,maxiter=1000,acc_threshold=0.98,batch_size=100):
        '''
        训练模型
        :param maxiter: 迭代次数
        :param accu: 精度阈值
        :param batch_size: 批量样本数
        :return: 保存模型
        '''
        y_out=self.cnnLayer()
        cross_entropy = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=y_out,labels=self.y_))  # 定义损失函数
        train_step=tf.train.AdadeltaOptimizer(1e-4).minimize(cross_entropy)#优化器
        # train_step = tf.train.GradientDescentOptimizer(0.15).minimize(cross_entropy)

        accuracy_step = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y_out, axis=1), tf.argmax(self.y_, axis=1)), tf.float32))  # 获得精度，输出和实际值比较
        '''
        tf.reduce_mean返回平均值，数据类型保持不变
        tf.cast返回dtype类型，即tf.float32
        tf.equal返回bool类型
        '''
        saver=tf.train.Saver() #初始化存储器
        sess = tf.Session()  # 构建会话
        sess.run(tf.global_variables_initializer())  # 变量初始化
        for i in range(maxiter):
            img_index= random.sample(range(len(self.xdata)),batch_size) #获得随机样本的index，数组
            batch_x=self.xdata[img_index]
            batch_y=self.labels[img_index]
            sess.run(train_step, feed_dict={self.x: batch_x, self.y_: batch_y}) #训练模型
            if i % 10 == 0: #间隔输出训练精度
                acc = sess.run(accuracy_step, feed_dict={self.x:batch_x, self.y_:batch_y})
                print('轮数:%d 训练精度:%f'%(i,acc))  # 打印输出，i为训练轮次
                if acc > acc_threshold and i > 500 :
                    saver.save(sess,self.modelfile)
        sess.close()

    def predict(self,test_x=test_x):
        '''
        预测函数，调用模型进行预测
        :param test_x: 测试数据
        :return: 返回样本预测类别和概率
        pre:样本属于各类别的概率，比如[0.1,0.2,0.8,0.5]
        pre_num:样本预测类别
        '''
        y_out=self.cnnLayer()
        with tf.Session() as sess:
            saver=tf.train.Saver() #初始化存储器
            saver.restore(sess,self.modelfile) #调用模型
            graph=tf.get_default_graph() #获得计算图
            test_data=graph.get_tensor_by_name('x_data:0')
            pre=sess.run(y_out,feed_dict={test_data:test_x})
            pre_num=np.argmax(pre,1)
        return pre_num,pre

if __name__ == '__main__':
    cnn_net=CnnNet()
    cnn_net.cnnTrain()#训练模型
    # pre_num,pre=cnn_net.predict()
    # test_acc=sum(tf.equal(pre_num, test_y)) / len(test_y)#测试精度
    # print(test_acc)