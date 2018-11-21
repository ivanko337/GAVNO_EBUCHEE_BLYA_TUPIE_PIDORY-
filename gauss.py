#/usr/bin/env python3
#coding=utf-8

import sys
from gui_gauss import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from dragLabel import DragLabel
from MatrixAlghoritms import toTriangleShape
from MyMatrix import Matrix

class Test(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setuoUi(self)
		self.matrix = None
		self.matrixB = None
		self.matrixList = []
		self.systemArgumentLineEdits = [ [self.argument_lineEdit_11, self.argument_lineEdit_12, self.argument_lineEdit_13],
							[self.argument_lineEdit_21, self.argument_lineEdit_22, self.argument_lineEdit_23],
							[self.argument_lineEdit_31, self.argument_lineEdit_32, self.argument_lineEdit_33]]
		self.answerLineEdits = [ self.answer_LineEdit_1, self.answer_LineEdit_2, self.answer_LineEdit_3 ]

		self.systemArgumentLables = [self.argument_label_11, self.argument_label_12, self.argument_label_13, self.argument_label_21, self.argument_label_22, self.argument_label_23,
							self.argument_label_31, self.argument_label_32, self.argument_label_33]
		self.systemArgumentLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.systemArgumentLabels ]

		self.answerLabels = [self.answer_label_1, self.answer_label_2, self.answer_label_3]
		self.answerLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.answerLabels ]


		self.normalizeLineEdits()

	def normalizeLineEdits(self):
		for i in self.systemArgumentLineEdits:
			for j in i:
				j.raise_()
