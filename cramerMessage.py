#!/usr/bin/env python3
#coding=utf-8

from PyQt5 import QtWidgets, QtCore
from messageCramerMainDetIsZero import Ui_Dialog

class MainDetIsZero(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_close.clicked.connect(parent.close)