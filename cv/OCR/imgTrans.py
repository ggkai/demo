#导入包
import cv2
import os,re
import numpy as np

# 读图片文件

#方式一：listdir的参数是文件夹的路径，filename是文件夹中文件的名称
# for filename in os.listdir('./OCR_data/trainImages/'):
#     print (filename)

#方式二
class ImgTrans:
    def __init__(self,path='./OCR_data/trainImages/'):
        self.path=path

    def getImgName(self):
        filenames = os.listdir(self.path)
        imgnames = []
        for i in filenames:
            #print(re.findall('^\d_\d+\.png$',i))
            #判断是否为空，匹配不上的是空数组
            if re.findall('^\d_\d+\.png$',i)!=[]:
                imgnames.append(i)
        return imgnames
    def getImgData(self,shape=(28,28)):
        imgnames=self.getImgName()
        n=len(imgnames)
        M,N=shape
        #data维度[120,28*28=784],labels维度[120]
        data=np.zeros([n,M*N],dtype='float32')
        labels=np.zeros([n],dtype='float32')
        #处理数据尺寸
        for i in range(n):
            #获取图片
            img=cv2.imread(self.path+imgnames[i])
            #尺寸为28*28*3
            img_resize=cv2.resize(img,shape)
            #尺寸为28*28，max-min归一化
            img_gray=img_resize[:,:,0]/255
            #reshape[1,784]即1行784列，等同于img_gray.reshape(784)
            data[i,:]=np.reshape(img_gray,[M*N])
            #获取第一个字母为标签,float类型
            labels[i]=imgnames[i][0]
        return data,labels