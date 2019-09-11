import codecs

g = codecs.open("dic.txt", encoding="utf-8")
dic_words = g.read().split()
g.close

confuse_groups=[]
with codecs.open("confusion groups.txt", encoding="utf-8") as f:
    confuse_groups = f.readlines()
f.close()

confuse_list=[]
for i in range(0,len(confuse_groups)):
	confuse_list.append(confuse_groups[i].split())
	

g = codecs.open("text.txt", encoding="utf-8")
word = g.read()
g.close


s = codecs.open("corrected.txt","w+",encoding="utf-8" )
if (word in dic_words):
	print("true")
	s.write(word)
else:
	print("false")
	correct_word=word
	found_correct_word = False
	for j in range(0,len(word)):	
		for k in range(0,len(confuse_list)):
			if(word[j] in confuse_list[k]):
				for m in range(0,len(confuse_list[k])):
					if(word[0:j]+confuse_list[k][m]+word[j+1:] in dic_words):
						correct_word=word[0:j]+confuse_list[k][m]+word[j+1:]
						found_correct_word = True
						break
			if(found_correct_word):
				break
		if(found_correct_word):
			break
	s.write(correct_word)



s.close()



