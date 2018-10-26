# 导入库
import os
import cv2
import time
from mtcnn.mtcnn import MTCNN
from getimgdata import  GetImgData
getimg=GetImgData() #获取图片类实例化

class CaptureFace:
    def __init__(self,imgdir='./data/capture_img/',gray_imgdir='./data/capture_gray_img'):
        '''
        :param imgdir: 拍照图片路径
        :param gray_imgdir: 灰色图片路径
        '''
        self.imgdir=imgdir
        self.gray_imgdir=gray_imgdir

    def captureface(self,someone='Default',picturenum=10,waitkey=300):
        '''
        通过摄像头拍照
        :param someone: 人名，并以此人名命名文件名
        :param picturenum: 拍照数量
        :param waitkey: 延迟毫秒
        :return: 保存拍摄的图片
        '''
        if not os.path.exists(self.imgdir): #创建多级目录
            os.mkdir(self.imgdir)
        filepath=os.path.join(self.imgdir,someone)
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        capture=cv2.VideoCapture(0)
        time.sleep(1) # 间断1秒，相机准备，解决拍到全黑照片的问题
        for i in range(picturenum):
            ret,frame=capture.read()
            cv2.imshow(someone,frame)#显示图片
            cv2.imwrite(filepath+'/'+str(i)+'.jpg',frame)#将图片写入指定路径
            if cv2.waitKey(waitkey)==ord('q'):#
                break
        capture.release()#释放摄像头
        cv2.destroyAllWindows()#关闭窗口
        print('Successfully captured photos')

    def facetogray(self,someone='Default',size=64,waitkey=300):
        '''
        人脸检测，转换为灰度图
        :param someone: 人名，并以此人名命名文件名
        :param size: 图片尺寸
        :param waitkey: 延迟毫秒
        :return: 保存灰度图片
        '''
        detector = MTCNN()
        imgpath=getimg.get_file_path(path=os.path.join(self.imgdir,someone))#获得所有图片路径
        if not os.path.exists(self.gray_imgdir):
            os.mkdir(self.gray_imgdir)
        newpath=os.path.join(self.gray_imgdir,someone)
        if not os.path.exists(newpath):
            os.mkdir(newpath) #新建保存灰度图片的文件夹
        for i in range(len(imgpath)):#迭代所有图片
            img=cv2.imread(imgpath[i])
            results=detector.detect_faces(img) #对每一张图片进行人脸检测，支持多个人脸
            for result in results: #迭代每一个人脸
                if result is not None:  # 检测不到人脸返回None
                    face_box = result['box']#人脸位置信息，左上角x、左上角y、宽、高
                    face=img[face_box[1]:face_box[1]+face_box[3],face_box[0]:face_box[0]+face_box[2]]#截取人脸上下范围（y+高），左右范围（x+宽）
                    face_gray=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)#转换为灰度图
                    print(face_gray)
                    cv2.imshow(someone,face_gray)
                    cv2.imwrite(newpath+'/'+str(i)+'.jpg',face_gray)
                    if cv2.waitKey(waitkey) == ord('q'):
                        break
        cv2.destroyAllWindows()  #关闭显示窗口
        print('Successfully convert into gray photos')

if __name__ == '__main__':
    picture=CaptureFace()
    picture.captureface()
    picture.facetogray()