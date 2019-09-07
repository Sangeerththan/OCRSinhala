import codecs

f = codecs.open("confusions.txt", encoding="utf-8")
ocrConfusions = f.read().split("\r\n")
f.close

g = codecs.open("dic.txt", encoding="utf-8")
dic_words = g.read().split()
g.close

confusionList =[]
for x in ocrConfusions:
    oneLine=[]
    line = x.split("\t")

    confusionList.append(line)
    
print(confusionList)        
    
