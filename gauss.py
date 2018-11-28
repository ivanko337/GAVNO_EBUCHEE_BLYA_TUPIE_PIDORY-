#!/usr/bin/env python3
#coding=utf-8

from gui_gauss import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from MyMatrix import Matrix
from MatrixAlghoritms import addColumn
from toTriangleShape import toTriangleShape

class Gauss(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.matrix = None
		self.matrixB = None
		self.matrixAB = None
		self.x = None
		self.y = None
		self.z = None
		self.matrixList = []
		self.count = 0
		self.systemArgumentLineEdits = [ [self.argument_lineEdit_11, self.argument_lineEdit_12, self.argument_lineEdit_13],
							[self.argument_lineEdit_21, self.argument_lineEdit_22, self.argument_lineEdit_23],
							[self.argument_lineEdit_31, self.argument_lineEdit_32, self.argument_lineEdit_33]]
		self.answerLineEdits = [ self.answer_lineEdit_1, self.answer_lineEdit_2, self.answer_lineEdit_3 ]

		self.systemArgumentLables = [self.argument_label_11, self.argument_label_12, self.argument_label_13, self.argument_label_21, self.argument_label_22, self.argument_label_23,
							self.argument_label_31, self.argument_label_32, self.argument_label_33]
		self.systemArgumentLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.systemArgumentLables ]

		self.answerLabels = [self.answer_label_1, self.answer_label_2, self.answer_label_3]
		self.answerLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.answerLabels ]

		self.matrixALabels = [ self.matrixA_label_11, self.matrixA_label_12, self.matrixA_label_13,
					self.matrixA_label_21, self.matrixA_label_22, self.matrixA_label_23,
					self.matrixA_label_31, self.matrixA_label_32, self.matrixA_label_33 ]
		self.matrixALabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.matrixALabels ]

		self.matrixBLabels = [ self.matrixB_1, self.matrixB_2, self.matrixB_3 ]
		self.matrixBLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.matrixBLabels ]

		self.matrixABWidgets = [ self.matrixA_label, self.matrixA_bracket_label_1, self.matrixA_bracket_label_2, self.matrixB_label, self.matrixB_bracket_label_1, self.matrixB_bracket_label_2 ]

		self.augmentMatrixWidgets = [ self.augmentMatrix_bracket_label_1, self.augmentMatrix_vertLine_label, self.augmentMatrix_bracket_label_2 ]
		self.augmentMatrixArgumentLabels = [ self.augmentMatrix_label_11, self.augmentMatrix_label_12, self.augmentMatrix_label_13,
							self.augmentMatrix_label_21, self.augmentMatrix_label_22, self.augmentMatrix_label_23,
							self.augmentMatrix_label_31, self.augmentMatrix_label_32, self.augmentMatrix_label_33 ]
		self.augmentMatrixArgumentLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.augmentMatrixArgumentLabels ]

		self.augmentMatrixAnswersLabels = [ self.augmentMatrix_label_14, self.augmentMatrix_label_24, self.augmentMatrix_label_34 ]
		self.augmentMatrixAnswersLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.augmentMatrixAnswersLabels ]

		self.matrix1Labels = [ self.matrix_1_11, self.matrix_1_12, self.matrix_1_13, self.matrix_1_14,
					self.matrix_1_21, self.matrix_1_22, self.matrix_1_23, self.matrix_1_24,
					self.matrix_1_31, self.matrix_1_32, self.matrix_1_33, self.matrix_1_34 ]
		self.matrix1Widgets = [ self.matrix1_bracket_label_1, self.matrix1_bracket_label_2, self.matrix1_vertLine_label ]
		self.matrix2Labels = [ self.matrix_2_11, self.matrix_2_12, self.matrix_2_13, self.matrix_2_14,
					self.matrix_2_21, self.matrix_2_22, self.matrix_2_23, self.matrix_2_24,
					self.matrix_2_31, self.matrix_2_32, self.matrix_2_33, self.matrix_2_34 ]
		self.matrix2Widgets = [ self.tilde_label_1, self.matrix2_bracket_label_1, self.matrix2_bracket_label_2, self.matrix2_vertLine_label ]
		self.matrix3Labels = [ self.matrix_3_11, self.matrix_3_12, self.matrix_3_13, self.matrix_3_14,
					self.matrix_3_21, self.matrix_3_22, self.matrix_3_23, self.matrix_3_24,
					self.matrix_3_31, self.matrix_3_32, self.matrix_3_33, self.matrix_3_34 ]
		self.matrix3LabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.matrix3Labels ]
		self.matrix3Widgets = [ self.tilde_label_2, self.matrix3_bracket_label_1, self.matrix3_bracket_label_2, self.matrix3_vertLine_label ]

		self.resultSystemWidgets = [ self.brace_label_2, self.label_16, self.label_19, self.label_21, self.label_22, self.label_27, self.label_28, self.label_29, self.label_30, self.label_31,
							self.x11_label_3, self.x21_label_3, self.x22_label_3, self.x31_label_3, self.x32_label_3, self.x33_label_3 ]
		self.resultSystemLabels = [ self.result_system_label_11, self.result_system_label_12, self.result_system_label_13,
					self.result_system_label_21, self.result_system_label_22, self.result_system_label_23,
					self.result_system_label_31, self.result_system_label_32, self.result_system_label_33 ]
		self.resultSystemLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.resultSystemLabels ]

		self.resultSystemAnswerLabels = [ self.result_system_answer_label_1, self.result_system_answer_label_2, self.result_system_answer_label_3 ]
		self.resultSystemAnswerLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.resultSystemAnswerLabels ]

		self.values = [self.z_label, self.z_value_label, self.y_label, self.y_value_label, self.x_label, self.x_value_label]

		self.hide = [self.augmentMatrixWidgets, self.matrixABWidgets, self.matrix1Widgets, self.matrix2Widgets, self.matrix3Widgets, self.resultSystemWidgets, self.values]

		self.actions = [ self.showABMatrixWidgets, self.showAugmentMatrixWidgets, self.showFirstMatrixWidgets, self.showSecondMatrixWidgets, self.showThirdMatrixWidgets,
				self.showResultMatrixWidgets, self.refreshMatrix3Labels, self.showZValue, self.showYValue, self.showXValue ]

		self.normalizeLineEdits()
		self.hideAll()
		self.pushButton.clicked.connect(self.nextAction)

	def refreshWidgets(self, widgets, coordinates):
		for i in range(len(widgets)):
			widgets[i].move(*coordinates[i])

	def refreshSysLabels(self):
		self.refreshWidgets(self.systemArgumentLables, self.systemArgumentLabelsCoordinates)

	def refreshAnswerLabel(self):
		self.refreshWidgets(self.answerLabels, self.answerLabelsCoordinates)

	def refreshMatrixALabels(self):
		self.refreshWidgets(self.matrixALabels, self.matrixALabelsCoordinates)

	def refreshMatrixBLabels(self):
		self.refreshWidgets(self.matrixBLabels, self.matrixBLabelsCoordinates)

	def createAugmentMatrix(self):
		self.matrixAB = addColumn(self.matrix, self.matrixB)
		self.matrixList = toTriangleShape(self.matrixAB)

	def nextAction(self):
		if self.count == len(self.actions):
			return
		self.actions[self.count]()
		self.count += 1

	def setCoordinates(self, widgets, coordinates):
		for i in range(len(widgets)):
			widgets[i].setCoordinates(QtCore.QPoint(*coordinates[i]))

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
				self.systemArgumentLables[j].setText(k.text())
				j += 1
		for i in range(len(self.answerLineEdits)):
			self.answerLabels[i].setText(str(self.answerLineEdits[i].text()))

	def hideAll(self):
		for i in self.hide:
			for j in i:
				j.hide()

	def showFirstMatrixWidgets(self):
		for i in range(len(self.augmentMatrixArgumentLabels)):
			self.augmentMatrixArgumentLabels[i].setText(self.matrixALabels[i].text())
		for i in range(len(self.augmentMatrixAnswersLabels)):
			self.augmentMatrixAnswersLabels[i].setText(self.matrixBLabels[i].text())
		self.refreshMatrixALabels()
		self.refreshMatrixBLabels()
		self.createAugmentMatrix()
		for i in self.matrix1Widgets:
			i.show()
		self.fillFirstMatrixLabels()

	def showSecondMatrixWidgets(self):
		self.tilde_label_1.show()
		for i in range(len(self.matrix2Widgets)):
			self.matrix2Widgets[i].show()
		j = 0
		for i in self.matrixList[1]:
			for k in i:
				self.matrix2Labels[j].setText(str(int(k) if int(k) == k else k))
				j += 1

	def showThirdMatrixWidgets(self):
		self.tilde_label_2.show()
		for i in range(len(self.matrix3Widgets)):
			self.matrix3Widgets[i].show()
		j = 0
		for i in self.matrixList[2]:
			for k in i:
				self.matrix3Labels[j].setText(str(int(k) if int(k) == k else k))
				j += 1

	def fillFirstMatrixLabels(self):
		j = 0
		for i in self.matrixList[0]:
			for k in i:
				self.matrix1Labels[j].setText(str(int(k) if int(k) == k else k))
				j += 1

	def showAugmentMatrixWidgets(self):
		for i in range(len(self.matrixALabels)):
			self.matrixALabels[i].setText(self.systemArgumentLables[i].text())
		for i in range(len(self.answerLabels)):
			self.matrixBLabels[i].setText(self.answerLabels[i].text())
		self.refreshSysLabels()
		self.refreshAnswerLabel()
		self.setCoordinates(self.matrixALabels, self.augmentMatrixArgumentLabelsCoordinates)
		self.setCoordinates(self.matrixBLabels, self.augmentMatrixAnswersLabelsCoordinates)
		for i in self.augmentMatrixWidgets:
			i.show()

	def normalizeLineEdits(self):
		for i in self.systemArgumentLineEdits:
			for j in i:
				j.raise_()

	def showABMatrixWidgets(self):
		self.createMatrix()
		self.setCoordinates(self.systemArgumentLables, self.matrixALabelsCoordinates)
		self.setCoordinates(self.answerLabels, self.matrixBLabelsCoordinates)
		for i in self.matrixABWidgets:
			i.show()

	def showResultMatrixWidgets(self):
		for i in range(len(self.resultSystemWidgets)):
			self.resultSystemWidgets[i].show()
		self.setThirdMatrixLabelsCoordinates()

	def setThirdMatrixLabelsCoordinates(self):
		j = 0
		for i in range(len(self.matrix3Labels)):
			if self.matrix3Labels[i].objectName()[-1] != '4':
				self.matrix3Labels[i].setCoordinates(QtCore.QPoint(*self.resultSystemLabelsCoordinates[j]))
				j += 1
		j = 0
		for i in range(len(self.matrix3Labels)):
			if self.matrix3Labels[i].objectName()[-1] == '4':
				self.matrix3Labels[i].setCoordinates(QtCore.QPoint(*self.resultSystemAnswerLabelsCoordinates[j]))
				j += 1

	def refreshMatrix3Labels(self):
		for i in range(len(self.matrix3Labels)):
			self.matrix3Labels[i].move(*self.matrix3LabelsCoordinates[i])
		j = 0
		k = 0
		for i in range(len(self.matrix3Labels)):
			if self.matrix3Labels[i].objectName()[-1] != '4':
				self.resultSystemLabels[j].setText(self.matrix3Labels[i].text())
				j += 1
			else:
				self.resultSystemAnswerLabels[k].setText(self.matrix3Labels[i].text())
				k += 1

	def showZValue(self):
		self.z_label.show()
		self.z_value_label.show()
		self.z = float(self.result_system_answer_label_3.text())
		self.z = round(self.z, 2)
		self.z = int(self.z) if int(self.z) == self.z else self.z
		self.z_value_label.setText(str(self.z))

	def showYValue(self):
		y_answ = round(float(self.result_system_answer_label_2.text()), 2)
		y_answ = int(y_answ) if int(y_answ) == y_answ else y_answ
		z_coef = round(float(self.result_system_label_23.text()), 2)
		z_coef = int(z_coef) if int(z_coef) == z_coef else z_coef
		self.y_label.show()
		self.y_value_label.show()
		self.y = y_answ - z_coef * self.z
		self.y = round(self.y, 2)
		self.y = int(self.y) if int(self.y) == self.y else self.y
		self.y_value_label.setText('{} - {}z = {} - {} * {} = {}'.format(y_answ, z_coef, y_answ, z_coef, self.z, self.y))

	def showXValue(self):
		self.x_label.show()
		self.x_value_label.show()
		z_coef = round(float(self.result_system_label_13.text()), 2)
		z_coef = int(z_coef) if int(z_coef) == z_coef else z_coef
		y_coef = round(float(self.result_system_label_12.text()), 2)
		y_coef = int(y_coef) if int(y_coef) == y_coef else y_coef
		x_answ = round(float(self.result_system_answer_label_1.text()), 2)
		x_answ = int(x_answ) if int(x_answ) == x_answ else x_answ
		self.x = x_answ - z_coef * self.z - y_coef * self.y
		self.x = round(self.x, 2)
		self.x = int(self.x) if int(self.x) == self.x else self.x
		self.x_value_label.setText('{} - {}z - {}y = {} - {} * {} - {} * {} = {}'.format(x_answ, z_coef, y_coef, x_answ, z_coef, self.z, y_coef, self.y, self.x))

def __main__():
	app = QtWidgets.QApplication([])
	window = Gauss()
	window.show()
	app.exec_()

if __name__ == '__main__':
	__main__()
