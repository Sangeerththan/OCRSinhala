# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\FYP\emeres-ui\emeresOcrUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import os , re , cv2 , pytesseract, codecs, difflib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import  QIcon, QPixmap, QColor


class Ui_MainWindow(object):

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1080)
        MainWindow.setStyleSheet("QMainWindow#MainWindow\n"
"{\n"
"    /*background-image: ;*/\n"
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
        MainWindow.setStyleSheet( "#MainWindow {background-image: url(horse-with-sinhala-letters.png)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonGetImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGetImage.setGeometry(QtCore.QRect(190, 682, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonGetImage.setFont(font)
        self.buttonGetImage.setObjectName("buttonGetImage")
        self.buttonGenerateWordFrequency = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGenerateWordFrequency.setGeometry(QtCore.QRect(610, 682, 130, 40))
        self.buttonGenerateWordFrequency.setText("Generate Frequency List")
        font = QtGui.QFont()
        font.setPointSize(7)
        self.buttonGenerateWordFrequency.setFont(font)
        self.buttonGenerateWordFrequency.setObjectName("buttonGenerateWordFrequency")
        
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(190, 30, 550, 630))
        self.labelImage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.buttonExtractText = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtractText.setGeometry(QtCore.QRect(25, 130, 130, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonExtractText.setFont(font)
        self.buttonExtractText.setIconSize(QtCore.QSize(16, 16))
        self.buttonExtractText.setObjectName("buttonExtractText")
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setGeometry(QtCore.QRect(782, 682, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonClear.setFont(font)
        self.buttonClear.setObjectName("buttonClear")
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(1202, 682, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(782, 30, 550, 630))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.buttonExtractText_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtractText_2.setGeometry(QtCore.QRect(25, 270, 130, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buttonExtractText_2.setFont(font)
        self.buttonExtractText_2.setObjectName("buttonExtractText_2")
        self.buttonExtractText_3 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExtractText_3.setGeometry(QtCore.QRect(25, 410, 130, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
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
        self.buttonGenerateWordFrequency.clicked.connect(self.generateWordFrequency)
        self.buttonExtractText.clicked.connect(self.extractText)
        self.buttonExtractText_2.clicked.connect(self.extractText_2) 
        self.buttonExtractText.setEnabled(False)
        self.buttonExtractText_2.setEnabled(False)
        self.buttonClear.clicked.connect(self.clearText) 
        self.buttonSave.clicked.connect(self.saveText) 
        self.buttonExtractText_3.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Optical Character Recognition"))
        self.buttonGetImage.setText(_translate("MainWindow", "Load Image"))
        self.buttonExtractText.setText(_translate("MainWindow", "Tesseract \n+ \nDictionary Match"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.buttonSave.setText(_translate("MainWindow", "Save"))
        self.buttonExtractText_2.setText(_translate("MainWindow", "Nearest Match"))
        self.buttonExtractText_3.setText(_translate("MainWindow", "EMERES Model"))

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

    def setImage(self, fileName):
        pixmap =QPixmap(fileName)
        pixmap2 = pixmap.scaledToWidth(600)
        self.labelImage.setPixmap(pixmap2)    
        self.buttonExtractText.setEnabled(True)
        self.buttonExtractText_2.setEnabled(True)
        #self.buttonExtractText_3.setEnabled(True)
    def extractText(self):
        self.textEdit.clear()        
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
        print (fulllist)    

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

        def my_max_by_weight(sequence):
            if not sequence:
                raise ValueError('empty sequence')

            maximum = sequence[0]

            for item in sequence:
                # Compare elements by their weight stored
                # in their second element.
                if item[2] > maximum[2]:
                    maximum = item

            return maximum 

        #confusionCharacs = [අ,ඉ,උ,එ,ඔ,ක,ඛ,ග,ඝ,ච,ඡ,ජ,ට,ඨ,ඩ,ඪ,ත,ථ,ද,ධ,ප,ඵ,බ,භ,ය,ර,ල,ව,ශ,ෂ,ස,හ, ෆ,න,ණ,ඥ, ං]
        confusionMatrix =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.06666666666666667,0,0,0,0,0,0,0,0,0,0,0.13333333333333333,0,0,0,0,0.6666666666666666,0,0,0.06666666666666667,0,0,0.06666666666666667],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.03571428571428571,0,0.8928571428571429,0,0,0,0,0,0,0,0,0.03571428571428571,0,0,0,0,0,0,0,0,0.03571428571428571],[0,0,0,0,0,0,0,0,0,0.3333333333333333,0,0,0,0,0,0,0.3333333333333333,0,0,0,0,0,0,0.16666666666666666,0,0,0,0,0,0,0,0,0,0.16666666666666666,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0.0023094688221709007,0,0,0,0,0.009237875288683603,0,0.011547344110854504,0,0.009237875288683603,0,0.004618937644341801,0,0.0023094688221709007,0,0,0,0.628175519630485,0.09468822170900693,0.025404157043879907,0.09237875288683603,0.016166281755196306,0.0023094688221709007,0.03926096997690531,0.023094688221709007,0,0.02771362586605081,0.004618937644341801,0,0.006928406466512702],[0,0,0,0,0,0.075,0,0,0,0,0,0,0,0,0.05,0,0,0,0.025,0.125,0,0,0.625,0,0,0,0,0.025,0,0,0.025,0,0,0.025,0,0,0.025],[0,0.0410958904109589,0,0,0,0.1232876712328767,0,0,0,0,0,0,0.0136986301369863,0,0,0,0.2054794520547945,0,0,0,0.0136986301369863,0,0,0,0.0684931506849315,0.0684931506849315,0.0136986301369863,0.0547945205479452,0.1232876712328767,0,0.0136986301369863,0.0547945205479452,0.0136986301369863,0.0821917808219178,0,0,0.1095890410958904],[0,0,0,0,0,0.0028735632183908046,0,0,0,0,0,0,0,0,0,0,0.005747126436781609,0,0.0028735632183908046,0,0,0,0,0,0.031609195402298854,0.06896551724137931,0.0028735632183908046,0.008620689655172414,0,0.0028735632183908046,0.8591954022988506,0.0028735632183908046,0,0,0,0.005747126436781609,0.005747126436781609],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.027777777777777776,0,0,0,0,0,0,0,0.027777777777777776,0,0.027777777777777776,0.4444444444444444,0,0.3055555555555556,0,0,0.05555555555555555,0,0,0,0,0,0.1111111111111111],[0,0,0,0,0,0,0,0.017391304347826087,0,0,0,0.008695652173913044,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.017391304347826087,0,0.02608695652173913,0.008695652173913044,0,0.9217391304347826,0,0,0,0,0],[0,0,0,0,0,0.02830188679245283,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.8301886792452831,0,0,0,0.009433962264150943,0.07547169811320754,0.009433962264150943,0.009433962264150943,0,0,0,0,0,0.018867924528301886,0.009433962264150943,0,0.009433962264150943],[0,0,0,0,0,0.09302325581395349,0,0,0,0.023255813953488372,0,0,0,0,0,0,0.06976744186046512,0,0.023255813953488372,0,0.11627906976744186,0,0,0,0.3488372093023256,0,0.09302325581395349,0.13953488372093023,0,0,0,0,0,0.06976744186046512,0.023255813953488372,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.9230769230769231,0,0.07692307692307693,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.06896551724137931,0,0.06896551724137931,0,0,0,0,0,0,0,0,0,0,0.06896551724137931,0.1724137931034483,0,0,0.034482758620689655,0,0,0.06896551724137931,0.06896551724137931,0.06896551724137931,0,0,0,0,0,0.3793103448275862,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0,0.2,0,0,0.2,0,0,0,0,0,0],[0,0,0.3333333333333333,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.3333333333333333,0,0,0,0,0,0,0.3333333333333333,0,0,0,0,0,0,0,0,0,0,0],[0,0,0.0017574692442882249,0,0,0.008787346221441126,0,0,0,0,0,0,0,0,0.0017574692442882249,0,0.005272407732864675,0,0,0,0.0017574692442882249,0,0,0,0.005272407732864675,0.022847100175746926,0.0017574692442882249,0.008787346221441126,0.0017574692442882249,0,0.9226713532513181,0.01054481546572935,0,0.005272407732864675,0.0017574692442882249,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0.07692307692307693,0.07692307692307693,0,0,0,0.07692307692307693,0,0,0,0,0,0,0.15384615384615385,0.6153846153846154,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.02857142857142857,0,0,0,0,0,0,0.05714285714285714,0,0,0,0.22857142857142856,0,0.11428571428571428,0,0,0,0,0,0.05714285714285714,0.3142857142857143,0.11428571428571428,0.02857142857142857,0,0,0.02857142857142857,0,0,0.02857142857142857,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0.030303030303030304,0,0,0,0,0,0.9393939393939394,0.030303030303030304,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0.1111111111111111,0,0,0,0,0,0,0,0,0,0,0,0,0.05555555555555555,0,0.05555555555555555,0,0,0,0,0.4444444444444444,0.05555555555555555,0,0,0,0.2222222222222222,0,0,0.05555555555555555,0,0,0],[0,0,0,0,0,0.02564102564102564,0,0,0,0,0,0,0,0,0.02564102564102564,0,0,0,0,0,0,0,0,0,0.02564102564102564,0.28205128205128205,0,0.02564102564102564,0.02564102564102564,0,0,0.5897435897435898,0,0,0,0,0],[0,0,0,0,0,0.09824561403508772,0.005263157894736842,0.017543859649122806,0,0.005263157894736842,0,0.0017543859649122807,0.043859649122807015,0,0.005263157894736842,0,0.04736842105263158,0.014035087719298246,0.05964912280701754,0.007017543859649123,0.01929824561403509,0,0.007017543859649123,0.007017543859649123,0,0.20175438596491227,0.043859649122807015,0.10526315789473684,0.02456140350877193,0.0017543859649122807,0.014035087719298246,0.04035087719298246,0,0.1280701754385965,0.0824561403508772,0.014035087719298246,0.005263157894736842],[0,0,0.16158536585365854,0,0,0.10365853658536585,0,0.009146341463414634,0,0.003048780487804878,0,0,0.036585365853658534,0,0.003048780487804878,0,0.01524390243902439,0,0.21646341463414634,0,0.021341463414634148,0,0.003048780487804878,0,0.039634146341463415,0,0.03048780487804878,0.11890243902439024,0.1524390243902439,0.012195121951219513,0.042682926829268296,0,0,0.012195121951219513,0.01524390243902439,0,0.003048780487804878],[0,0,0,0,0,0.05945945945945946,0,0.02702702702702703,0.005405405405405406,0.043243243243243246,0,0,0.021621621621621623,0,0.010810810810810811,0,0.05405405405405406,0.005405405405405406,0.02702702702702703,0,0.02702702702702703,0.032432432432432434,0.02702702702702703,0,0.10810810810810811,0.032432432432432434,0,0.2972972972972973,0,0.005405405405405406,0.12432432432432433,0.032432432432432434,0.005405405405405406,0.05405405405405406,0,0,0],[0,0.005263157894736842,0,0,0,0.042105263157894736,0,0.021052631578947368,0,0.010526315789473684,0,0.005263157894736842,0.11578947368421053,0,0.010526315789473684,0,0.05263157894736842,0.005263157894736842,0.042105263157894736,0.005263157894736842,0.03684210526315789,0,0,0.02631578947368421,0.22105263157894736,0.19473684210526315,0.02631578947368421,0,0.010526315789473684,0.010526315789473684,0.04736842105263158,0.010526315789473684,0,0.05789473684210526,0.03684210526315789,0.005263157894736842,0],[0,0,0,0,0,0.05172413793103448,0,0.1206896551724138,0,0,0,0,0,0,0,0,0.05172413793103448,0,0.017241379310344827,0,0,0,0,0,0.1724137931034483,0.27586206896551724,0,0.017241379310344827,0,0.017241379310344827,0,0,0,0,0.05172413793103448,0.08620689655172414,0.13793103448275862],[0,0,0,0,0,0.05555555555555555,0,0,0,0,0.05555555555555555,0,0,0,0,0,0.05555555555555555,0,0,0,0.05555555555555555,0,0,0,0.05555555555555555,0,0.3333333333333333,0,0,0,0.1111111111111111,0.16666666666666666,0,0,0.1111111111111111,0,0],[0,0,0,0,0,0.03225806451612903,0.03225806451612903,0,0,0,0,0,0,0,0,0,0,0,0.03225806451612903,0,0,0,0,0,0.16129032258064516,0.41935483870967744,0,0.1935483870967742,0,0,0,0,0,0.03225806451612903,0,0,0.0967741935483871],[0,0.022988505747126436,0,0,0,0.08045977011494253,0,0,0,0,0,0,0,0,0.011494252873563218,0,0.10344827586206896,0,0.011494252873563218,0,0,0,0,0.011494252873563218,0,0.5517241379310345,0.011494252873563218,0.022988505747126436,0,0.05747126436781609,0.034482758620689655,0,0,0.011494252873563218,0,0,0.06896551724137931],[0,0,0,0,0,0.3333333333333333,0,0,0,0,0,0,0.3333333333333333,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.3333333333333333,0,0,0,0,0],[0,0.00011235955056179776,0.00011235955056179776,0,0,0.011235955056179775,0.00022471910112359551,0.0017977528089887641,0,0.00011235955056179776,0,0.0005617977528089888,0.0035955056179775282,0,0.00033707865168539324,0,0.9274157303370787,0,0.0005617977528089888,0.00033707865168539324,0.0029213483146067415,0,0.0005617977528089888,0,0.023707865168539326,0.011235955056179775,0.0012359550561797752,0.008314606741573034,0.0012359550561797752,0.0005617977528089888,0.001348314606741573,0.0007865168539325843,0,0,0.0016853932584269663,0,0],[0,0,0,0,0,0.015776699029126214,0,0.0012135922330097086,0.012135922330097087,0.012135922330097087,0,0,0,0,0,0,0.01699029126213592,0,0,0,0.0012135922330097086,0,0.0048543689320388345,0,0.009708737864077669,0.02063106796116505,0.0036407766990291263,0.014563106796116505,0.0036407766990291263,0,0.4441747572815534,0.015776699029126214,0,0.4223300970873786,0,0.0012135922330097086,0],[0,0,0,0,0,0,0,0.006289308176100629,0,0,0,0.006289308176100629,0.006289308176100629,0,0,0,0.012578616352201259,0,0,0,0,0,0,0.012578616352201259,0.03773584905660377,0.031446540880503145,0,0.025157232704402517,0,0,0.8364779874213837,0.018867924528301886,0,0.006289308176100629,0,0,0],[0,0,0,0,0,0.125,0.25,0.06944444444444445,0,0,0,0,0.013888888888888888,0,0.013888888888888888,0,0.06944444444444445,0,0.06944444444444445,0,0.041666666666666664,0,0,0,0.09722222222222222,0.041666666666666664,0.027777777777777776,0.05555555555555555,0.013888888888888888,0,0.05555555555555555,0.027777777777777776,0,0.027777777777777776,0,0,0]]
        self.textEdit.clear()
        config = ('-l sin --oem 0 --psm 3')
        img = cv2.imread(self.fileName, cv2.IMREAD_COLOR)
        # Run tesseract OCR on image
        text = pytesseract.image_to_string(img, config=config)

        ocr_words = text.split()
        g = codecs.open("dic.txt", encoding="utf-8")
        dic_words = g.read().split()
        g.close
        
        fulllist = []

        #Create fequency list
        frequencyList = []
        if(os.path.isfile("freq_dic.txt")):
            f = codecs.open("freq_dic.txt", encoding="utf-8")
            lines = f.read().splitlines()
        #print(lines)
            for i in range(0,len(lines)):
                wordElement = lines[i].split()
                frequencyList.append(wordElement)    
            #print("Frequency List ",frequencyList)

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

        u = codecs.open("conf_characters.txt", encoding="utf-8-sig")
        confusionList = u.read().split()
        print(confusionList)
        for i in range(0,len(fulllist)):
            
            redColor = QColor(255,0,0)
            greenColor = QColor(0,128,0)
            blackColor = QColor(0,0,0)

            if (fulllist[i][1] == "0"):
                found = difflib.get_close_matches(fulllist[i][0],dic_words)
                ocrWord = fulllist[i][0]
                print(ocrWord)
                

                '''for c in range(0,len(ocrWord)):
                    
                    newOcrWord =ocrWord

                    if ocrWord[c] in confusionList:
                        indexElement = confusionList.index(ocrWord[c])
                        highestElement = max(confusionMatrix[indexElement])
                        print(highestElement)
                        
                        bestReplacementIndex = confusionMatrix[indexElement].index(highestElement)
                        print(bestReplacementIndex)
                        bestReplacement = confusionList[bestReplacementIndex]
                        newOcrWord.replace(newOcrWord[c],bestReplacement)
                        
                        checkdicNew = False
                        new_checked_word = []
                        for l in range(0, len(dic_words)):
                            if(newOcrWord == dic_words[l]):
                                checkdicNew = True
                                break
                        if(checkdicNew):
                            new_checked_word = [newOcrWord, "1"]
                            fulllist[i] =new_checked_word
                        else:
                            new_checked_word = [newOcrWord, "0"]
                        print(newOcrWord)
                '''        
                #fulllist.remove(fulllist[i])
                #fulllist[i] =new_checked_word                       


                ocrConfusionData = []
                newOcrWord =ocrWord
                for d in range(0,len(ocrWord)):

                    
                    

                    if ocrWord[d] in confusionList:
                        ocrConfusionDataElement = [ocrWord[d]]

                        indexElement = confusionList.index(ocrWord[d])
                        highestElement = max(confusionMatrix[indexElement])
                        print(highestElement)
                        
                        bestReplacementIndex = confusionMatrix[indexElement].index(highestElement)
                        print(bestReplacementIndex)
                        bestReplacement = confusionList[bestReplacementIndex]
                        ocrConfusionDataElement.append(bestReplacement)
                        ocrConfusionDataElement.append(highestElement)

                        ocrConfusionData.append(ocrConfusionDataElement)
                print(ocrConfusionData)

                #for e in range(0,len(ocrConfusionData)):

                
                if(len(ocrConfusionData)>0):
                    maxOcrConfusionElement = my_max_by_weight(ocrConfusionData)
                    print ("Max confusion elemenet: ", maxOcrConfusionElement)
                    newOcrWord.replace(maxOcrConfusionElement[0], maxOcrConfusionElement[1])
                    checkdicNew = False
                    new_checked_word = []
                    for l in range(0, len(dic_words)):
                        if(newOcrWord == dic_words[l]):
                            checkdicNew = True
                            break
                    if(checkdicNew):
                        new_checked_word = [newOcrWord, "1"]
                        fulllist[i] =new_checked_word
                    else:
                        new_checked_word = [newOcrWord, "0"]
                    print("Revised matrix output: ", newOcrWord)

                
                print("Found List ",found)
                
                if (len(found)>0):
                    self.textEdit.setTextColor(greenColor)
                    matchedList=[]
                    for p in range(0,len(found)):
                        for q in range(0,len(frequencyList)):
                            if (found[p] == frequencyList[q][0]):
                                matchedList.append(frequencyList[q])

                    print("Matched List ",matchedList)

                    if (len(matchedList)==0):
                        self.textEdit.insertPlainText(found[0]+" ")
                    else:
                        maxElement = [matchedList[0]]
                        for r in range(1,len(matchedList)):
                            if(int(maxElement[0][1]) < int(matchedList[r][1])):
                                maxElement[0] = matchedList[r]
                        print("Max Element ",maxElement)
                        self.textEdit.insertPlainText(maxElement[0][0]+ " ")

                                                         
                else:
                    self.textEdit.setTextColor(blackColor)
                    self.textEdit.insertPlainText(fulllist[i][0]+" ")
                
            else:
                self.textEdit.setTextColor(blackColor)
                self.textEdit.insertPlainText(fulllist[i][0]+" ")
        #self.textEdit.append(fulllist)

    def generateWordFrequency(self):
        fulllist=[["ඒකාබද්ධ",1]]

        for n in range(730,864):
            if(os.path.isfile("Sinhala-source/Letters 5(S)-"+str(n)+".txt")):
                #print("file "+str(n))
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
