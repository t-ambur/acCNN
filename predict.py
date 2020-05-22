import cv2
import tensorflow as tf
import constants as c


def prepare(filepath, width, height):
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img_array = img_array/255.0
    new_array = cv2.resize(img_array, (width, height))
    return new_array.reshape(-1, width, height, 1)


def predict(filepath, model, model_name):
    prediction = None
    if model_name is "screen":
        prediction = model.predict_classes([prepare(filepath, c.IMG_SIZE_SCREEN_WIDTH, c.IMG_SIZE_SCREEN_HEIGHT)])
    elif model_name is "character":
        prediction = model.predict_classes([prepare(filepath, c.IMG_SIZE_CHAR_WIDTH, c.IMG_SIZE_CHAR_HEIGHT)])
    else:
        print("Invalid model name provided", flush=True)
        return None

    # print(prediction)
    index = prediction[0]
    return index

# prediction = model.predict_classes([prepare('dog.jpg')])
