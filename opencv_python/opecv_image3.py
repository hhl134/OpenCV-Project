import cv2

# 8 运用级联分类器，识别脸部
# 级联方法不是最准确的，但较快
# 加上了摄像头

# faceCascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")
# img = cv2.imread("Sources/lena.png")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
# cv2.imshow("Result", img)
# cv2.waitKey(0)

faceCascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 640)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # ret的True和False反映是否捕捉成功，frame返回画面
    ret, frame = cap.read()
    if not ret:
        print("无法获取画面帧")
        exit()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('frame_window', frame)
    # 如果按下q键，就跳出循环
    if cv2.waitKey(1) == ord('q'):
        break
# 关闭摄像头
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()
