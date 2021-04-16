import numpy as np
import cv2


image1_url = r"X:\library\texture\earth\zoom.earth\835_1416_885_1516\835_1416_886_1517_stitched.jpg"
image2_url = r"X:\library\texture\earth\zoom.earth\885_1416_935_1516\885_1416_935_1516_stitched.jpg"

img1 = cv2.imread(image1_url)
img2 = cv2.imread(image2_url)

addImg = np.concatenate((img1,img2),axis=0)
cv2.imwrite(("X:/library/texture/earth/zoom.earth/udim1/1001.jpg"),addImg)