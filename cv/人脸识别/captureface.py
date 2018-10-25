# 导入库
import numpy as np
import os
import cv2
import time
from mtcnn.mtcnn import MTCNN


#通过摄像头拍照
def captureface(imgdir,someone=None,picturenum=10,waitkey=300):
    filepath=os.path.join(imgdir,someone)
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    capture=cv2.VideoCapture(0)
    for i in range(picturenum):
        ret,frame=capture.read()
        cv2.imshow(someone,frame)#显示图片
        cv2.imwrite(imgdir+str(i)+'.png',frame)#将图片写入指定路径
        if cv2.waitKey(1000)==ord('q'):#
            break
    capture.release()#释放摄像头
    cv2.destroyAllWindows()#关闭窗口

#人脸检测，转换为灰度图
def facetogray(facegraydir,imgdir,someone='default',size=64,waitkey=100):
    detector = MTCNN()
    a,b=get_file_name(imgdir)#获得所有图片
    n=len(b)
    newpath=os.path.join(facegraydir,someone)
    if not os.path.exits(newpath):
        os.mkdir(newpath)
    for i in range(n):#迭代所有图片
        img=cv2.imread(b[i])
        results=detector.detect_faces(img)
        if result is not None:
            for result in results:
                bounding_box = result['box']#人脸位置信息，左上角xy，宽高
                face=img[box[1]:box[1]+box[3],box[0]:box[0]+box[2]]#截取人脸高范围，宽范围
                face_gray=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)#转换为灰度图
                cv2.imshow('image',face_gray)
                cv2.imwrite(newpath+'/'+str(i)+'.png',face_gray)
    cv2.destroyAllWindows()  #关闭显示窗口