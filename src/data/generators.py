import os

import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

BATCH_SIZE = 4
INPUT_DIM = (224,224)

class VideoFramesGenerator(keras.utils.Sequence):
    ''' Custom generator class from next
        frame prediction
        Input: File paths of video data
        '''
    def __init__(
        self, 
        input_dir,
        batch_size=32, 
        shuffle=True
        ):

        self.input_dir =input_dir
        self.batch_size = batch_size
        self.indices = list(range(len(os.listdir(input_dir))))
        self.files = os.listdir(input_dir)
        self.shuffle = shuffle
        self.on_epoch_end()
        
    def on_epoch_end(self):
        self.index = np.arange(len(self.indices))
        if self.shuffle == True:
            np.random.shuffle(self.index)

    def __len__(self):
        # Denotes the number of batches per epoch
        return len(self.indices) // self.batch_size

    def __getitem__(self, index):
        # Generate one batch of data
        # Generate indices of the batch
        index = self.index[index * self.batch_size:(index + 1) * self.batch_size]

        batch = [self.indices[k] for k in index]     # Generate data
        X, y = self.__get_data(batch)
        return X, y

    def __get_data(self, batch):
        X = list(range(BATCH_SIZE))
        y = list(range(BATCH_SIZE+1))
        
        for i, id in enumerate(batch):
            X[i], y[i] = self.__get_video(self.files[id])

        return X, y

    def __get_video(self, video):
        x = []
        y = [0]
        video_file = os.path.join(self.input_dir, video)
        cap = cv2.VideoCapture(video_file)
        if (cap.isOpened()== False):
            print("Error opening video stream or file")
        i = 0
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                norm_image = cv2.normalize(frame, None, alpha=0,
                                           beta=1, norm_type=cv2.NORM_MINMAX,
                                           dtype=cv2.CV_32F)
                image = cv2.resize(norm_image, INPUT_DIM)
                x.append(image)
                y.append(image)
                i += 1 
            else: 
                break

        cap.release()
        return x, y