import codecs

f = codecs.open("sin_long.txt", encoding="utf-8")
ocr_words = f.read().split()
f.close

g = codecs.open("dic.txt", encoding="utf-8")
dic_words = g.read().split()
g.close

fulllist = []

for i in range(0, len(ocr_words)):
	checkdic=False
	checked_word=[]
	for j in range (0, len(dic_words)):
		if(ocr_words[i]==dic_words[j]):
			checkdic=True
			break
	if(checkdic):
		checked_word=[ocr_words[i],"1"]
	else:
		checked_word=[ocr_words[i],"0"]
	fulllist.append(checked_word)


s = codecs.open("checked_by_dic.txt","w+",encoding="utf-8" )

for k in range(0,len(fulllist)):
	s.write(fulllist[k][0]+" "+fulllist[k][1]+" ")

	