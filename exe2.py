# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exe2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from PyQt4.QtGui import QFileDialog
from matplotlib import pyplot as plt
from tkinter import *
from tkinter.ttk import *
import numpy as np
import cv2
import os.path

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_Form(object):

    def saveImage(self):
        
        fileName = QtGui.QFileDialog.getSaveFileName(None,'Save Image','','*.jpg')
        cv2.imwrite(fileName, Output_image)
        
        # if fileName:
        #  print (fileName)    
    
    def selectFile(self):
        global ImagePath
        ImagePath = QFileDialog.getOpenFileName()
        self.lineEdit.setText(ImagePath)
        
        global img_name  
       
        img_name = os.path.basename(ImagePath)

    def submitaction(self):
       

        img = cv2.imread(ImagePath)
        

        sub = "dermatological"

        if  sub in img_name:

            img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)

        img_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('image',img_grayscale)
        ret1,th1 = cv2.threshold(img_grayscale,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #cv2.imshow('Bin Image',th1)

       


        global Output_image

        combovalue1=self.comboBox.currentText()
        combovalue2=self.comboBox_2.currentText()
        
        if combovalue1=='Erosion'and combovalue2=='Square (5x5)':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
            Output_image = cv2.erode(th1,kernel,iterations = 1)
            #cv2.imshow('Erode image',Output_image)
            
        if combovalue1=='Erosion'and combovalue2=='Square (10x10)':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
            Output_image = cv2.erode(th1,kernel,iterations = 1)
            #cv2.imshow('Erode image',Output_image)

        if combovalue1=='Erosion'and combovalue2=='Cross (5x5)':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
            Output_image = cv2.erode(th1,kernel,iterations = 1)
            #cv2.imshow('Erode image',Output_image)

        if combovalue1=='Erosion'and combovalue2=='Cross (10x10)':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
            Output_image = cv2.erode(th1,kernel,iterations = 1)
            #cv2.imshow('Erode image',Output_image)
 #----------------------------------------------------------------------------
        if combovalue1=='Dilation'and combovalue2=='Square (5x5)':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
            Output_image = cv2.dilate(th1,kernel,iterations = 1)
            #cv2.imshow('dilate image',Output_image)
            
        if combovalue1=='Dilation'and combovalue2=='Square (10x10)':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
            Output_image = cv2.dilate(th1,kernel,iterations = 1)
            #cv2.imshow('dilate image',Output_image)

        if combovalue1=='Dilation'and combovalue2=='Cross (5x5)':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
            Output_image = cv2.dilate(th1,kernel,iterations = 1)
            #cv2.imshow('dilate image',Output_image)

        if combovalue1=='Dilation'and combovalue2=='Cross (10x10)':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
            Output_image = cv2.dilate(th1,kernel,iterations = 1)
            #cv2.imshow('dilate image',Output_image)
#----------------------------------------------------------------------------
        if combovalue1=='Closing'and combovalue2=='Square (5x5)':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
            Output_image = cv2.morphologyEx(th1,cv2.MORPH_CLOSE,kernel)
            #cv2.imshow('Closing image',Output_image)
            
        if combovalue1=='Closing'and combovalue2=='Square (10x10)':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
            Output_image = cv2.morphologyEx(th1,cv2.MORPH_CLOSE,kernel)
            #cv2.imshow('Closing image',Output_image)

        if combovalue1=='Closing'and combovalue2=='Cross (5x5)':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
            Output_image = cv2.morphologyEx(th1,cv2.MORPH_CLOSE,kernel)
            #cv2.imshow('Closing image',Output_image)

        if combovalue1=='Closing'and combovalue2=='Cross (10x10)':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
            Output_image = cv2.morphologyEx(th1,cv2.MORPH_CLOSE,kernel)
            #cv2.imshow('Closing image',Output_image)
#----------------------------------------------------------------------------
        if combovalue1=='Opening'and combovalue2=='Square (5x5)':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
            Output_image = cv2.morphologyEx(th1,cv2.MORPH_OPEN,kernel)
            #cv2.imshow('Opening image',Output_image)
            
        if combovalue1=='Opening'and combovalue2=='Square (10x10)':
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
            Output_image = cv2.morphologyEx(th1,cv2.MORPH_OPEN,kernel)
            #cv2.imshow('Opening image',Output_image)

        if combovalue1=='Opening'and combovalue2=='Cross (5x5)':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
            Output_image = cv2.morphologyEx(th1,cv2.MORPH_OPEN,kernel)
            #cv2.imshow('Opening image',Output_image)

        if combovalue1=='Opening'and combovalue2=='Cross (10x10)':
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
            Output_image = cv2.morphologyEx(th1,cv2.MORPH_OPEN,kernel)
            #cv2.imshow('Opening image',Output_image)
     




        #cv2.imshow('image',im)
        plt.subplot(221),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
        plt.axis("off")
        plt.subplot(222),plt.imshow(img_grayscale,'gray'), plt.title('Grayscale Image')
        plt.axis("off")
        plt.subplot(223),plt.imshow(th1,'gray'), plt.title('Binary Image')
        plt.axis("off")
        plt.subplot(224),plt.imshow(Output_image,'gray'), plt.title('final_image')
        plt.axis("off")
        plt.show()

#pushButton   -> browse image
#pushButton_2 -> submit
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(558, 339)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 2)
        
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.selectFile)

        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 2)
        
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.submitaction)

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 3)
        
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.saveImage)

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Browse image", None))
        self.label.setText(_translate("Form", "Please select a morfology operator", None))
        self.comboBox.setItemText(0, _translate("Form", "Erosion", None))
        self.comboBox.setItemText(1, _translate("Form", "Dilation", None))
        self.comboBox.setItemText(2, _translate("Form", "Opening", None))
        self.comboBox.setItemText(3, _translate("Form", "Closing", None))
        self.label_2.setText(_translate("Form", "Please select a structuring element", None))
        self.comboBox_2.setItemText(0, _translate("Form", "Square (5x5)", None))
        self.comboBox_2.setItemText(1, _translate("Form", "Square (10x10)", None))
        self.comboBox_2.setItemText(2, _translate("Form", "Cross (5x5)", None))
        self.comboBox_2.setItemText(3, _translate("Form", "Cross (10x10)", None))
        self.pushButton_2.setText(_translate("Form", "Submit", None))
        self.pushButton_3.setText(_translate("Form", "Save image", None))


def main():
        app = QtGui.QApplication(sys.argv)
        window = QtGui.QDialog() 
        ui = Ui_Form() 
        ui.setupUi(window) 
        window.show() 
        
        sys.exit(app.exec_()) 
if __name__ == "__main__": 
        main()

