import requests
import cv2
import numpy as np

base_url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/11/"
save_dir = "Z:/Piper/get-earth/images/"

# co-ordinates
x1, y1 = 1, 1
x2, y2 = 5, 5

xdist = x2 - x1
ydist = y2 - y1

# get the images
for i in range(xdist):
    for j in range(ydist):
        url = base_url + str(x1 + i) + "/" + str(y1 + j)
        file_name = str(x1 + i) + "_" + str(y1 + j) + ".png"

        # request
        response = requests.get(url)

        # save file
        file = open(save_dir + file_name, "wb")
        file.write(response.content)
        print("Saved Image Tile: " + file_name)
        file.close()


# stich the images

for i in range(xdist):
    horImgs = None
    # horizontal stitches
    for j in range(ydist):
        if j == 0:
            horImgs = cv2.imread(save_dir + file_name)
        
        else:
            newImg = cv2.imread(save_dir + file_name)
            addImg = np.concatenate((horImgs, newImg),axis=1)
            horImgs = addImg

    # vertical stitches
    if i == 0:
        newVImg = horImgs
    else:
        addVImg = np.concatenate((newVImg, horImgs),axis=0)
        newVImg = addVImg

# write image
cv2.imwrite((save_dir + "stitched.jpg"),newVImg)