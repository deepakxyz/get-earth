import os
import shutil

N_start = 36
N_end =  10
E_start = 64
E_end = 116
path = r"X:\library\texture\earth\zoom.earth\height_30SRTM"

for j in range(N_start,(N_end-1),-1):
    N = str(j).zfill(2)
    for i in range(E_start, E_end + 1):
        E = str(i).zfill(3)
        coordinates = "N{0}E{1}".format(str(N),E)
        file_name = coordinates + ".jpg"
        # Horizontal stitching
        file_loc = os.path.join(path, file_name)
        # print(file_loc)
        if os.path.isfile(file_loc):
            print("file_exists")
        else:
            black_file = os.path.join(path, "zero.jpg") 
            shutil.copyfile(black_file,file_loc)
            print("New file: " , file_name)
        # break

        
    #     empty_file = r'Z:\Piper\workbench\copyandrenamefile\empty_ma.mb'
    # new_file = os.path.join(ROOT_DIR,project_id,cat,asset_name)
    # new_file = os.path.join(new_file , 'll_ch_lou_mod_v001.mb')
    # print(new_file)
