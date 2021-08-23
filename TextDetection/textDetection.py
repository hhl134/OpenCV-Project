import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "F:\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("Num3.jpg")
img = cv2.resize(img, (640, 480))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_boxes(img))

# detecting characters
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (255, 0, 0), 2)
    cv2.putText(img, b[0], (x, hImg - y + 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (50, 50, 255), 2)

# # detecting words
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_data(img)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b)==12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x, y), (w+x, h+y), (255, 0, 0), 2)
#             cv2.putText(img, b[11], (x, y + 10), cv2.FONT_HERSHEY_SIMPLEX,
#                         0.5, (50, 50, 255), 2)

# # detecting numbers
# hImg, wImg, _ = img.shape
# cfg = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img, config = cfg)
# for x, b in enumerate(boxes.splitlines()):
#     if x != 0:
#         b = b.split()
#         print(b)
#         if len(b) == 12:
#             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#             cv2.rectangle(img, (x, y), (w + x, h + y), (255, 0, 0), 2)
#             cv2.putText(img, b[11], (x, y + 10), cv2.FONT_HERSHEY_SIMPLEX,
#                         0.5, (50, 50, 255), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
