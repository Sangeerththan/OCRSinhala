import codecs

#f = codecs.open("testing-out.txt", encoding="utf-8")
#f = codecs.open("tes-dic-out.txt", encoding="utf-8")
f = codecs.open("tes-con-out.txt", encoding="utf-8")
#f = codecs.open("tes-out.txt", encoding="utf-8")
lines = f.read().splitlines()

totalcharacters=0
correctocr=0

for i in range(0,len(lines)):
	print(i)
	split=lines[i].split("-")
	if(len(split)!=2):
		continue
	ocr=split[0]
	correct=split[1]
	minlength=0
	if(len(ocr)<len(correct)):
		minlength=len(ocr)
	else:
		minlength=len(correct)
		
	totalcharacters = totalcharacters + len(correct)
		
	for j in range(0,minlength):
		if(ocr[j]==correct[j]):
			correctocr=correctocr+1
			
print("total cahracter count: "+str(totalcharacters))
print("correctly ocred character counter: "+ str(correctocr))
print("accuracy: "+str(round(correctocr*100/totalcharacters,2))+"%")