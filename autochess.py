from ahk import AHK
import sys
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # or any 0 all 1 no info 2 no info warning 3 filter all
import pyscreenshot as ImageGrab
import tensorflow as tf
import time
####
import constants as c
import predict
import crop
import AI_Player
####

# fix the memory usage problems on both gpus
#physical_devices = tf.config.experimental.list_physical_devices('GPU')
#assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
#config = tf.config.experimental.set_memory_growth(physical_devices[0], True)
#config = tf.config.experimental.set_memory_growth(physical_devices[1], True)

ahk = AHK()
counter = 0

print("Loading CNNs...", flush=True)
model_screen = tf.keras.models.load_model(c.SCREEN_MODEL_PATH)
model_char = tf.keras.models.load_model(c.CHAR_MODEL_PATH)


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


def read_shop():
    global model_char
    pos1_i = predict.predict(r'store\pos1.png', model_char, "character")
    pos2_i = predict.predict(r'store\pos2.png', model_char, "character")
    pos3_i = predict.predict(r'store\pos3.png', model_char, "character")
    pos4_i = predict.predict(r'store\pos4.png', model_char, "character")
    pos5_i = predict.predict(r'store\pos5.png', model_char, "character")
    pos1 = c.CHAR_CATEGORIES[pos1_i]
    pos2 = c.CHAR_CATEGORIES[pos2_i]
    pos3 = c.CHAR_CATEGORIES[pos3_i]
    pos4 = c.CHAR_CATEGORIES[pos4_i]
    pos5 = c.CHAR_CATEGORIES[pos5_i]
    output = ">>> 1=" + pos1 + " 2=" + pos2 + "\n>>>3=" + pos3 + " 4=" + pos4 + "\n>>>5=" + pos5
    print(output, flush=True)


def get_level(player):
    return "LEVEL=" + str(player.get_level()) + " "


def get_shop_info(location, player):
    crop.crop_store(location)
    read_shop()
    return "GOLD=" + str(player.get_gold()) + " "


def get_board_info(player):
    level = get_level(player)
    return level + "ITEMS_IN_BAG=" + str(player.get_items()) + " "


current_round = 1
if len(sys.argv) > 1:
    try:
        current_round = int(sys.argv[1])
    except Exception:
        current_round = 1

player = AI_Player.Player(ahk, current_round)
state = AI_Player.State(current_round)
looping = True
#  loop until keyboard interrupt
print("looping", flush=True)
try:
    while looping:
        location = screenshot()
        screen_name = get_index_name(location)
        st = state.get_state()
        if state.get_round() > current_round:
            current_round = state.get_round()
            player.next_round()
        report = "CNN: " + screen_name + " state: " + str(st) + " -- status: "

        if screen_name is "shop":
            report += get_shop_info(location, player)
            if st is "shop":
                time.sleep(1)
                if player.get_store().num_bought <= 0:
                    success = player.buy_pos(1, 5)
                    if success:
                        player.leave_store()
                        state.next_state()
                    report += "bought?: " + str(success) + " "
        elif screen_name is "board":
            report += get_board_info(player)
            if st is "board":
                if player.can_deploy_character():
                    player.deploy(1)
                state.next_state()
        elif screen_name is "get_item":
            if st is "item":
                player.choose_item(1, 1)
                state.next_state()
        else:
            report += " non-programmed screen"

        print(report, flush=True)

except KeyboardInterrupt as e:
    print("\nexiting..", flush=True)
    sys.exit()
