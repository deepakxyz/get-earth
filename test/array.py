import numpy as np
import requests
import cv2

base_url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/11/"


x1, y1 = 968,1477
x2, y2 = 971,1480

xdist = x2 - x1
ydist = y2 - y1

# for i in range(xdist):
#     for j in range(ydist):
#         print(x1 + i, y1 + j)
#         url = base_url + str(x1 + i) + "/" + str(y1 + j)
#         file_name = str(x1 + i ) + "_" + str(y1 + j) + ".png"
        # print(file_name)
        # request
        # response = requests.get(url)
        
        # save file
        # file = open("Z:/Piper/get-earth/images/"+file_name, "wb")
        # file.write(response.content)
        # file.close()


for i in range(xdist):
    horImgs = None
    for j in range(ydist):
        file_name = str(x1+i) + "_" +str(y1 + j) + ".png"
        # print(file_name)
        # read the first image
        if j == 0:
            horImgs = cv2.imread("../images/" + file_name)
        
        else:
            newImg = cv2.imread("../images/" + file_name) 
            addImg = np.concatenate((horImgs,newImg),axis=1)
            horImgs = addImg


    # break
    # first vertical loop
    if i == 0:
        newVImg = horImgs
    else:
        # newVImg = horImgs
        addVImg = np.concatenate((newVImg,horImgs),axis=0)
        newVImg = addVImg

    # show image
    # cv2.imshow('Hor',newVImg)
    # cv2.waitKey(0)

    # write image
cv2.imwrite("stitched.jpg",newVImg)