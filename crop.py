from PIL import Image
import constants as c
import sys


# 1600x900


def crop_store(image_name):
    im = Image.open(image_name)

    x1 = c.BUY1_X1
    y1 = c.BUY1_Y1
    x2 = c.BUY1_X2
    y2 = c.BUY1_Y2

    im_cropped = im.crop((x1, y1, x2, y2))
    im_cropped.save("store\\pos1.png")

    for i in range(4):
        temp = x1
        x1 = x2
        x2 += (x2 - temp)
        im_cropped = im.crop((x1, y1, x2, y2))
        number = i + 2
        im_cropped.save("store\\pos" + str(number) + ".png")


def crop_gold(image_name):
    im = Image.open(image_name)

    x1 = 1230
    x2 = 1280

    y1 = 10
    y2 = 40

    im_cropped = im.crop((x1, y1, x2, y2))
    im_cropped.save("status\\gold.png")


def crop_level(image_name):
    im = Image.open(image_name)

    x1 = 168
    x2 = 188

    y1 = 750
    y2 = 775

    im_cropped = im.crop((x1, y1, x2, y2))
    im_cropped.save("status\\level.png")


def crop_bag_icon(image_name):
    im = Image.open(image_name)

    x1 = 1308
    x2 = 1343

    y1 = 755
    y2 = 787

    im_cropped = im.crop((x1, y1, x2, y2))
    im_cropped.save("status\\bagicon.png")


if len(sys.argv) > 1:
    crop_store(sys.argv[1])
    print("cropped. Done.")
