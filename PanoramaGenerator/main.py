import cv2
import os

mainFolder='Image'
myFolders=os.listdir(mainFolder)

for folder in myFolders:
    path=mainFolder +'/'+folder
    images=[]
    myList=os.listdir(path)
    print(f'Total no of images detected {len(myList)}')
    for imgN in myList:
        curImg=cv2.imread(f'{path}/{imgN}')
        curImg=cv2.resize(curImg,(0,0),None,0.2,0.2)
        cv2.imshow(folder+imgN,curImg)
        images.append(curImg)

    stitcher=cv2.Stitcher.create()
    (status,result)=stitcher.stitch(images)
    if status==cv2.STITCHER_OK:
        print("Panorama Generated")
        cv2.imshow(folder,result)
    else:
        print("Panorama Generation unsuccessful")
cv2.waitKey(0)