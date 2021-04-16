import cv2
import numpy as np

img1 = cv2.imread("../images/968_1477.png")
img2 = cv2.imread("../images/968_1478.png")
img3 = cv2.imread("../images/968_1479.png")
print(img1.shape)

# horizontal stack
# hor = np.hstack((img1,img2,img3))
hor = np.concatenate((img1,img2),axis=1)
hor2 = np.concatenate((hor,img3),axis=1)
cv2.imshow('Hor',hor2)

cv2.waitKey(0)