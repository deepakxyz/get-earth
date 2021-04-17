from get_earth_height import GetEarthHeight

N_start = 10
N_end =  0
E_start = 64
E_end = 116
path = "X:/library/texture/earth/zoom.earth/height_30SRTM"
height = GetEarthHeight(N_start,N_end,E_start,E_end,path)

height.fetch_images()
# height.stitch_images()