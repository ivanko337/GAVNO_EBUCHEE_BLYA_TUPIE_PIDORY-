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
		self.count = 0
		self.matrix = matrix
		self.matrixB = matrixB
		self.mainDet = None
		self.det1 = None
		self.det2 = None
		self.det3 = None
		self.systemArgumentLabels = [self.argument_label_11, self.argument_label_12, self.argument_label_13, self.argument_label_21, self.argument_label_22, self.argument_label_23,
						self.argument_label_31, self.argument_label_32, self.argument_label_33]
		self.systemArgumentLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.systemArgumentLabels ]

		self.answerLabels = [self.answer_label_1, self.answer_label_2, self.answer_label_3]
		self.answerLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.answerLabels ]

		self.mainDetArgLabels  = [self.main_det_arg_11, self.main_det_arg_12, self.main_det_arg_13, self.main_det_arg_21, self.main_det_arg_22, self.main_det_arg_23, self.main_det_arg_31,
						self.main_det_arg_32, self.main_det_arg_33]
		self.mainDetArgLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.mainDetArgLabels ]
		self.mainDetWindgets   = [self.main_det_triangle_label, self.main_det_equals_1, self.main_det_brice_label_1, self.main_det_brice_label_2, self.main_det_equals_2]

		self.det1AnswerLabels = [self.det1_answer_label_1, self.det1_answer_label_2, self.det1_answer_label_3]
		self.det1AnswerLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.det1AnswerLabels ]
		self.det1ArgumentLabels = [self.det1_argument_12_label, self.det1_argument_13_label, self.det1_argument_22_label, self.det1_argument_23_label, self.det1_argument_32_label,
						self.det1_argument_33_label]
		self.det1ArgumentLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.det1ArgumentLabels ]
		self.det1Widgets = [self.det1_triangle_label, self.det1_index_label, self.det1_equals_1_label, self.det1_brice_label_1, self.det1_brice_label_2, self.det1_equals_2_label]

		self.det2AnswerLabels = [self.det2_answer_label_1, self.det2_answer_label_2, self.det2_answer_label_3]
		self.det2AnswerLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.det2AnswerLabels ]
		self.det2ArgumentLabels = [self.det2_argument_11_label, self.det2_argument_13_label, self.det2_argument_21_label, self.det2_argument_23_label, self.det2_argument_31_label, self.det2_argument_33_label]
		self.det2ArgumentLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.det2ArgumentLabels ]
		self.det2Widgets = [self.det2_triangle_label, self.det2_index_label, self.det2_equals_1_label, self.det2_brice_label_1, self.det2_brice_label_2, self.det2_equals_2_label]

		self.det3AnswerLabels = [self.det3_answer_label_1, self.det3_answer_label_2, self.det3_answer_label_3]
		self.det3AnswerLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.det3AnswerLabels ]
		self.det3ArgumentLabels = [self.det3_argument_11_label, self.det3_argument_12_label, self.det3_argument_21_label, self.det3_argument_22_label]
		self.det3ArgumentLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.det3ArgumentLabels ]
		self.det3Widgets = [self.det3_triangle_label, self.det3_index_label, self.det3_equals_1_label, self.det3_brice_label_1, self.det3_brice_label_2, self.det3_equals_2_label]

		self.x1Widgets = [self.x1_label, self.x1_equals_label, self.x1_det1_triangle_label, self.x1_det_index_label, self.x1_divide_line_label, self.x1_main_triangle_det_label,
					self.x1_equals2_label, self.x1_divide_line2_label, self.x1_equals3_label, self.x1_result_label]
		self.x2Widgets = [self.x2_label, self.x2_equals_label, self.x2_det2_triangle_label, self.x2_det_index_label, self.x2_divide_line_label, self.x2_main_triangle_det_label,
					self.x2_equals2_label, self.x2_divide_line2_label, self.x2_equals3_label, self.x2_result_label]
		self.x3Widgets = [self.x3_label, self.x3_equals_label, self.x3_det3_triangle_label, self.x3_det_index_label, self.x3_divide_line_label, self.x3_main_triangle_det_label,
					self.x3_equals2_label, self.x3_divide_line2_label, self.x3_equals3_label, self.x3_result_label]

		self.hide = [self.mainDetWindgets, self.det1Widgets, self.det2Widgets, self.det3Widgets, self.x1Widgets, self.x2Widgets, self.x3Widgets]
		self.actions = [self.showMainDetWidgets, self.showMainDet, self.showFirstDetWidgets, self.showFirstDet, self.showSecondDetWidgets, self.showSecondDet, self.showThirdDetWidgets]
		self.pushButton.clicked.connect(self.nextAction)
		self.hideAll()

	def refreshAnswerLabels(self):
		for i in range(len(self.answerLabels)):
			self.answerLabels[i].move(*self.answerLabelsCoordinates[i])

	def nextAction(self):
		if self.count == len(self.actions):
			return
		print(self.actions[self.count])
		self.actions[self.count]()
		self.count += 1

	def hideAll(self):
		for i in self.hide:
			for j in i:
				j.hide()

	def showWidgets(self, widgetsList):
		for i in widgetsList:
			i.show()

	def showMainDetWidgets(self):
		self.showWidgets(self.mainDetWindgets)
		for i in range(len(self.mainDetArgLabels)):
			self.systemArgumentLabels[i].setCoordinates(QtCore.QPoint(*self.mainDetArgLabelsCoordinates[i]))

	def refreshSystemLabels(self):
		for i in range(len(self.systemArgumentLabels)):
			self.systemArgumentLabels[i].move(*self.systemArgumentLabelsCoordinates[i])
		for i in range(len(self.systemArgumentLabels)):
			self.mainDetArgLabels[i].setText(self.systemArgumentLabels[i].text())

	def showFirstDetWidgets(self):
		j = 0
		for i in range(len(self.systemArgumentLabels)):
			if self.systemArgumentLabels[i].objectName()[-1] == '1': continue
			self.det1ArgumentLabels[j].setText(self.systemArgumentLabels[i].text())
			j += 1
		self.showWidgets(self.det1Widgets)

	def showFirstDet(self):
		matr = swapRowsL(self.matrix, 0, self.matrixB)
		res = det(matr)
		for i in range(len(self.det1AnswerLabels)): self.det1AnswerLabels[i].setText(str(self.answerLabels[i].text()))
		self.det_1_label.setText(str(int(res)))
		self.refreshAnswerLabels()

	def setAnswerLabelsCoordinates(self, coordinatesList):
		for i in range(len(self.answerLabels)):
			self.answerLabels[i].setCoordinates(QtCore.QPoint(*coordinatesList[i]))

	def showSecondDet(self):
		matr = swapRowsL(self.matrix, 1, self.matrixB)
		res = det(matr)
		self.det_2_label.setText(str(int(res)))
		for i in range(len(self.det2AnswerLabels)):
			self.det2AnswerLabels[i].setText(self.answerLabels[i].text())
		self.refreshAnswerLabels()

	def showSecondDetWidgets(self):
		j = 0
		for i in range(len(self.systemArgumentLabels)):
			if self.systemArgumentLabels[i].objectName()[-1] == '2': continue
			self.det2ArgumentLabels[j].setText(self.systemArgumentLabels[i].text())
			j += 1
		self.showWidgets(self.det2Widgets)
		self.setAnswerLabelsCoordinates(self.det2AnswerLabelsCoordinates)

	def showThirdDetWidgets(self):
		self.showWidgets(self.det3Widgets)

	def showMainDet(self):
		res = det(self.matrix)
		self.refreshSystemLabels()
		self.main_det_label.setText(str(int(res)))
		self.setAnswerLabelsCoordinates(self.det1AnswerLabelsCoordinates)

def __main__():
	app = QtWidgets.QApplication(sys.argv)
	window = Test(Matrix([[5, 1, 2], [4, 3, 6], [12, 23, 18]]), Matrix([77, 132, 536]))
	window.show()
	app.exec_()

if __name__ == '__main__':
	__main__()
