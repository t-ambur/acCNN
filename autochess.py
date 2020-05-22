from ahk import AHK
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # or any 0 all 1 no info 2 no info warning 3 filter all
import pyscreenshot as ImageGrab
import threading
import tensorflow as tf
import time
####
import constants as c
import controls
import predict
import crop
import textConverter
####

# fix the memory usage problems on both gpus
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
config = tf.config.experimental.set_memory_growth(physical_devices[0], True)
config = tf.config.experimental.set_memory_growth(physical_devices[1], True)

ahk = AHK()
controller = controls.Control()
counter = 0

print("Loading CNNs...", flush=True)
model_screen = tf.keras.models.load_model(c.SCREEN_MODEL_PATH)
# model2 = tf.keras.models.load_model(c.TEXT_MODEL_PATH)


def screenshot():
    # thread = threading.Timer(c.SCREEN_SHOT_INTERVAL, screenshot)
    # thread.daemon = True
    # thread.start()
    global counter
    if counter > 19:
        counter = 0
    window = ahk.active_window
    x = window.position[0]
    y = window.position[1]
    h = window.height
    w = window.width
    im = ImageGrab.grab(bbox=(x, y+c.SCREEN_SHOT_Y_REMOVAL, x + w, y + h))
    location = "screenshots\\screenshot" + str(counter) + ".png"
    counter += 1
    im.save(location)
    return location
    #  t = time.time()
    #  print("Window Captured:", str(location), flush=True)


def get_index_name(location):
    current_index = read(location)
    index_name = str(c.SCREEN_CATEGORIES[current_index])
    #  t = time.time() - t
    if current_index is not None:
        print(index_name, flush=True)
    else:
        print("Prediction returned None", flush=True)
    return index_name


def read(image):
    global model_screen
    return predict.predict(image, model_screen, "screen")


def get_level(location):
    crop.crop_level(location)
    return "LEVEL=" + str(textConverter.get_level()) + " "


def get_shop_info(location):
    crop.crop_gold(location)
    crop.crop_store(location)
    return "GOLD=" + textConverter.get_gold() + " "


def get_board_info(location):
    crop.crop_bag_icon(location)
    return "ITEMS_IN_BAG=" + textConverter.get_bag_items() + " "


looping = True
#  loop until keyboard interrupt
print("looping", flush=True)
try:
    while looping:
        location = screenshot()
        screen_name = get_index_name(location)

        report = "status: "
        report += get_level(location)

        if screen_name is "shop":
            report += get_shop_info(location)
            #controller.buy_1()
        elif screen_name is "board":
            report += get_board_info(location)
        elif screen_name is "get_item":
            controller.grab_item_1()
        else:
            report += " non-programmed screen"

        print(report, flush=True)

except KeyboardInterrupt as e:
    print("exiting..", flush=True)
    sys.exit()
