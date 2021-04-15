import requests
response = requests.get("https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/11/971/1475")

file = open("sample_image.png", "wb")
file.write(response.content)
file.close()