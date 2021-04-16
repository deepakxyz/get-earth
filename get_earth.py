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

    def fetch_image(self):
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

    def stitch_images(self):
        for i in range(self.xdist):

            # horizontal stitches
            horizontal_images = None
            for j in range(self.ydist):
                # file name
                file_name = str(self.x1 + i) + "_" + str(self.y1 + j) + ".png"
                file_full_path = os.path.join(self.directory_path, file_name)
                if j == 0:
                    horizontal_images = cv2.imread(file_full_path)
                
                else:
                    new_hort_image = cv2.imread(file_full_path)
                    add_new_image = np.concatenate((horizontal_images, new_hort_image), axis=1)
                    horizontal_images = add_new_image
            
            # vertical stitches
            if i == 0:
                new_vert_image = horizontal_images
            
            else:
                add_new_vert_img = np.concatenate((new_vert_image, horizontal_images),axis=0)
                new_vert_img = add_new_vert_img

        # write image
        stitch_file_name = str(self.x1) + "_" + str(self.y1)  + "_" +str(self.x2)+ "_" + str(self.y2) + "_" + "stitched.jpg"
        # print(self.directory_path + "/"+ stitch_file_name)
        cv2.imwrite((self.directory_path +"/"+ stitch_file_name), new_vert_image)

