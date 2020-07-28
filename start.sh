#!/bin/bash


# TODO : check if the dependancy alreay exists

# Get into backend folder
cd Backend
# create virtual env
virtualenv communicate

# activate virtual env
source ./communicate/bin/activate

# install opencv-python
pip3 install -r requirements.txt

# Run
python3 step_5_camera.py