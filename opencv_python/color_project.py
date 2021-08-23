# 7月23日 未完成 将color_picker的参数移过来无效，还有捕捉轮廓的程序未完成
import cv2
import numpy as np

# 21 179 121 255 63 255 red
# 16 75 96 255 71 255 yellow
# 58 179 69 255 28 255 blue
my_Colors = [[21, 179, 121, 255, 63, 255],
             [16, 75, 96, 255, 71, 255],
             [58, 179, 69, 255, 28, 255]]
myColorValues = [[0, 0, 255],  ## BGR
                 [255, 0, 255],
                 [255, 0, 0]]
myPoints = []  ## [x , y , colorId ]


def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return newPoints


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


# 打开摄像头，0为电脑默认摄像头，直接写文件名可以打开本地视频
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # ret的True和False反映是否捕捉成功，frame返回画面
    ret, img = cap.read()
    if not ret:
        print("无法获取画面帧")
        exit()
    imgResult = img.copy()
    newPoints = findColor(img, my_Colors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow('frame_window', imgResult)

    # 如果按下q键，就跳出循环
    if cv2.waitKey(1) == ord('q'):
        break
# 关闭摄像头
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()
