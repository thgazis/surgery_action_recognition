import tensorflow as tf
from src.inception3d.i3d_inception import Inception_Inflated3d, WEIGHTS_NAME
from tensorflow.keras.layers import Flatten, Dense


def create_model():
    model = Inception_Inflated3d(False, WEIGHTS_NAME[0],input_shape=[32,224,224,3])
    model.add(Flatten())
    model.add(Dense(units=512))
    return model