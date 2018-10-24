#图片人脸检测
import cv2
imagePath='./faceImg/1.png'
haarcascadePath='/anaconda/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_alt.xml'
faceCascade=cv2.CascadeClassifier(haarcascadePath)#创建haar分类器对象
image=cv2.imread(imagePath)#读取图片
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#转换灰度图片
faces=faceCascade.detectMultiScale(gray,scaleFactor=1.15,minNeighbors=5,minSize=(5,5),flags=cv2.CASCADE_SCALE_IMAGE) #人脸目标检测
#scaleFactor尺寸变换1.15倍
#minNeighbors人脸附近检测次数
#minSize最小人脸尺寸大小
#CASCADE_DO_CANNY_PRUNING=1, 利用canny边缘检测来排除一些边缘很少或者很多的图像区域
#CASCADE_SCALE_IMAGE=2, 正常比例检测
#CASCADE_FIND_BIGGEST_OBJECT=4, 只检测最大的物体
#CASCADE_DO_ROUGH_SEARCH=8 初略的检测
print('{}张人脸'.format(len(faces)))
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)
    '''
    第一个参数：img是原图
    第二个参数：（x，y）是矩阵的左上点坐标
    第三个参数：（x+w，y+h）是矩阵的右下点坐标
    第四个参数：（0,255,0）是画线对应的rgb颜色
    第五个参数：2是所画的线的宽度
    '''
cv2.imshow('face box',image)
cv2.waitKey(0)#等待用户操作,0代表是永远
cv2.destroyAllWindows()