#!/usr/bin/env python3
#coding=utf-8

from PyQt5 import QtCore, QtWidgets
from task import Ui_MainWindow
from cramer import Cramer
from gauss import Gauss

class App(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton_Cramer.clicked.connect(self.cramer)
		self.pushButton_Gauss.clicked.connect(self.gauss)

	def cramer(self):
		window = Cramer()
		window.show()

	def gauss(self):
		window = Gauss()
		window.show()

def __main__():
	app = QtWidgets.QApplication([])
	window = App()
	window.show()
	app.exec_()

if __name__ == '__main__':
	__main__()
