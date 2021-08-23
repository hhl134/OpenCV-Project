import cv2
# 打开摄像头，0为电脑默认摄像头，直接写文件名可以打开本地视频
cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 640)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # ret的True和False反映是否捕捉成功，frame返回画面
    ret, frame=cap.read()
    if not ret:
        print("无法获取画面帧")
        exit()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame_window', gray)
    # 如果按下q键，就跳出循环
    if cv2.waitKey(1) == ord('q'):
        break
# 关闭摄像头
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()
