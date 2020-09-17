import cv2
import os
import numpy as np


FRAME_WIDTH = 224
FRAME_HEIGHT = 224

def compress_videos(input_path, output_path):
    print(os.getcwd())

    for video in os.listdir(input_path):
        input_video = os.path.join(input_path, video)
        print(input_video)
        output_video = os.path.join(output_path,video)
        cap = cv2.VideoCapture(input_video)
        out = cv2.VideoWriter(output_video,
                            cv2.VideoWriter_fourcc('M','J','P','G'),
                            10,
                            (FRAME_WIDTH,FRAME_HEIGHT))
        frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(frameCount)
        fc = 0
        ret = True
        while (fc < frameCount  and ret):
            if fc%4 == 0:
                ret, frame = cap.read()
                print("Currently processing %s frame", fc)
            
                try:
                    frame = cv2.resize(frame,(224,224))
                except :
                    frame = np.zeros((224,224,3))
                # frame = cv2.normalize(frame, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
                # buf[fc] = frame
                print('Writing')
                out.write(frame)
                print('Written')
            fc += 1
        cap.release()