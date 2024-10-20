from django.shortcuts import render
import os
import numpy
import cv2
from keras.models import load_model
from django.core.files.storage import default_storage
from django.conf import settings
