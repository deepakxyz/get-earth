import cv2
import numpy as np

# img1 = cv2.imread("../images/968_1477.png")
# img2 = cv2.imread("../images/968_1478.png")
# img3 = cv2.imread("../images/968_1479.png")
# print(img1.shape)

# # horizontal stack
# # hor = np.hstack((img1,img2,img3))
# hor = np.concatenate((img1,img2),axis=1)
# hor2 = np.concatenate((hor,img3),axis=1)
# cv2.imshow('Hor',hor2)

# cv2.waitKey(0)


n_start = 36 
n_end =  0
e_start = 64
e_end = 116

# for i in range(n_start,(n_end-1),-1):
#     n = i
#     horimgs = None
#     for j in range(e_start, e_end + 1):
#         e = str(j).zfill(3)
#         coordinates = "N{0}E{1}".format(str(n),e)
#         file_name = coordinates + ".jpg"
#         if j == e_start:
#             print(file_name)
#             # horimgs = cv2.imread(path + "\\" + file_name)
#         else:
#             print(file_name)
#             # newimg = cv2.imread(path + "\\" + file_name)
#             # addimg = np.concatenate((horimgs, newimg),axis=1)
#             # horimgs = addimg
#         break

# cv2.imwrite(h + "\\" + "stitch.jpg", horImgs)
# print("Image written")


for i in range(n_start,(n_end-1),-1):
    n = i
    for j in range(e_start,e_end + 1):
        print(i,j)
        # break
    break