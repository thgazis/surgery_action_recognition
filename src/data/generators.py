import os

import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

BATCH_SIZE = 4
INPUT_DIM = (224,224)

class VideoDataGenerator(keras.utils.Sequence):
      
    def __init__(self, x_set, y_set, batch_size):
        self.x, self.y = x_set, y_set
        self.batch_size = batch_size

    def __len__(self):
        return int(np.ceil(len(self.x) / float(self.batch_size)))

    def __getitem__(self, idx):
        batch_x = self.x[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]
        output=np.array([self.load_video(video) for video in batch_x])
        return (output ,batch_y)

    def load_video(self, video):
        cap = cv2.VideoCapture(video)
        frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frameWidth = 224
        frameHeight = 224

        buf = np.empty((frameCount%4, frameHeight, frameWidth, 3), np.dtype('float'))

        fc = 0
        ret = True
        while (fc < frameCount  and ret):
            if fc%4 == 0:
                ret, frame = cap.read()
            
                try:
                    frame = cv2.resize(frame,(224,224))
                except :
                    frame = np.zeros((224,224,3))
                frame = cv2.normalize(frame, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
                buf[fc] = frame
                fc += 1
        cap.release()

        return np.stack([buf[0:12], buf[(frameCount//2):(frameCount//2+12)], buf[(frameCount-12):frameCount]])


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



