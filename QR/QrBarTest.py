import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread("QR1.jpg")
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    Ret,img=cap.read()
    code = decode(img)
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        # 这里使用polylines而不使用rectangle
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]-10),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
# 关闭摄像头
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()