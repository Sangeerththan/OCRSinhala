import codecs
import os

ab = ["ඒකාබද්ධ","ඒකාබද්ධ","ඒකාබද්ධ"]
fulllist=[["ඒකාබද්ධ",1]]

for n in range(730,864):
	if(os.path.isfile("Sinhala-source/Letters 5(S)-"+str(n)+".txt")):
		print("file "+str(n))
		f = codecs.open("Sinhala-source/Letters 5(S)-"+str(n)+".txt", encoding="utf-8")
		#f = codecs.open("Sinhala-source/test.txt", encoding="utf-8")
		lines = f.read().split()

		for i in range(0,len(lines)):
			isitinfulllist = False
			ischargood = True
			for j in range (0, len(lines[i])):
				if(ord(lines[i][j])<128):
					ischargood = False
					break
			if(ischargood):
				for k in range(0, len(fulllist)):
					if(lines[i]==fulllist[k][0]):
						fulllist[k][1] = fulllist[k][1]+1
						isitinfulllist = True
						break
				if(not isitinfulllist):
					fulllist.append([lines[i],1])		
			
#print(fulllist)	

g = codecs.open("freq_dic.txt","w+",encoding="utf-8" )

for m in range(0,len(fulllist)):
	g.write(fulllist[m][0]+" "+str(fulllist[m][1])+"\n")

 


