import numpy as np
import os
import random
import cv2  # for image manipulation
import pickle
import sys
import constants as c

# CURRENTLY ONLY FOR SCREENS

# train holds all folders containing labels
DATADIR_SCREENS = "train\\screens"
DATADIR_CHARS = "train\\characters"
# resize to a square IMG_SIZE x IMG_SIZE
training_data = []


def create_training_data(CATEGORIES, width, height, directory):
    for category in CATEGORIES:
        path = os.path.join(directory, category)
        index = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img),
                                       cv2.IMREAD_GRAYSCALE)  # convert to array, convert to greyscale
                img_array = img_array/255  # normalize
                new_array = cv2.resize(img_array, (width, height))  # resize
                training_data.append([new_array, index])
            except Exception as e:
                print(str(img), "could not preprocess", flush=True)
                pass


def prep(categories, width, height, directory):
    training_data.clear()
    print("preparing images...", flush=True)
    create_training_data(categories, width, height, directory)
    print("shuffling data", flush=True)
    random.shuffle(training_data)
    X = []  # capital X is your feature set
    y = []  # lowercase y is your labels
    print("generating pickle files...", flush=True)
    for features, label in training_data:
        X.append(features)
        y.append(label)

    # -1 for any number, 1 for grayscale (3 for RGB)
    X = np.array(X).reshape(-1, width, height, 1)
    return X, y


def save(X, y, location):
    outputlocation = os.path.join(location, c.X_NAME)
    pickle_out = open(outputlocation, 'wb')
    pickle.dump(X, pickle_out)
    pickle_out.close()
    print("X done.", flush=True)
    outputlocation = os.path.join(location, c.Y_NAME)
    pickle_out = open(outputlocation, 'wb')
    pickle.dump(y, pickle_out)
    pickle_out.close()
    print("Y done.\nPrepare complete.", flush=True)
    training_data.clear()


prep_num = 0
if len(sys.argv) > 1:
    try:
        prep_num = int(sys.argv[1])
    except Exception:
        prep_num = 0


if prep_num == 0 or prep_num == 1:
    #  Screen
    print("Preparing SCREEN", flush=True)
    X, y = prep(c.SCREEN_CATEGORIES, c.IMG_SIZE_SCREEN_WIDTH, c.IMG_SIZE_SCREEN_HEIGHT, DATADIR_SCREENS)
    save(X, y, c.SCREEN_PATH)

if prep_num == 0 or prep_num == 2:
    #  Characters
    print("Preparing Characters", flush=True)
    X, y = prep(c.CHAR_CATEGORIES, c.IMG_SIZE_CHAR_WIDTH, c.IMG_SIZE_CHAR_HEIGHT, DATADIR_CHARS)
    save(X, y, c.CHAR_PATH)
