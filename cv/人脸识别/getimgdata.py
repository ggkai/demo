import os
import re
import cv2
import numpy as np


class GetImgData:
    '''
    将图片数据处理成ndarray数据
    '''
    # 初始化函数
    def __init__(self,dir='.data/small_img_gray'):
        self.dir=dir # 该文件夹中有多个子文件夹，每个子文件夹名为一个人名，里面是这个人的多张人脸照片

    # 第一步：传入路径，返回文件路径数组、文件数组
    def get_file_name(path=None):
        filepaths = []
        filenames = os.listdir(path)  # 获取path中的所有文件名
        for filename in filenames:
            if filename=='.DS_Store':
                os.remove(path+'/'+filename) #去掉.DS_Store文件
            filepath=os.path.join(path,filename) #获得文件路径
            filepaths.append(filepath)
        return filepaths,filenames


    # 第二步：传入文件数组，返回文件分类的onehot编码
    def get_onehot(filenames):
        onehot = np.zeros([len(filenames), len(filenames) ])  # 构建全零数组，行数为数字个数，列为数字最大值加一
        onehot[np.arange(len(filenames)), np.arange(len(filenames))] = 1         # 利用数组的索引方式进行赋值，构建onehot编码
        return onehot


    # 第三步：传入文件数组，返回分类名、分类标签
    '''
    def get_file_label(filenames):
        label_index=[]
        label_name=[]
        for index,item in enumerate(filenames):
            label_index.append(index)
            label_name.append(item)
        print(label_index,label_name)
    '''
    def get_file_label(filenames):
        return np.arange(len(filenames))


    # 第四步：传入路径，返回文件下图片路径、onehot编码、分类标签
    # def get_img_onehot_label(path):
    # #     dir_labels=list(zip(pathlist,b.tolist())) #人名路径：分类的独热编码
    # #     number_name=dict(zip(indexlist,namelist)) #数字标签：分类

    #     imgs = []     #图片像素数据
    #     labels = []   #图片标签
    #     for dirname,label in dir_labels:            #获得人名路径：分类独热编码
    #         print(dirname,label)
    #         for imgname in os.listdir(dirname):      #获得人名路径下的所有图片
    #             print(imgname)
    #             img = cv2.imread(dirname+'/'+imgname,cv2.IMREAD_GRAYSCALE)  #读取图片(灰度图)
    #             imgs.append(img)                  #存贮图片像素数据
    #             labels.append(label)              #存贮图片标签数据
    #             x = np.array(imgs,dtype='float32')/255    #将图片像素数据转为数组并归一化
    #              = np.array(labels,dtype='float32')      #将标签数据转为数组
    #             print(x,y,labels_name)
    def readimg(path):
        imgs = []
        onehots = []
        labels = []

        filepaths, filenames = get_file_name(path)
        label = get_file_label(filenames)
        onehot = get_onehot(filenames)

        i = 0
        for filepath in filepaths:  # 获得路径
            imgpaths, imgnames = get_file_name(filepath)  # 获得图片
            for imgpath in imgpaths:
                img = cv2.imread(imgpath)
                imgs.append(img)
                onehots.append(onehot[i])
                labels.append(label[i])
            i += 1
        x = np.array(imgs, dtype='float32') / 255
        y = np.array(labels, dtype='float32')
        return x, y, labels