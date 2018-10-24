# 获取照片数据
import cv2
import time
import os

capture=cv2.VideoCapture(0)

img_path='./data/'
if not os.path.exists(img_path):
    os.mkdir(img_path)
i=1
while(True):
    #cv2.waitKey(1000)#等待键盘输入，500ms
    ret,frame=capture.read()
    cv2.imshow('guokai',frame)
    cv2.imwrite(img_path+str(i)+'.png',frame)
    i=i+1
    if cv2.waitKey(1000)==ord('q'):
        break
capture.release()#释放摄像头
cv2.destroyAllWindows()#关闭窗口