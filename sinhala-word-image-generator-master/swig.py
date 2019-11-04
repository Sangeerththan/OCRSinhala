from PIL import Image, ImageDraw, ImageFont

import random
import string
import codecs

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
 

#f=open("testdic.txt", "r")

def Toggler(symbol,document):
    	with open("document", "r") as ins:
    	    array = []
            for line in ins:
                array.append(line)
			for lines in array:
				for symbol in lines:
					index_symbol = index(symbol)
					index_symbol-=1
					lines.delete(index_symbol)
					lines.insert(symbol,index_symbol+1)
	return document


f = codecs.open("dic.txt", encoding="utf-8")
lines = f.read().splitlines()
print(lines)   	
for i in range(0,len(lines)):	
	
	line= lines[i]
	textlength = len(line)	
	img = Image.new('RGB', (28*textlength+20, 70), color = (255, 255, 255))	 
	fnt = ImageFont.truetype('/fonttype/Nirmala.ttf', 14)
	d = ImageDraw.Draw(img)
	d.text((10,10), line, font=fnt, fill=(0, 0, 0))	 
	img.save('Nirmala-14/'+line+'.png')
	
f.close()