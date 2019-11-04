
import codecs
import os

global line
file = codecs.open("../../generate-images-java/characterGenerator/characters.txt","r", encoding="utf-8")
print("Success")
#print(len(file.readlines()))
st = " "
lines = file.readlines()
linesStr = str(lines)
print(linesStr)
st.join(lines)
