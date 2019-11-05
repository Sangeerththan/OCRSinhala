
import codecs


f = codecs.open("final.txt", encoding="utf-8")
lines = f.read().splitlines()


g = codecs.open("final2.txt", "w+", encoding="utf-8")


for i in range(0,len(lines)):
	print(i)
	split=lines[i].split()
	if(len(split)!=2):
		continue
	g.write(split[0]+" "+split[1]+"\n")
	