# get-earth
Get high res sat image of earth and stitch them.The data is sourced from [zoom.earth](https://zoom.earth/). 100 x 100 tiles give you you a total of 10000 individual tiles and when its all stitched together it totally give you a 25k x 25k image. So try not to go over 100 x 100 tiles.

## How to use it?
1. Import the `get_earth.GetEarth` module to your file.
2. Specify the P1(point one), P2(point two) and dir (directory to save the file.)
    ```python
    from get_earth import GetEarth

    # point 1
    p1 = (835, 1416)
    # point 2
    p2 = (885,1516)
    # directory to save file
    dir =r"X:\library\texture\earth\zoom.earth"
    # 
    getEarth = GetEarth(p1,p2,dir)
    getEarth.fetch_images()
    getEarth.stitch_images()
    ```