import requests
import os
import cv2
import shutil

# From N36E064 to N00E116

N_start = 36 
N_end =  0
E_start = 64
E_end = 116



# for j in range(N_start,N_end-1,-1):
#     N = j
#     for i in range(E_start, E_end+1):
#         E = str(i).zfill(3)
#         coordinates = "N{0}E{1}".format(str(N), E)
#         # Horizontal stitching
#         base_url = f"https://e4ftl01.cr.usgs.gov/MEASURES/SRTMGL1.003/2000.02.11/{coordinates}.SRTMGL1.2.jpg"
#         print(base_url)
#     break

class GetEarthHeight():

    def __init__(self,N_start,N_end,E_start,E_end, path):
        self.N_start = N_start
        self.N_end = N_end
        self.E_start = E_start
        self.E_end = E_end
        self.path = path


    def fetch_images(self):
        for j in range(self.N_start,(N_end-1),-1):
            N = str(j).zfill(2)
            for i in range(self.E_start, self.E_end + 1):
                E = str(i).zfill(3)
                coordinates = "N{0}E{1}".format(str(N),E)
                file_name = coordinates + ".jpg"
                # Horizontal stitching
                url = f"https://e4ftl01.cr.usgs.gov/MEASURES/SRTMGL1.003/2000.02.11/{coordinates}.SRTMGL1.2.jpg"

                # request
                response = requests.get(url)

                if response.status_code == 404:
                    print("Copying new file.")
                    black_file = os.path.join(self.path, "zero.jpg")
                    new_file = os.path.join(self.path, file_name)
                    shutil.copyfile(black_file, new_file)


                else:
                    # save file
                    file = open(os.path.join(self.path, file_name),"wb")
                    file.write(response.content)
                    file.close()
                    print("Saved: " + file_name )

        
    def stitch_images(self):
        for i in range(self.N_start, (N_end-1),-1):
            N = i
            horImgs = None
            for j in range(self.E_start, self.E_end + 1):
                E = str(j).zfill(3)
                coordinates = "N{0}E{1}".format(str(N),E)
                file_name = coordinates + ".jpg"
                if j == self.E_start:
                    horImgs = cv2.imread(self.path + "\\" + file_name)
                else:
                    newImg = cv2.imread(self.path + "\\" + file_name)
                    addImg = np.concatenate((horImgs, newImg),axis=1)
                    horImgs = addImg
                # break

            cv2.imwrite(self.path + "\\" + "stitch.jpg", horImgs)
            print("Image written")


if __name__ == "__main__":

    n_start = 36 
    n_end =  0
    e_start = 64
    e_end = 116

    for i in range(n_start,(n_end-1),1):
        n = i
        horimgs = none
        for j in range(e_start, e_end + 1):
            e = str(j).zfill(3)
            coordinates = "n{0}e{1}".format(str(n),e)
            file_name = coordinates + ".jpg"
            if j == e_start:
                print(file_name)
                # horimgs = cv2.imread(path + "\\" + file_name)
            else:
                print(file_name)
                # newimg = cv2.imread(path + "\\" + file_name)
                # addimg = np.concatenate((horimgs, newimg),axis=1)
                # horimgs = addimg
            # break

    # cv2.imwrite(h + "\\" + "stitch.jpg", horImgs)
    # print("Image written")