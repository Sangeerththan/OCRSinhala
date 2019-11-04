
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
def stringJoin(line):
    st = " "
    char_str = []
    for i in range(0,len(line),1):
        st.join(line[i])
        char_str.append(line[i])
    return st,char_str

con_string,con_list = stringJoin(lines)
str_l = str(con_list).split("\\r\\n")
def StringFormatted(con_string):
    print("character string:",con_string)
    print("character list is:",con_list)
    str_l = str(con_list).split("\\r\\n")
    str_latest =str(str_l).strip(", ")
    print(str_latest)
    #print(str_l)
    print("Length of charcter:",len(str_l))
    return str_latest

def refactorStr(stringInput):
    for i in range(0,len(stringInput),1):
        strings = stringInput[i]
        string1 = strings[0]
        string2 = strings[1]
        print("string is:\n",str(strings[len(strings)-2]),str(strings[len(strings)-1]))
print(refactorStr(str_l))

