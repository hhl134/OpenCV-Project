import cv2

#############
nPlateCascade = cv2.CascadeClassifier("Files/haarcascade_russian_plate_number.xml")
minArea = 500
count = 1
#############
cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 640)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # ret的True和False反映是否捕捉成功，frame返回画面
    ret, img = cap.read()
    if not ret:
        print("无法获取画面帧")
        exit()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow('ROI', imgRoi)

    cv2.imshow('frame_window', img)

    # 如果按下q键，就跳出循环
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Scanned/Noplate_" + str(count) + ".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1
# 关闭摄像头
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()
