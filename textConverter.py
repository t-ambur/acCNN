import pytesseract
import cv2
import numpy as np
from PIL import Image
import PIL.ImageOps
import constants

'''
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 3)
    threshed = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite("blur.png", blurred)
    cv2.imwrite("threshed.png", threshed)
    #ret, img = cv2.threshold(np.array(grey), 125, 255, cv2.THRESH_BINARY)
    inverted = ~threshed
    cv2.imwrite("threshed-inverted.png", inverted)
    '''
    #resized_location = r"conversion\resized.png"
    #c = Image.open(image)
    #c = c.resize((c.size[0]*4, c.size[1]*4), 1)
    #c.save(resized_location)

    #image = cv2.imread(resized_location, cv2.IMREAD_GRAYSCALE)
    #cv2.imwrite(r"conversion\gray.png", image)
    #image = cv2.medianBlur(image, 3)
    #cv2.imwrite(r"conversion\blur.png", image)
    #image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #cv2.imwrite(r"conversion\threshed.png", image)


def convert_gold_to_text(image):
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'
    return pytesseract.image_to_string(image, config="--psm 7")  # 7 treat as single line for gold


def convert_bag_to_text(image):
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'

    resized_location = r"conversion\resized.png"
    c = Image.open(image)
    c = c.resize((c.size[0]*4, c.size[1]*4))
    c.save(resized_location)

    image = cv2.imread(resized_location, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(r"conversion\gray.png", image)
    image = ~image
    cv2.imwrite(r"conversion\inverted.png", image)

    return pytesseract.image_to_string(image)  # 7 treat as single line for gold


def convert_level_to_text(image):
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'

    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(r"conversion\gray.png", image)
    image = ~image
    cv2.imwrite(r"conversion\inverted.png", image)

    return pytesseract.image_to_string(image, config="--psm 7")  # 7 treat as single line for gold


def get_gold():
    string = convert_gold_to_text(constants.GOLD_IMG_LOCATION)
    return generic_get(string)


def get_level():
    string = convert_level_to_text(constants.LEVEL_IMG_LOCATION)
    return generic_get(string)

def get_bag_items():
    string = convert_bag_to_text(constants.BAG_IMG_LOCATION)
    string = string.replace("(", "")
    string = string.replace(")", "")
    return generic_get(string)


def generic_get(string):
    if string is None:
        return 0
    number = 0
    try:
        number = int(string)
    except Exception as e:
        number = 0
    return number
