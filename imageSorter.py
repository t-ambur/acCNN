import PySimpleGUI as gui
import os

import constants as c

gui.theme('DarkAmber')

directory = "toclassify"
store_base_dir = "store"
char_path = c.CHAR_PATH

imgs = []
for img in os.listdir(directory):
    imgs.append(os.path.join(directory, img))

counter = 0
image = imgs[counter]

layout = [[gui.Text("Is this correct?")],
          [gui.Image(imgs[counter], key='image')],
          [gui.Button("yes", size=(50,10)), gui.Button("no", size=(50,10))]]

window = gui.Window("Simple Sorter", layout)
counter += 1
window['image'].Update(imgs[counter])

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event is 'yes':
        print("yes", flush=True)
        counter += 1
        window['image'].Update(imgs[counter])
    if event is 'no':
        print("no", flush=True)

window.close()
