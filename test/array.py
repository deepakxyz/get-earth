import numpy as np
import requests

base_url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/11/"


x1, y1 = 968,1477
x2, y2 = 971,1480

xdist = x2 - x1
ydist = y2 - y1

for i in range(xdist):
    for j in range(ydist):
        print(x1 + i, y1 + j)
        url = base_url + str(x1 + i) + "/" + str(y1 + j)
        file_name = str(x1 + i ) + "_" + str(y1 + j) + ".png"
        # request
        response = requests.get(url)
        
        # save file
        file = open(file_name, "wb")
        file.write(response.content)
        file.close()


