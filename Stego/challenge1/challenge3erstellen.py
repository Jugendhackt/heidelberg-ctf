from PIL import Image, ImageDraw, ImageFont
im = Image.open("logo.png")
print(im.format, im.size, im.mode)
#im.save("logo.png", "PNG")
#flag: jhhdcft{..}
draw = ImageDraw.Draw(im)
txt = Image.new("RGB", im.size, (0, 0, 0))
d = ImageDraw.Draw(txt)
#fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
d.text((10, 10), "Du bist ein CTF-Alpaka! Flag: jhhdctf{2020}", fill=(255, 255, 255))
txt.save("txt.png")

for x in range(im.size[0]):
    for y in range(im.size[1]):
        if txt.getpixel((x, y)) == (255, 255, 255):
            cur = im.getpixel((x, y))
            #im.putpixel((x,y), (cur[0]-3, cur[1]-3, cur[2]-3))
            im.putpixel((x,y), (cur[0]-3, cur[1]-3, cur[2]-3))
im.save("test.png")