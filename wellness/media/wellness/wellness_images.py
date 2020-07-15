from PIL import Image

im = Image.open("alexander-w-oEpnMn1y-7A-unsplash.jpg")

def img_details():
    print(im.format, im.size, im.mode)

img_details()