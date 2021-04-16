import requests
import cv2
import numpy as np
import os
# from input_data import SAVE_DIR, X1, X2, Y1, Y2

base_url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/11/"
# save_dir = SAVE_DIR

# co-ordinates
# x1, y1 = X1, Y1
# x2, y2 = X2, Y2

# xdist = x2 - x1
# ydist = y2 - y1

class GetEarth():

    def __init__(self, p1, p2, dir):
        self.p1 = p1
        self.p2 = p2
        self.dir = dir

        self.x1, self.y1 = self.p1
        self.x2, self.y2 = self.p2

        # distance
        self.xdist = self.x2 - self.x1
        self.ydist = self.y2 - self.y1

        # name for the directory to save image
        self.dir_name = str(self.x1) + "_" + str(self.y1)  + "_" +str(self.x2)+ "_" + str(self.y2) 

        # check if the directory exists if not create new
        self.directory_path = os.path.join(self.dir,self.dir_name )
        if not os.path.isdir(self.directory_path):
            os.mkdir(self.directory_path) 

        # self.x2 = self.x2 + 1
        # self.y2 = self.y2 + 1

    # fetch images
    def fetch_images(self):
        for i in range(self.xdist):
            for j in range(self.ydist):
                url = base_url + str(self.x1 + i) + "/" + str(self.y1 + j)
                file_name = str(self.x1 + i) + "_" + str(self.y1 + j) + ".png"

                # request
                response = requests.get(url)

                # save file
                file = open(os.path.join(self.directory_path, file_name), "wb") 
                file.write(response.content)
                print("Saved Image Tile:" + file_name)
                file.close()



    # stitch images
    def stitch_images(self):
        for i in range(self.xdist):
            horImgs = None
            for j in range(self.ydist):
                file_name = str(self.x1 + i) + "_" + str(self.y1 + j) + ".png"
                if j == 0:
                    horImgs = cv2.imread(self.directory_path +"\\" + file_name)
                else:
                    newImg = cv2.imread(self.directory_path +"\\" + file_name)
                    # print(self.directory_path +"\\" +  file_name)
                    addImg = np.concatenate((horImgs, newImg),axis=1)
                    horImgs = addImg
            # vertical stitches
            if i == 0:
                newVImg = horImgs
                # break
            else:
                addVImg = np.concatenate((newVImg, horImgs),axis=0)
                newVImg = addVImg

            print("Verticle Distance:" + str(self.x1 + i))

        # write image
        img_file_name =  str(self.x1) + "_" + str(self.y1) +"_"+ str(self.x2) + "_" + str(self.y2) +"_stitched.jpg"
        cv2.imwrite((self.directory_path +"\\" +img_file_name),newVImg)
        print("Image File written: " + img_file_name)

