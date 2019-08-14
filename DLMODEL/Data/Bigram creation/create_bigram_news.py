import codecs

#3456 - 3526  akuru

#3527 - 3572 pillam

g = codecs.open("news.txt", encoding="utf-8")
lines = g.read().splitlines()
g.close()

fullbigram =[]

#line1 = lines[0]
#line1 = "මන්නාරම සමූහ මිනී වළේ අස්ථි ‍සාම්පල සම්බන්ධයෙන් ඇමෙරිකානු ෆ්ලෝරීඩා රසායනාගාරය ලබා දුන් දින වකවානු විමසීමේදී එකම මිනී වළ තුළින් හමුවූ අස්ථි සාම්පලවල කාලය"

for j in range(0,len(lines)):
	i=0
	while(True):
		count=0
		length=0
		print(length)
		
		try:
			while(count<2):
				if(ord(lines[j][i+length])>3455 and ord(lines[j][i+length])<3527):
					print("inn")
					count=count+1
					length=length+1
				else:
					print("out")
					length=length+1
				if(count==2):
					if(ord(lines[j][i+length])>3526 and ord(lines[j][i+length])<3573):
						length=length+1
				
			print("bigram element : "+lines[j][i:i+length])		
			fullbigram.append(lines[j][i:i+length])
			if(ord(lines[j][i+1])>3455 and ord(lines[j][i+1])<3527):
				i=i+1
			elif(ord(lines[j][i+1])>3526 and ord(lines[j][i+1])<3573 and ord(lines[j][i+2])==32):
				i=i+3
			else:
				i=i+2
				
		except:
			print("exception handling")
			break
				
		
		
		

print(fullbigram)

s = codecs.open("bigramnews.txt","w+",encoding="utf-8" )

for k in range(0,len(fullbigram)):
	s.write(fullbigram[k]+"\n")





