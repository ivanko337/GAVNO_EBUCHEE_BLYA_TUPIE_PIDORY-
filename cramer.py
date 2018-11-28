#!/usr/bin/env python3
#coding=utf-8

import sys
from first import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from dragLabel import DragLabel
from numpy.linalg import det
from MatrixAlghoritms import swapRowsL
from MyMatrix import Matrix

class Cramer(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.count = 0
		self.matrix = None
		self.matrixB = None
		self.mainDet = None
		self.det1 = None
		self.det2 = None
		self.det3 = None

		self.systemArgumentLineEdits = [ [self.argument_lineEdit_11, self.argument_lineEdit_12, self.argument_lineEdit_13],
							[self.argument_lineEdit_21, self.argument_lineEdit_22, self.argument_lineEdit_23],
							[self.argument_lineEdit_31, self.argument_lineEdit_32, self.argument_lineEdit_33]]
		self.answerLineEdits = [ self.answer_LineEdit_1, self.answer_LineEdit_2, self.answer_LineEdit_3 ]

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
		self.det3ArgumentLabels = [self.det3_argument_11_label, self.det3_argument_12_label, self.det3_argument_21_label, self.det3_argument_22_label, self.det3_argument_31_label, self.det3_argument_32_label]
		self.det3ArgumentLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.det3ArgumentLabels ]
		self.det3Widgets = [self.det3_triangle_label, self.det3_index_label, self.det3_equals_1_label, self.det3_brice_label_1, self.det3_brice_label_2, self.det3_equals_2_label]

		self.x1Widgets = [self.x1_label, self.x1_equals_label, self.x1_det1_triangle_label, self.x1_det_index_label, self.x1_divide_line_label, self.x1_main_triangle_det_label,
					self.x1_equals2_label, self.x1_divide_line2_label, self.x1_equals3_label, self.x1_result_label]
		self.x2Widgets = [self.x2_label, self.x2_equals_label, self.x2_det2_triangle_label, self.x2_det_index_label, self.x2_divide_line_label, self.x2_main_triangle_det_label,
					self.x2_equals2_label, self.x2_divide_line2_label, self.x2_equals3_label, self.x2_result_label]
		self.x3Widgets = [self.x3_label, self.x3_equals_label, self.x3_det3_triangle_label, self.x3_det_index_label, self.x3_divide_line_label, self.x3_main_triangle_det_label,
					self.x3_equals2_label, self.x3_divide_line2_label, self.x3_equals3_label, self.x3_result_label]

		self.hide = [self.mainDetWindgets, self.det1Widgets, self.det2Widgets, self.det3Widgets, self.x1Widgets, self.x2Widgets, self.x3Widgets]
		self.actions = [self.showMainDetWidgets, self.showMainDet, self.showFirstDetWidgets, self.showFirstDet, self.showSecondDetWidgets, self.showSecondDet,
					self.showThirdDetWidgets, self.showThirdDet, self.showX1Widgets, self.showX1Widgets2, self.showX1, self.showX2Widgets, self.showX2Widgets2, self.showX2,
					self.showX3Widgets, self.showX3Widgets2, self.showX3]
		self.pushButton.clicked.connect(self.nextAction)
		self.hideAll()
		self.normalizeLineEdits()

	def normalizeLineEdits(self):
		for i in self.systemArgumentLineEdits:
			for j in i:
				j.raise_()

	def createMatrix(self):
		arguments = Matrix([])
		answers = Matrix([])
		temp = []
		for i in self.systemArgumentLineEdits:
			for j in i:
				temp.append(float(j.text()))
			arguments.append(temp)
			temp = []
		for i in self.answerLineEdits:
			answers.append(float(i.text()))
		self.matrix = arguments
		self.matrixB = answers
		for i in self.systemArgumentLineEdits:
			for j in i:
				j.move(5000, 5000)
		for i in self.answerLineEdits:
			i.move(5000, 5000)
		j = 0
		for i in self.systemArgumentLineEdits:
			for k in i:
				self.systemArgumentLabels[j].setText(k.text())
				j += 1
		for i in range(len(self.answerLineEdits)):
			self.answerLabels[i].setText(str(self.answerLineEdits[i].text()))

	def refreshAnswerLabels(self):
		for i in range(len(self.answerLabels)):
			self.answerLabels[i].move(*self.answerLabelsCoordinates[i])

	def nextAction(self):
		if self.count == len(self.actions):
			return
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
		self.createMatrix()
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
		self.det1 = res
		for i in range(len(self.det1AnswerLabels)): self.det1AnswerLabels[i].setText(str(self.answerLabels[i].text()))
		self.det_1_label.setText(str(int(res)))
		self.refreshAnswerLabels()

	def setAnswerLabelsCoordinates(self, coordinatesList):
		for i in range(len(self.answerLabels)):
			self.answerLabels[i].setCoordinates(QtCore.QPoint(*coordinatesList[i]))

	def showSecondDet(self):
		matr = swapRowsL(self.matrix, 1, self.matrixB)
		res = det(matr)
		self.det2 = res
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

	def showThirdDet(self):
		matr = swapRowsL(self.matrix, 2, self.matrixB)
		res = det(matr)
		self.det3 = res
		self.det_3_label.setText(str(int(res)))
		for i in range(len(self.det3AnswerLabels)):
			self.det3AnswerLabels[i].setText(self.answerLabels[i].text())
		self.refreshAnswerLabels()

	def showThirdDetWidgets(self):
		j = 0
		for i in range(len(self.systemArgumentLabels)):
			if self.systemArgumentLabels[i].objectName()[-1] == '3': continue
			self.det3ArgumentLabels[j].setText(self.systemArgumentLabels[i].text())
			j += 1
		self.showWidgets(self.det3Widgets)
		self.setAnswerLabelsCoordinates(self.det3AnswerLabelsCoordinates)

	def showMainDet(self):
		res = det(self.matrix)
		self.mainDet = res
		self.refreshSystemLabels()
		self.main_det_label.setText(str(int(res)))
		self.setAnswerLabelsCoordinates(self.det1AnswerLabelsCoordinates)

	def showX1Widgets(self):
		for i in self.x1Widgets[:6]:
			i.show()

	def showX1Widgets2(self):
		for i in self.x1Widgets[6:9]:
			i.show()
		self.x1_det1_label.setText(str(int(self.det1)))
		self.x1_main_det_label.setText(str(int(self.mainDet)))

	def showX1(self):
		self.x1Widgets[-1].show()
		self.x1Widgets[-2].show()
		res = self.det1 / self.mainDet
		self.x1_result_label.setText(str(int(round(res))))

	def showX2Widgets(self):
		for i in self.x2Widgets[:6]:
			i.show()

	def showX2Widgets2(self):
		for i in self.x2Widgets[6:8]:
			i.show()
		self.x2_det2_label.setText(str(int(self.det2)))
		self.x2_main_det_label.setText(str(int(self.mainDet)))

	def showX2(self):
		self.x2Widgets[-1].show()
		self.x2Widgets[-2].show()
		res = self.det2 / self.mainDet
		self.x2_result_label.setText(str(int(round(res))))

	def showX3Widgets(self):
		for i in self.x3Widgets[:6]:
			i.show()

	def showX3Widgets2(self):
		for i in self.x3Widgets[6:8]:
			i.show()
		self.x3_det3_label.setText(str(int(self.det3)))
		self.x3_main_det_label.setText(str(int(self.mainDet)))

	def showX3(self):
		self.x3Widgets[-1].show()
		self.x3Widgets[-2].show()
		res = self.det3 / self.mainDet
		self.x3_result_label.setText(str(int(round(res))))

def __main__():
	app = QtWidgets.QApplication(sys.argv)
	window = Cramer()
	window.show()
	app.exec_()

if __name__ == '__main__':
	__main__()
