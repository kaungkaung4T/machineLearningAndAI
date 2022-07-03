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

im = im.crop((512, 512, 1536, 1536)) # left, top, right, bottom
w, h = im.size
print(w, h)


im = im.rotate(-30)
print(im.size)

im.save("Question2/result4.jpg")
im.show()
