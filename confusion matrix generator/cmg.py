import pytesseract 
from PIL import Image
import glob
import codecs

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

mylist = [f for f in glob.glob("images/*")]

f = codecs.open("conf_characters.txt", encoding="utf-8")
confusion_list = f.read().splitlines()
config = ('-l sin --oem 1 --psm 3')

g = codecs.open("cmgText.txt","w+",encoding="utf-8" )

 
ocr=[]
correct=[]

matrix=[]
for s in range (0, len(confusion_list)):
	matrixline=[]
	for p in range (0, len(confusion_list)):
		matrixline.append(0)
	matrix.append(matrixline)



for i in range(0,len(mylist)):
	correct.append(mylist[i][7:-4])
	text = pytesseract.image_to_string(Image.open(mylist[i]),config=config)
	ocr.append(text)
	
for j in range(0,len(ocr)):
	if(len(ocr[j]) ==  len(correct[j])):
		for k in range(0,len(ocr[j])):
			if ((ocr[j][k] != correct[j][k]) & (ocr[j][k] in confusion_list) & (correct[j][k] in confusion_list)):
				ocrIndex = confusion_list.index(ocr[j][k])
				correctIndex = confusion_list.index(correct[j][k])
				g.write(ocr[j])
				g.write(correct[j-1])
				g.write("/n")
				g.write(ocr[j][k])
				g.write(correct[j][k])
				print(matrix[ocrIndex])
				print(matrix[ocrIndex+1])
				matrix[ocrIndex][correctIndex]=matrix[ocrIndex][correctIndex]+1
				print(matrix[ocrIndex])
				print(matrix[ocrIndex+1])
				print("incremented")
				print(j)
				print(k)
				print (ocrIndex)
				print(correctIndex)
				
				
				
print (matrix)	

for i in range (0,len(ocr)):
	g.write(ocr[i]+"-")
	g.write(correct[i]+"\n")
	
g.write(ocr[0][1])
#g = codecs.open("cmgText.txt","w+",encoding="utf-8" )
#g.write(correct[0])


