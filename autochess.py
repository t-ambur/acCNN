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
    im.save(location)
    #  t = time.time()
    #  print("Window Captured:", str(location), flush=True)
    current_index = read(location)
    index_name = str(c.SCREEN_CATEGORIES[current_index])
    #  t = time.time() - t
    if current_index is not None:
        print(index_name + " " + str(counter), flush=True)
    else:
        print("Prediction returned None", flush=True)
    counter += 1
    return index_name


def read(image):
    global model_screen
    return predict.predict(image, model_screen, "screen")


looping = True
#  loop until keyboard interrupt
print("looping", flush=True)
try:
    while looping:
        screen_name = screenshot()
        if screen_name is "shop":
            controller.buy_1()

except KeyboardInterrupt as e:
    print("exiting..", flush=True)
    sys.exit()
