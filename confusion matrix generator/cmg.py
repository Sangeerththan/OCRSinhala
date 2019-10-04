import pytesseract
from PIL import Image
import glob
import codecs
import math
import numpy

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

mylist = [f for f in glob.glob("images/*")]

f = codecs.open("conf_characters.txt", encoding="utf-8")
confusion_list = f.read().splitlines()
config = ('-l sin --oem 1 --psm 3')

g = codecs.open("cmgText.txt", "w+", encoding="utf-8")


ocr = []
correct = []

confusionPairMatrix = []
for s in range(0, len(confusion_list)):
    confusionPairMatrixline = []
    for p in range(0, len(confusion_list)):
        confusionPairMatrixline.append(0)
    confusionPairMatrix.append(confusionPairMatrixline)

confusionProbabilityPairMatrix = []
for s in range(0, len(confusion_list)):
    confusionProbabilityPairMatrixline = []
    for p in range(0, len(confusion_list)):
        confusionProbabilityPairMatrixline.append(0)
    confusionProbabilityPairMatrix.append(confusionProbabilityPairMatrixline)


for i in range(0, len(mylist)):
    correct.append(mylist[i][7:-4])
    text = pytesseract.image_to_string(Image.open(mylist[i]), config=config)
    ocr.append(text)

for j in range(0, len(ocr)):
    if(len(ocr[j]) == len(correct[j])):
        for k in range(0, len(ocr[j])):
            if ((ocr[j][k] != correct[j][k]) & (ocr[j][k] in confusion_list) & (correct[j][k] in confusion_list)):
                ocrIndex = confusion_list.index(ocr[j][k])
                correctIndex = confusion_list.index(correct[j][k])
                g.write(ocr[j])
                g.write(correct[j-1])
                g.write("/n")
                g.write(ocr[j][k])
                g.write(correct[j][k])
                confusionPairMatrix[ocrIndex][correctIndex] = confusionPairMatrix[ocrIndex][correctIndex]+1
                print("OCR index: ", ocrIndex)
                print("Corrected index: ", correctIndex)

print("Confusion Pair Matrix: ", confusionPairMatrix)

for a in range(0, len(confusionPairMatrix)):
    subSum = 0
    for b in range(0, len(confusionPairMatrix)):
        subSum += confusionPairMatrix[a][b]
    for c in range(0, len(confusionPairMatrix)):
        if ((confusionPairMatrix[a][c]) != 0):
            confusionProbabilityPairMatrix[a][c] = confusionPairMatrix[a][c]/subSum

print("Confusion Probability Pair Matrix: ", confusionProbabilityPairMatrix)


for i in range(0, len(ocr)):
    g.write(ocr[i]+"-")
    g.write(correct[i]+"\n")

g.write(ocr[0][1])
#g = codecs.open("cmgText.txt","w+",encoding="utf-8" )
# g.write(correct[0])
