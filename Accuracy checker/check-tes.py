import pytesseract
from PIL import Image
import glob
import codecs
import math
import numpy
import re

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

#mylist = [f for f in glob.glob("../generate-images-java/Output/*")]
#mylist = [f for f in glob.glob("../generate-images-java/testout/*")]
#mylist = [f for f in glob.glob("images/*")]
mylist = [f for f in glob.glob("../generate-images-java/testing-100-images/*")]

g = codecs.open("tes-out-100.txt", "w+", encoding="utf-8")

config = ('-l sin --oem 1 --psm 3')



for i in range(0, len(mylist)):
	print(i)
	
	text = pytesseract.image_to_string(Image.open(mylist[i]), config=config)
	splited = mylist[i].split("/")
	splited = splited[-1].split(".")
	splited = splited[-2].split("\\")
	correct = (splited[-1])
	g.write(text+"-")
	g.write(correct+"\n")
	








