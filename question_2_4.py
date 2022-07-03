from PIL import Image, ImageDraw, ImageFilter, ImageChops


im1 = Image.open('Question2/foreground.jpg')


background_img = Image.open('Question2/background.jpg').resize(im1.size)


mask = Image.open('Question2/mask.png').resize(im1.size)


mask = mask.convert("RGBA")

newImage = []
for data in mask.getdata():
    if data[:3] == (0, 255, 0):
        newImage.append((255, 255, 255, 0))
    else:
        newImage.append(data)

mask.putdata(newImage)

im = Image.composite(im1, background_img, mask)


im.show()