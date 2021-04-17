from get_earth import GetEarth


# 835 , 1416
# p11 = (835, 1416)
# p12 = (885,1516)

# p1 = (886,1416)
# p2 = (935,1516)

# p1 = (885, 1415)
# p2 = (890, 1420)

# p1 = (890,1415)
# p2 = (895,1420)

# p1 = (835, 1416)
# p2 = (885,1516) # start where you end it

# p1 = (885, 1416)
# p2 = (935,1516)

# p1 = (835,1516)
# p2 = (935,1616)

# p1 = (935,1416)
# p2 = (1035,1516) # tamil nadu

# p1 = (935,1516)
# p2 = (1035,1616)

# p1 = (835,1616)
# p2 = (935,1716)

p1 = (935,1616)
p2 = (1035,1716)

dir =r"X:\library\texture\earth\zoom.earth"

# p1 = (1, 1)
# p2 = (10, 10)
i = GetEarth(p1,p2,dir)
i.fetch_images()
i.stitch_images()