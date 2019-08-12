import codecs
import difflib

g = codecs.open("dic.txt", encoding="utf-8")
dic_words = g.read().split()
g.close

found = difflib.get_close_matches("කදෑර්යාල",dic_words)

s = codecs.open("found_words.txt","w+",encoding="utf-8" )

for i in range(0,len(found)):
	s.write(found[i]+"\n")

s.close