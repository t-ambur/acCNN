import pickle
import numpy as np
import time
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
import constants as c

# to run tensorboard:
# tensorboard --logdir=logs/


# loops to create different combinations for testing
def test_layers(path, size):
    inputlocation = os.path.join(path, c.X_NAME)
    pickle_in = open(inputlocation, 'rb')
    X = pickle.load(pickle_in)

    inputlocation = os.path.join(path, c.Y_NAME)
    pickle_in = open(inputlocation, 'rb')
    y = pickle.load(pickle_in)

    ###################################

    # rule of thumb, try one on each size +/-
    dense_layers = [0, 1, 2]
    layer_sizes = [32, 64, 128]
    conv_layers = [1, 2, 3]
    for dense_layer in dense_layers:
        for layer_size in layer_sizes:
            for conv_layer in conv_layers:
                NAME = "{}-conv-{}-nodes-{}-dense-{}".format(conv_layer, layer_size, dense_layer, int(time.time()))
                tensorboard = tf.keras.callbacks.TensorBoard(log_dir='logs\\{}'.format(NAME))
                print(NAME)

                model = tf.keras.Sequential()
                # (3,3) is windows, x.shape is IMG_SIZExIMG_SIZEx1 ignore -1
                model.add(tf.keras.layers.Conv2D(64, (3, 3), input_shape=X.shape[1:]))
                model.add(tf.keras.layers.Activation("relu"))
                model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))

                for l in range(conv_layer-1):
                    model.add(tf.keras.layers.Conv2D(64, (3, 3)))
                    model.add(tf.keras.layers.Activation("relu"))
                    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

                model.add(tf.keras.layers.Flatten())

                for l in range(dense_layer):
                    model.add(tf.keras.layers.Dense(layer_size))
                    model.add(tf.keras.layers.Activation("relu"))
                    model.add(tf.keras.layers.Dropout(0.2))

                # model.add(tf.keras.layers.Dense(64))
                # model.add(tf.keras.layers.Activation("relu"))

                # output
                model.add(tf.keras.layers.Dense(size))
                model.add(tf.keras.layers.Activation("softmax"))

                model.compile(loss="sparse_categorical_crossentropy",
                              optimizer="adam",
                              metrics=['accuracy'])

                y = np.asarray(y)

                model.fit(X, y, batch_size=6,
                          epochs=c.EPOCHS, validation_split=c.VALIDATION_SPLIT,
                          callbacks=[tensorboard])


test_layers(c.SCREEN_PATH, len(c.SCREEN_CATEGORIES))
