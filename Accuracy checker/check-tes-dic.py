import codecs
import pytesseract
import glob
from PIL import Image
import difflib

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

mylist = [f for f in glob.glob("../generate-images-java/Output/*")]
#mylist = [f for f in glob.glob("../generate-images-java/testout/*")]
#mylist = [f for f in glob.glob("images/*")]

g = codecs.open("tes-dic-out.txt", "w+", encoding="utf-8")

config = ('-l sin --oem 1 --psm 3')

f = codecs.open("dic.txt", encoding="utf-8")
dic_words = f.read().split()


for i in range(0, len(mylist)):
	print(i)
	text = pytesseract.image_to_string(Image.open(mylist[i]), config=config)
	splited = mylist[i].split("/")
	splited = splited[-1].split(".")
	splited = splited[-2].split("\\")
	correct = (splited[-1])
	
	if(text not in dic_words):
		
		diffout = difflib.get_close_matches(text,dic_words)
		if(len(diffout)!=0):
			text=diffout[0]
			
	
	g.write(text+"-")
	g.write(correct+"\n")

