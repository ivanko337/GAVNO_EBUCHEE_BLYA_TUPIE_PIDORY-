# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messageCramerMainDetIsZero.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 184)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 341, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setGeometry(QtCore.QRect(230, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Определитель равен нулю"))
        self.label.setText(_translate("Dialog", "Определитель основной\n"
"матрицы равен нулю.\n"
"Решение методом Красмера\n"
"невозможно."))
        self.pushButton_close.setText(_translate("Dialog", "Ок"))

