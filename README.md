# Surgery_action_recognition
This is the source code for surgery action recognition.

The data used was acquired in University of Athens, Dept. of Medicine, 
Medical Physics Lab by Dr C. Loukas.

There is a dockerfile to build a docker image and run the code.
After the image is built run:

docker run -it --gpus all  --mount type=bind,source="$(pwd)"/projects/surgery_action_recognition/,target=/app video-deep-learning:latest