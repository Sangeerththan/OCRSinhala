import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt
from skimage.transform import resize as imresize
import cv2
import time

directory = '../generate-images-java/characterGenerator/'
images = ['%d.png'%(d) for d in range(100000)]
with open(directory+'characters.txt','r') as fopen:
    labels = [i.split()[0] for i in list(filter(None,fopen.read().split('\n')))]
len(images)
len(labels)