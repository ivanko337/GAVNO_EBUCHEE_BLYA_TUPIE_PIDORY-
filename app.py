#!/usr/bin/env python3
#coding=utf-8

from PyQt5 import QtCore, QtWidgets
from task import Ui_MainWindow
from cramer import Cramer
from gauss import Gauss
from matrixMethod import MatrixMethod

class App(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.cramerM = Cramer()
		self.gaussM  = Gauss()
		self.matrix  = MatrixMethod()
		self.pushButton_Cramer.clicked.connect(self.cramer)
		self.pushButton_Gauss.clicked.connect(self.gauss)
		self.pushButton_Matrix.clicked.connect(self.matrixM)

	def cramer(self):
		self.cramerM.close()
		self.cramerM = Cramer()
		self.cramerM.show()

	def gauss(self):
		self.gaussM.close()
		self.gaussM = Gauss()
		self.gaussM.show()

	def matrixM(self):
		self.matrix.close()
		self.matrix = MatrixMethod()
		self.matrix.show()

def __main__():
	app = QtWidgets.QApplication([])
	window = App()
	window.show()
	app.exec_()

if __name__ == '__main__':
	__main__()