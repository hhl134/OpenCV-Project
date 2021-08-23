import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# img = cv2.imread("Sources/lena.tif")

# # 1 灰度化、模糊、Canny算子、膨胀、腐蚀
# # 算子：5*5的uint8类型单位矩阵
# kernel = np.ones((5, 5), np.uint8)
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# imgCanny = cv2.Canny(img, 100, 100)
# # 膨胀
# imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# # 腐蚀
# imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
#
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dilation Image", imgDilation)
# cv2.imshow("Eroded Image", imgEroded)

# # 2 裁剪
# # shape返回的是y*x
# print(img.shape)
# imgResize = cv2.resize(img, (300, 200))
# imgCropped = img[0:200, 200:500]
#
# cv2.imshow("Resize Image", imgResize)
# cv2.imshow("Cropped Image", imgCropped)

# # 3 创建数字矩阵并添加颜色、画线、长方形、圆、写字
# img = np.zeros((512, 512, 3), np.uint8)
# # # BGR
# # img[200:300, 100:200] = 0, 0, 255
# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# cv2.rectangle(img, (0, 0), (200, 300), (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (300, 400), 100, (255, 255, 0), 5)
# cv2.putText(img, "OPENCV", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 1)
# cv2.imshow("Image", img)

# # 4 透视变换
# img = cv2.imread("Sources/cards.jpg")
# width, height = 250, 350
# pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
#
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgOutput = cv2.warpPerspective(img, matrix,(width, height))
# cv2.imshow("Image", img)
# cv2.imshow("Output", imgOutput)

# # 5 图像堆栈
# img = cv2.imread("Sources/lena.png")
# imgHor = np.hstack((img, img))
# imgVer = np.vstack((img, img))
# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vertical", imgVer)


# 6 使用滑动条改变图片的HSV，并使用图像堆叠放一起
def empty():
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread("Sources/lambo.PNG")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow("Image", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("MASK", mask)
    cv2.imshow("Result", imgResult)

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)
    cv2.waitKey(1)
