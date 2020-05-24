import PySimpleGUI as gui
import os
import tensorflow as tf
import predict
import crop
import sys
import shutil
import time

import constants as c

gui.theme('DarkAmber')

directory = "toclassify"
store_base_dir = "store"
char_path = c.DATADIR_CHARS

imgs = []
predictions = []
for img in os.listdir(directory):
    imgs.append(os.path.join(directory, img))

file_counter = 0
pos_counter = 1

print("loading models...", flush=True)
#model_screen = tf.keras.models.load_model(c.SCREEN_MODEL_PATH)
model_char = tf.keras.models.load_model(c.CHAR_MODEL_PATH)


def get_shop():
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
    poss = [pos1, pos2, pos3, pos4, pos5]
    return poss


crop.crop_store(imgs[file_counter])
predictions = get_shop()


print("Setting up GUI", flush=True)
layout = [[gui.Text(predictions[0] + "-----------------------", key='text')],
          [gui.Image(r'store\pos1.png', key='image')],
          [gui.Button("yes", size=(50,10)), gui.Button("no", size=(50,10))]]

window = gui.Window("Simple Sorter", layout)


def remove_image(path):
    if os.path.exists(path):
        os.remove(path)


def clear_directory():
    print("Cleaning up directories by deleting duplicates...", flush=True)
    for image in os.listdir("store"):
        remove_image(os.path.join("store", image))
    for image in os.listdir("toclassify"):
        remove_image(os.path.join("toclassify", image))


def next_image(images):
    global file_counter, pos_counter, window, predictions
    pos_counter += 1
    if pos_counter >= 6:
        pos_counter = 1
        file_counter += 1
        try:
            crop.crop_store(images[file_counter])
            predictions = get_shop()
        except Exception:
            clear_directory()
            print("Finished!", flush=True)
            window.close()
            sys.exit(0)
    path = r'store\pos' + str(pos_counter) + ".png"
    window['image'].Update(path)
    window['text'].Update(predictions[pos_counter-1] + str(pos_counter))


def put_in_folder(correct):
    global predictions, pos_counter, char_path
    p_source = r'store\pos' + str(pos_counter) + ".png"
    new_name = 'store\\' + str(time.time()) + ".png"
    os.rename(p_source, new_name)
    p_source = new_name
    if correct:
        p_dest = os.path.join(char_path, predictions[pos_counter-1])
        shutil.copy(p_source, p_dest)
        print("Copied to: " + p_dest, flush=True)
    else:
        p_dest = "classified_wrong"
        shutil.copy(p_source, p_dest)
        print("Copied to: " + p_dest, flush=True)


while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event is 'yes':
        print("yes", flush=True)
        put_in_folder(True)
        next_image(imgs)
    if event is 'no':
        print("no", flush=True)
        put_in_folder(False)
        next_image(imgs)

clear_directory()
window.close()
