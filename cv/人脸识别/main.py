from cnn_net import CnnNet
import numpy as np
import cv2
from getimgdata import GetImgData
from mtcnn.mtcnn import MTCNN

# 调用mtcnn人脸检测器
detector=MTCNN()

# 读取数据
imgs,labels,num_name=GetImgData().read_img()

def main(size=64,threshold=0.98,waitkey=1000):
    capture = cv2.VideoCapture(0)             #调用电脑的摄像头
    while True:
        res,img = capture.read()                #获取图片
        results = detector.detect_faces(img)    #人脸检测
        if results is not None:
            for result in results:
                face_box = result['box']  # 人脸位置信息，左上角x、左上角y、宽、高
                face = img[face_box[1]:face_box[1] + face_box[3],face_box[0]:face_box[0] + face_box[2]]  # 截取人脸上下范围（y+高），左右范围（x+宽）
                face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
                face_data = cv2.resize(face_gray,(size,size)).reshape([1,size,size,1])
                cnnnet=CnnNet()
                pre_num, pre=cnnnet.predict(test_x=face_data)
                if np.max(pre) < threshold:
                    name='unknowm'
                else:
                    name=num_name[pre_num[0]]
                print('这是谁? %s' % name)
                cv2.putText(img=img, text=name, org=(int(face_box[0]), int(face_box[1]) - 20), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=1, color=(255), thickness=2)
                cv2.rectangle(img, (face_box[0],face_box[1]), (face_box[0]+face_box[2],face_box[1]+face_box[3]), (255, 0, 0), 3)  # 将x,宽，高，face显示出来
                cv2.imshow('image', img)
        if cv2.waitKey(waitkey) == ord('q'):  # 在每次迭代中延迟waitkey毫秒，按"q"键可退出拍照
                break
    capture.release()        #释放摄像头
    cv2.destroyAllWindows()  #关闭显示窗口

if __name__ == '__main__':
    main()
