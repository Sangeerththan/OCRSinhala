# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FYP\emeres-ui\emeresOcrUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import os , re , cv2 , pytesseract, codecs, difflib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import  QIcon ,QPixmap, QColor


class Ui_MainWindow(object):

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 800)
        MainWindow.setStyleSheet("QMainWindow#MainWindow\n"
"{\n"
"    background-color:rgb(72,164,136);\n"
"    /*background-image: url(\'H:/Github/PythonScripts/PyQtDesigner/WebScrapper/bg.png\');*/\n"
"     background-position: center; /* Center the image */\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel\n"
"{    \n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    border-color: black;\n"
"      border-width: 1px 1px 1px 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonGetImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetImage.setGeometry(QtCore.QRect(490, 610, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonGetImage.setFont(font)
        self.buttonGetImage.setObjectName("buttonGetImage")
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(250, 50, 600, 480))
        self.labelImage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.buttonExtractText = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtractText.setGeometry(QtCore.QRect(30, 130, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.buttonExtractText.setFont(font)
        self.buttonExtractText.setIconSize(QtCore.QSize(16, 16))
        self.buttonExtractText.setObjectName("buttonExtractText")
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setGeometry(QtCore.QRect(930, 610, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonClear.setFont(font)
        self.buttonClear.setObjectName("buttonClear")
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(1200, 610, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(930, 50, 400, 480))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.buttonExtractText_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtractText_2.setGeometry(QtCore.QRect(30, 270, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.buttonExtractText_2.setFont(font)
        self.buttonExtractText_2.setObjectName("buttonExtractText_2")
        self.buttonExtractText_3 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtractText_3.setGeometry(QtCore.QRect(30, 410, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.buttonExtractText_3.setFont(font)
        self.buttonExtractText_3.setObjectName("buttonExtractText_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1490, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.buttonGetImage.clicked.connect(self.getImage)
        self.buttonExtractText.clicked.connect(self.extractText)
        self.buttonExtractText_2.clicked.connect(self.extractText_2) 
        self.buttonExtractText.setEnabled(False)
        self.buttonClear.clicked.connect(self.clearText) 
        self.buttonSave.clicked.connect(self.saveText) 

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Optical Character Recognition"))
        self.buttonGetImage.setText(_translate("MainWindow", "Load Image"))
        self.buttonExtractText.setText(_translate("MainWindow", "Extract text (Tesseract + Dictionary Match)"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.buttonSave.setText(_translate("MainWindow", "Save"))
        self.buttonExtractText_2.setText(_translate("MainWindow", "Extract text ( Nearest Dictionalry Match)"))
        self.buttonExtractText_3.setText(_translate("MainWindow", "Extract text ( EMERES Model)"))

    def getImage(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(options=options)
        # self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open a image", "","All Files (*);;Image Files (*.jpg);;Image Files (*.png)", options=options)
        if self.fileName:
            print(self.fileName)
            pattern = ".(jpg|png|jpeg|bmp|jpe|tiff|JPG)$"
            if re.search(pattern,self.fileName):
                self.setImage(self.fileName)

    def setImage(self,fileName):
        self.labelImage.setPixmap(QPixmap(fileName))
        self.buttonExtractText.setEnabled(True)

    def extractText(self):
        config = ('-l sin --oem 0 --psm 3')
        img = cv2.imread(self.fileName, cv2.IMREAD_COLOR)
        # Run tesseract OCR on image
        text = pytesseract.image_to_string(img, config=config)

        ocr_words = text.split()
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
            

        # Print recognized text
        for i in range(0,len(fulllist)):
            
            redColor = QColor(255,0,0)
            blackColor = QColor(0,0,0)

            if (fulllist[i][1] == "0"):
                self.textEdit.setTextColor(redColor)
                self.textEdit.insertPlainText(fulllist[i][0]+" ")
                
            else:
                self.textEdit.setTextColor(blackColor)
                self.textEdit.insertPlainText(fulllist[i][0]+" ")
        #self.textEdit.append(fulllist)

    def extractText_2(self):

        config = ('-l sin --oem 0 --psm 3')
        img = cv2.imread(self.fileName, cv2.IMREAD_COLOR)
        # Run tesseract OCR on image
        text = pytesseract.image_to_string(img, config=config)

        ocr_words = text.split()
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
            

        # Print recognized text
        for i in range(0,len(fulllist)):
            
            redColor = QColor(255,0,0)
            greenColor = QColor(0,128,0)
            blackColor = QColor(0,0,0)

            if (fulllist[i][1] == "0"):
                found = difflib.get_close_matches(fulllist[i][0],dic_words)
                print(found)
                
                if (len(found)>0):
                    self.textEdit.setTextColor(greenColor)
                    self.textEdit.insertPlainText(found[0]+" ")
                else:
                    self.textEdit.setTextColor(blackColor)
                    self.textEdit.insertPlainText(fulllist[i][0]+" ")
                
            else:
                self.textEdit.setTextColor(blackColor)
                self.textEdit.insertPlainText(fulllist[i][0]+" ")
        #self.textEdit.append(fulllist)

    def clearText(self):
        self.textEdit.clear()

    def saveText(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        # fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Save text","All Files (*);;Text Files (*.txt)", options=options)
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(options=options)
        if fileName:
            print(fileName)
            file = open(fileName,'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())