def convert(img_bin_file, lbl_bin_file,
            img_txt_file, lbl_txt_file, n_images):

  img_bf = open(img_bin_file, "rb")    # binary image pixels
  lbl_bf = open(lbl_bin_file, "rb")    # binary labels

  img_tf = open(img_txt_file, "w")     # text image pixels
  lbl_tf = open(lbl_txt_file, "w")     # text labels

  img_bf.read(16)   # discard image header info
  lbl_bf.read(8)    # discard label header info

  for i in range(n_images):   # number images requested 

    # do labels first for no particular reason
    lbl = ord(lbl_bf.read(1))  # get label like '3' (one byte) 
    encoded = [0] * 10         # make one-hot vector
    encoded[lbl] = 1
    for i in range(10):
      lbl_tf.write(str(encoded[i]))
      if i != 9: lbl_tf.write(" ")  # like 0 0 0 1 0 0 0 0 0 0 
    lbl_tf.write("\n")

    # now do the image pixels
    for j in range(784):  # get 784 vals for each image file
      val = ord(img_bf.read(1))
      img_tf.write(str(val))
      if j != 783: img_tf.write(" ")  # avoid trailing space 
    img_tf.write("\n")  # next image

  img_bf.close(); lbl_bf.close();  # close the binary files
  img_tf.close(); lbl_tf.close()   # close the text files

def main():

  convert(".\\UnzippedBinary\\train-images.idx3-ubyte.bin",
          ".\\UnzippedBinary\\train-labels.idx1-ubyte.bin",
          ".\\mnist_train_images_3.txt",
          ".\\mnist_train_labels_3.txt",
          n_images = 3)  # first n images

if __name__ == "__main__":
  main()
# show_mage.py

import numpy as np
import matplotlib.pyplot as plt

def display(img_txt_file, idx):
  # assumes an image file is 784 space-delimited
  # int values between 0-255

  data = np.loadtxt(img_txt_file, delimiter = " ")

  img = np.array(data[idx], dtype=np.float32)
  img = img.reshape((28,28))
  plt.imshow(img, cmap=plt.get_cmap('gray'))
  plt.show()

def main():
  print("\nBegin show MNIST image demo \n")

  img_file = ".\\mnist_train_images_3.txt"
  display(img_file, idx=0)  # first image

  print("\nEnd \n")

if __name__ == "__main__":
  main()