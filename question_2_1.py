from PIL import Image
import PIL

image = Image.open('Question2/sample.png')
color = image.getcolors()
lis = []


# RGB color from image
for cc in color:
    lis.append(cc[1])


# RGB covert to hex_color
def hex_color(rgb):
    return "#" + "%02x%02x%02x" % rgb
lis2 = []
for l in lis:
    lis2.append(hex_color(l))


# hex to name
final_lis = []
for name, code in PIL.ImageColor.colormap.items():
    for l in lis2:
        if l == code:
            final_lis.append(name)



# count color
red = 0
blue = 0
# In Pillow, it displayed with lime instead of green but it is also green.
lime = 0
for fl in final_lis:
    if fl == "red":
        red += 1
    if fl == "green" or fl == "lime":
        lime += 1
    if fl == "blue":
        blue += 1



# In pillow, they mark lime instead of green. Can also see RGB and hex_color are exactly same as red, lime(green) and blue like lis and lis2,
print(f"lime(green): {lis[0]}, red: {lis[1]}, blue: {lis[2]}\nlime(green): {lis2[0]}, red: {lis2[1]}, blue: {lis2[2]}")

print(f"""------------------------------------------------
 red   : {red} pixels
 green : {lime} pixels
 blue  : {blue} pixels
------------------------------------------------""")



