# ssd object detector
# nms 消除重叠 non-maximum suppression
import cv2
import numpy as np

Thres = 0.5
nms_threshold = 0.2
# img = cv2.imread("lena.png")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
# print(classNames)

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    Ret, img = cap.read()
    classIDs, confs, bbox = net.detect(img, confThreshold = Thres)
    bbox = list(bbox)
    # reshape??
    confs = list(np.array(confs.reshape(1, -1)[0]))
    confs = list(map(float, confs))
    indices = cv2.dnn.NMSBoxes(bbox, confs, Thres, nms_threshold)
    print(indices)

    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x + w, y + h), color = (0, 255, 0), thickness = 2)
        cv2.putText(img, classNames[classIDs[i][0]-1].upper(), (box[0] + 10, box[1] + 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    # # print(classIDs, confs,bbox)
    # if len(classIDs) != 0:
    #     for classID, confidence, box in zip(classIDs.flatten(), confs.flatten(), bbox):
    #         cv2.rectangle(img, box, color = (0, 255, 0), thickness = 2)
    #         cv2.putText(img, classNames[classID - 1].upper(), (box[0] + 10, box[1] + 30),
    #                     cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    #         cv2.putText(img, str(round(confidence, 2)), (box[0] + 50, box[1] + 30),
    #                     cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
