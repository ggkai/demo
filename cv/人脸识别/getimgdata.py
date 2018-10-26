import os
import re
import cv2
import numpy as np

class GetImgData:
    '''
    将图片数据处理成ndarray数据
    '''
    def __init__(self,dir='./data/small_img_gray'):
        self.dir=dir # 该文件夹中有多个子文件夹，每个子文件夹名为一个人名，里面是这个人的多张人脸照片

    def get_file_path(self,path=None):
        '''
        获得文件中的所有图片路径
        :param path: 文件路径
        :return: 返回图片路径
        '''
        filepaths = []
        filenames = os.listdir(path)  # 获取path中的所有文件名
        for filename in filenames:
            if re.findall('\d+\.jpg',filename)!=[]:
                filepath=os.path.join(path,filename) #获得文件路径
                filepaths.append(filepath) #添加到数组
        return filepaths

    def get_onehot(self,index):
        '''
        传入文件数组，返回文件分类的onehot编码
        :param filenames: 文件数组
        :return: onehot编码数组
        '''
        num=len(index)
        onehot = np.zeros([num,num])  # 构建全零数组，行数为数字个数，列为数字最大值加一
        onehot[np.arange(num), np.arange(num)] = 1         # 利用数组的索引方式进行赋值，构建onehot编码
        return onehot

    def get_file_label(self):
        '''
        获得self.dir中每个文件路径、onehot编码、数字标签
        :return: 返回两个值
        path_onehot: 返回list，文件路径和onehot编码，比如('./data/small_img_gray/hebo',[1,0,0,0,0])
        num_label: 返回字典，key:数字标签，values:文件名，比如{0:'hebo',1:'hexianbin'}
        '''
        file_index=[] #[0,1,2,3,4,5,...]
        file_name=[] #[hebo,hexianbin,...]
        path_list=[] #['./data/hebo,'./data/hexianbin',...]
        for index,item in enumerate(os.listdir(self.dir)):
            file_index.append(index)
            file_name.append(item)
            path_list.append(os.path.join(self.dir,item))
        filepath_onehot=list(zip(path_list,self.get_onehot(file_index)))
        num_label=dict(zip(file_index,file_name))
        return filepath_onehot,num_label

    def read_img(self):
        '''
        读取self.dir中所有图片，将图片转为数组，获得图片标签
        :return: 返回三个值
        x: 返回数组，图片像素数据
        y: 返回list，图片标签onehot编码，比如(0,1,0,0,...)
        num_label: 返回字典，图片数字标签和文件名，比如{0:'hebo',1:'hexianbin',...}
        '''
        imgs = [] #图片数组
        labels = [] #图片标签[...]

        filepath_onehot,num_label=self.get_file_label()
        for filepath,onehot in filepath_onehot:
            for imgpath in self.get_file_path(filepath):
                img=cv2.imread(imgpath,cv2.IMREAD_GRAYSCALE)
                imgs.append(img)
                labels.append(onehot)
        x=np.array(imgs,dtype='float32')/255
        y=np.array(labels,dtype='float32')
        return x,y,num_label

if __name__ == '__main__':
    imgData = GetImgData()
    x,y,name = imgData.read_img()
    print(x.shape,y.shape,name)