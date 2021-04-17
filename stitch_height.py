import os
import cv2
import shutil
import numpy as np

n_start = 36 
n_end =  0
e_start = 64
e_end = 69 #116
path = "X:/library/texture/earth/zoom.earth/height_30SRTM"
save_path = "X:/library/texture/earth/zoom.earth"

for i in range(n_start,(n_end-1),-1):
    N = str(i).zfill(2)
    horImgs = None

    for j in range(e_start,e_end + 1):
        E = str(j).zfill(3)
        coordinates = "N{0}E{1}".format(str(N),E)
        file_name = coordinates + ".jpg"
        print(file_name)
        if j == e_start:
            horImgs = cv2.imread(path + "\\" + file_name)
        else:
            newImg = cv2.imread(path + "\\" + file_name)
            addImg = np.concatenate((horImgs, newImg), axis=1)
            horImgs = addImg

#         # break
    break
print("goin to break")
na = save_path + "/" + "z_stitch.jpg"
print(na)
cv2.imwrite(na, horImgs)
print(horImgs)
    # print("wrote image file")