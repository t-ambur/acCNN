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
import predict
import crop
import textConverter
import AI_Player
####

# fix the memory usage problems on both gpus
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
config = tf.config.experimental.set_memory_growth(physical_devices[0], True)
config = tf.config.experimental.set_memory_growth(physical_devices[1], True)

ahk = AHK()
player = AI_Player.Player(ahk)
state = AI_Player.State()
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


def get_index_name(location):
    current_index = read(location)
    index_name = str(c.SCREEN_CATEGORIES[current_index])
    return index_name


def read(image):
    global model_screen
    return predict.predict(image, model_screen, "screen")


def get_level(player):
    return "LEVEL=" + str(player.get_level()) + " "


def get_shop_info(location, player):
    crop.crop_store(location)
    return "GOLD=" + str(player.get_gold()) + " "


def get_board_info(player):
    level = get_level(player)
    return level + "ITEMS_IN_BAG=" + str(player.get_items()) + " "


looping = True
#  loop until keyboard interrupt
print("looping", flush=True)
try:
    while looping:
        location = screenshot()
        screen_name = get_index_name(location)
        st = state.get_state()
        report = screen_name + " -- status: "

        if screen_name is "shop":
            report += get_shop_info(location, player)
            if st is "shop":
                if player.get_store().num_bought <= 0:
                    success = player.buy_pos(1, 5)
                    report += "bought?: " + str(success) + " "
                    state.next()
        elif screen_name is "board":
            report += get_board_info(player)
            if st is "board":
                if player.can_deploy_character():
                    player.deploy(1)
                    state.next()
        elif screen_name is "get_item":
            if st is "item":
                player.choose_item(1)
                state.next()
        else:
            report += " non-programmed screen"

        print(report, flush=True)

except KeyboardInterrupt as e:
    print("\nexiting..", flush=True)
    sys.exit()


# These are for the google image to text that works poorly
'''
def get_level(location):
    crop.crop_level(location)
    return "LEVEL=" + str(textConverter.get_level()) + " "


def get_shop_info(location):
    crop.crop_gold(location)
    crop.crop_store(location)
    return "GOLD=" + str(textConverter.get_gold()) + " "


def get_board_info(location):
    crop.crop_bag_icon(location)
    level = get_level(location)
    return level + "ITEMS_IN_BAG=" + str(textConverter.get_bag_items()) + " "
'''
