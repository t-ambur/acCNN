import PySimpleGUI as gui
import os
import sys
import shutil
import time

import constants as c

gui.theme('DarkAmber')

directory = "record"
screen_path = c.DATADIR_SCREENS

imgs = []
names = []
for img in os.listdir(directory):
    imgs.append(os.path.join(directory, img))

file_counter = 0

for folder_name in os.listdir(screen_path):
    name = str(folder_name)
    names.append(name)


print("Setting up GUI", flush=True)
layout = [[gui.Text("What is this image?")],
          [gui.Image(imgs[0], key='image'),
          gui.Listbox(values=names, size=(25,55), key="list", enable_events=True),
          gui.Button("skip", size=(10,50))]]

window = gui.Window("Wrong Sorter", layout)


def remove_image(path):
    if os.path.exists(path):
        print("would remove", str(path))
        #os.remove(path)


def clear_directory():
    global directory
    print("Cleaning up directories by deleting duplicates...", flush=True)
    for image in os.listdir(directory):
        remove_image(os.path.join(directory, image))


def next_image(images):
    global file_counter, window
    file_counter += 1
    try:
        path = images[file_counter]
        window['image'].Update(path)
    except Exception as e:
        print("assuming out of images...", str(e))
        clear_directory()
        print("Finished!", flush=True)
        window.close()
        sys.exit(0)


def put_in_folder(fold_name, imgs):
    global screen_path, file_counter
    p_source = imgs[file_counter]
    p_dest = os.path.join(screen_path, fold_name)
    temp_name = str(time.time()) + ".png"
    new_name = os.path.join("record", temp_name)
    os.rename(p_source, new_name)
    p_source = new_name
    shutil.copy(p_source, p_dest)
    print("Copied to: " + p_dest, flush=True)
    if str(fold_name) == "shop":
        p_dest = "toclassify"
        shutil.copy(p_source, p_dest)
        print("Copied to: " + p_dest, flush=True)


while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event in "skip":
        print("skipping...", flush=True)
        next_image(imgs)
    elif values['list']:
        put_in_folder(values['list'][0], imgs)
        next_image(imgs)

#clear_directory()
window.close()
