from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import tensorflow as tf
import pickle
import numpy as np
import constants as c
import os
import sys

# fix the memory usage problems on both gpus
#physical_devices = tf.config.experimental.list_physical_devices('GPU')
#assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
#config = tf.config.experimental.set_memory_growth(physical_devices[0], True)
#config = tf.config.experimental.set_memory_growth(physical_devices[1], True)


def load_pickles(path):
    inputlocation = os.path.join(path, c.X_NAME)
    pickle_in = open(inputlocation,"rb")
    X = pickle.load(pickle_in)

    inputlocation = os.path.join(path, c.Y_NAME)
    pickle_in = open(inputlocation,"rb")
    y = pickle.load(pickle_in)
    return X, y


def train(X, y, dense_layers, layer_sizes, conv_layers, output_size):
    model = None
    print("building network...", flush=True)
    for dense_layer in dense_layers:
        for layer_size in layer_sizes:
            for conv_layer in conv_layers:
                model = Sequential()

                model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))
                model.add(Activation('relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))

                for l in range(conv_layer-1):
                    model.add(Conv2D(layer_size, (3, 3)))
                    model.add(Activation('relu'))
                    model.add(MaxPooling2D(pool_size=(2, 2)))

                model.add(Flatten())

                for _ in range(dense_layer):
                    model.add(Dense(layer_size))
                    model.add(Activation('relu'))

                model.add(Dense(output_size))
                model.add(Activation('softmax'))

                # tensorboard = TensorBoard(log_dir="logs\\{}".format(NAME))
                print("Compiling model...", flush=True)
                model.compile(loss='sparse_categorical_crossentropy',
                              optimizer='adam',
                              metrics=['accuracy'],
                              )

                y = np.asarray(y)
                print("Start training", flush=True)
                model.fit(X, y,
                          batch_size=c.BATCH_SIZE,
                          epochs=c.EPOCHS,
                          validation_split=c.VALIDATION_SPLIT)

    return model


prep_num = 0
if len(sys.argv) > 1:
    try:
        prep_num = int(sys.argv[1])
    except Exception:
        prep_num = 0
if prep_num == 0 or prep_num == 1:
    # screen.model
    # 3 EPOCHS
    print("training screen model...", flush=True)
    ##########
    dense_layers = [0]
    layer_sizes = [32]  # nodes
    conv_layers = [1]
    output_size = len(c.SCREEN_CATEGORIES)
    path = c.SCREEN_PATH
    model_path = c.SCREEN_MODEL_PATH
    ##########
    print("loading pickle files...", flush=True)
    data, labels = load_pickles(path)
    model = train(data, labels, dense_layers, layer_sizes, conv_layers, output_size)
    print("saving model...", flush=True)
    save_location = model_path
    model.save(save_location)
    print("Complete. Model saved to:", save_location)
    print("\n\n", flush=True)

if prep_num == 0 or prep_num == 2:
    # character.model
    # 3 EPOCHS
    print("training character model...", flush=True)
    ##########
    dense_layers = [0]
    layer_sizes = [32]  # nodes
    conv_layers = [1]
    output_size = len(c.CHAR_CATEGORIES)
    path = c.CHAR_PATH
    model_path = c.CHAR_MODEL_PATH
    ##########
    print("loading pickle files...", flush=True)
    data, labels = load_pickles(path)
    model = train(data, labels, dense_layers, layer_sizes, conv_layers, output_size)
    print("saving model...", flush=True)
    save_location = model_path
    model.save(save_location)
    print("Complete. Model saved to:", save_location)
    print("\n\n", flush=True)
