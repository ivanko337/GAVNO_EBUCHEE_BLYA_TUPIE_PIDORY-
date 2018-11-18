#!/usr/bin/env python3
#coding=utf-8

import sys
from first import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from dragLabel import DragLabel
from numpy.linalg import det
from MatrixAlghoritms import swapRowsL
from MyMatrix import Matrix

class Test(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, matrix, matrixB):
		super().__init__()
		self.setupUi(self)
		self.matrix = matrix
		self.matrixB = matrixB
		self.actionCounter = 0
		self.elementsGroups = []
		self.addFunctions = [self.addArgumentsHideLabels, self.addAnswerArgumentsHideLabels, self.addArgumentsLabels, self.addAnswersLabels, self.addMainDetArguments, self.addDet1AnswersLabel,
					self.addDet1ArgumentsLabels, self.addDet2AnswerLabel, self.addDet2ArgumentsLabels, self.addDet3AnswerLabels, self.addDet3ArgumentsLabels, self.test]
		self.addAll()
		self.startElementCoordinates = []
		self.moveHideElementsToNormalPlace()
		self.pushButton.clicked.connect(self.showMainDet)

	def addAll(self):
		for i in self.addFunctions:
			i()

	def addArgumentsHideLabels(self):
		res = []
		res.append(self.argument_label_11_hide); res.append(self.argument_label_12_hide); res.append(self.argument_label_13_hide)
		res.append(self.argument_label_21_hide); res.append(self.argument_label_22_hide); res.append(self.argument_label_23_hide)
		res.append(self.argument_label_31_hide); res.append(self.argument_label_32_hide); res.append(self.argument_label_33_hide)
		self.elementsGroups.append(res)

	def addAnswerArgumentsHideLabels(self):
		res = []
		res.append(self.answer_label_1_hide1); res.append(self.answer_label_1_hide2); res.append(self.answer_label_1_hide3); res.append(self.answer_label_2_hide1)
		res.append(self.answer_label_2_hide2); res.append(self.answer_label_2_hide3); res.append(self.answer_label_3_hide1); res.append(self.answer_label_3_hide2)
		res.append(self.answer_label_3_hide3); self.elementsGroups.append(res)

	def addArgumentsLabels(self):
		res = []
		res.append(self.argument_label_11); res.append(self.argument_label_12); res.append(self.argument_label_13)
		res.append(self.argument_label_21); res.append(self.argument_label_22); res.append(self.argument_label_23)
		res.append(self.argument_label_31); res.append(self.argument_label_32); res.append(self.argument_label_33)
		self.elementsGroups.append(res)

	def addMainDetArguments(self):
		res = []
		res.append(self.main_det_arg_11); res.append(self.main_det_arg_12); res.append(self.main_det_arg_13)
		res.append(self.main_det_arg_21); res.append(self.main_det_arg_22); res.append(self.main_det_arg_23)
		res.append(self.main_det_arg_31); res.append(self.main_det_arg_32); res.append(self.main_det_arg_33)
		self.elementsGroups.append(res)

	def addDet1AnswersLabel(self):
		res = []
		res.append(self.det1_answer_label_1)
		res.append(self.det1_answer_label_2)
		res.append(self.det1_answer_label_3)
		self.elementsGroups.append(res)

	def addDet1ArgumentsLabels(self):
		res = []
		res.append(self.det1_argument_12_label); res.append(self.det1_argument_13_label)
		res.append(self.det1_argument_22_label); res.append(self.det1_argument_23_label)
		res.append(self.det1_argument_32_label); res.append(self.det1_argument_33_label)
		self.elementsGroups.append(res)

	def addDet2AnswerLabel(self):
		res = []
		res.append(self.det2_answer_label_1)
		res.append(self.det2_answer_label_2)
		res.append(self.det2_answer_label_3)
		self.elementsGroups.append(res)

	def addDet2ArgumentsLabels(self):
		res = []
		res.append(self.det2_argument_11_label); res.append(self.det2_argument_13_label)
		res.append(self.det2_argument_21_label); res.append(self.det2_argument_23_label)
		res.append(self.det2_argument_31_label); res.append(self.det2_argument_33_label)
		self.elementsGroups.append(res)

	def addDet3AnswerLabels(self):
		res = []
		res.append(self.det3_answer_label_1)
		res.append(self.det3_answer_label_2)
		res.append(self.det3_answer_label_3)
		self.elementsGroups.append(res)

	def addDet3ArgumentsLabels(self):
		res = []
		res.append(self.det3_argument_11_label); res.append(self.det3_argument_12_label)
		res.append(self.det3_argument_21_label); res.append(self.det3_argument_22_label)
		res.append(self.det3_argument_31_label); res.append(self.det3_argument_32_label)
		self.elementsGroups.append(res)

	def addAnswersLabels(self):
		res = []
		res.append(self.answer_label_1); res.append(self.answer_label_2); res.append(self.answer_label_3)
		self.elementsGroups.append(res)

	def showMainDet(self):
		res = det(self.matrix)
		self.main_det_label.setText(str(res))

	def showDet1(self):
		matr = swapRowsL(self.matrix, 0, self.matrixB)
		res = det(matr)
		self.det_1_label.setText(str(res))

	def showDet2(self):
		matr = swapRowsL(self.matrix, 1, self.matrixB)
		res = det(matr)
		self.det_2_label.setText(str(res))

	def showDet3(self):
		matr = swapRowsL(self.matrix, 2, self.matrixB)
		res = det(matr)
		self.set_3_label.setText(str(res))

	def test(self):
		print(type(self.centralwidget))

	def moveHideElementsToNormalPlace(self):
		for i in self.elementsGroups:
			for j in i:
				name = j.objectName()
				if name.find('hide') != -1 or name.find('det') != -1:
					self.startElementCoordinates.append((j.objectName(), j.pos().x(), j.pos().y()))
					j.move(5000, 5000)

def __main__():
	app = QtWidgets.QApplication(sys.argv)
	window = Test(Matrix([[5, 1, 2], [4, 3, 6], [12, 23, 18]]), Matrix([77, 132, 536]))
	window.show()
	app.exec_()

if __name__ == '__main__':
	__main__()
