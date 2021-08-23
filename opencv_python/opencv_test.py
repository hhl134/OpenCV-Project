import cv2
# opencv-4.5.3
print(cv2.__version__)
img = cv2.imread("Sources/lena.tif")

if img is None:
    print("没有读取图片")

cv2.imshow("Display Window", img)
# 0为无限延迟，数值1代表1ms
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("Sources/save_img.tif", img)

cv2.destroyAllWindows()