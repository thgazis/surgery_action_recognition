# Surgery action recognition
This is the source code for surgery action recognition.

The data used was acquired in University of Athens, Dept. of Medicine, 
Medical Physics Lab by Dr C. Loukas.

There is a dockerfile to build a docker image and run the code.
To build the image:

docker build - < Dockerfile

After the image is built run:

docker run -it --gpus all  --mount type=bind,source="$(pwd)"/projects/surgery_action_recognition/,target=/app video-deep-learning:latest


### TO DO's ###

1) Fine-tune a conv3d model for next-frame prediction

2) Build a classifier using the fine-tuned model

3) Build a classifier using the a not fine-tuned model

4) Compare results