import codecs
import editdistance

#f = codecs.open("testing-out.txt", encoding="utf-8")
#f = codecs.open("tes-dic-out.txt", encoding="utf-8")
#f = codecs.open("tes-con-out.txt", encoding="utf-8")
#f = codecs.open("tes-out.txt", encoding="utf-8")
#f = codecs.open("google-result.txt", encoding="utf-8")
#f = codecs.open("tes-con-out-100.txt", encoding="utf-8")
f = codecs.open("tes-con-dic-out-100.txt", encoding="utf-8")
lines = f.read().splitlines()

#totalcharacters=0
#correctocr=0

totalCER = []
totalWER = []
totalWords = 0
correctWords = 0

	
for i in range(0,len(lines)):
	print(i)
	totalWords +=1
	split=lines[i].split("-")
	if(len(split)!=2):
		continue
	ocr=split[0]
	correct=split[1]

	#removing half space at the end of the OCRed text
	if(ocr!=""):
		if(ord(ocr[-1])==8204):
			ocr=ocr[:-1]

	dist = editdistance.eval(ocr, correct)
	if(dist==0):
		correctWords += 1

	currCER = dist / max(len(ocr), len(correct))
	totalCER.append(currCER)
	
	#minlength=0
	#if(len(ocr)<len(correct)):
	#	minlength=len(ocr)
	#else:
	#	minlength=len(correct)
		
	#totalcharacters = totalcharacters + len(correct)
		
	#for j in range(0,minlength):
	#	if(ocr[j]==correct[j]):
	#		correctocr=correctocr+1
	
    
	
charErrorRate = sum(totalCER) / len(totalCER)	

			
#print("total cahracter count: "+str(totalcharacters))
#print("correctly ocred character counter: "+ str(correctocr))
#print("accuracy: "+str(round(correctocr*100/totalcharacters,2))+"%")

print("Charactr level accuracy: "+str(round((1-charErrorRate)*100,2))+"%")
print("Word level accuracy: "+str(round(correctWords/totalWords*100,2))+"%")