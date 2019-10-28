import numpy as np
#from skdata.mnist.views import OfficialImageClassification
#from matplotlib import pyplot as plt
#from PIL import Image 
import os, os.path                                                           
#import glob

import cv2 as cv2

num_images = input()
DirectoryPath = '../generate-images-java/characterGenerator/Output'
relativepath = os.path.curdir
data = []
for i in range(2,int(num_images)):
    imagePath = relativepath +"/"+ str(i)+".png"
    print(imagePath)
    absolutepath =os.path.abspath(imagePath)
    
    image = cv2.imread(absolutepath)
    x_data = np.array(image)
    print(x_data)
    print(absolutepath)
    pixelArray = x_data.flatten()
    print(pixelArray)
    data.append(pixelArray)

#x_data = np.array( [np.array(cv2.imread(imagePath[i])) for i in range(len(imagePath))] )

#pixels = x_data.flatten()
print(pixelArray)