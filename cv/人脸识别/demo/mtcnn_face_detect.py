from mtcnn.mtcnn import MTCNN
import cv2
image = cv2.imread("./faceImg/biyezhao.jpg")
detector = MTCNN()
results=detector.detect_faces(image)
for result in results:
    bounding_box = result['box']#左上角xy，宽高
    keypoints = result['keypoints']
    cv2.rectangle(image,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0,155,255),
              2)
    cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)#图片、坐标、半径、线条颜色、线条宽度
    cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
    cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)
cv2.imwrite("./faceImg/biyezhao-new.jpg", image)
print(result)