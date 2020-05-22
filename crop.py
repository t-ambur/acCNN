from PIL import Image
import constants as c
import sys



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

    print("Done.")


if len(sys.argv) > 1:
    crop_store(sys.argv[1])
