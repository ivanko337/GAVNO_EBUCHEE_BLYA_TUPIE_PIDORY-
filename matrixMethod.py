#!/usr/bin/env python3
#coding=utf-8

from matrixMethod_gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from MyMatrix import Matrix
from MatrixAlghoritms import addColumn
from toUnitShape import toUnitShape

class MatrixMethod(QtWidgets.QMainWindow, Ui_MainWindow):
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
		self.matrix4Labels = [ self.matrix_4_11, self.matrix_4_12, self.matrix_4_13, self.matrix_4_14,
					self.matrix_4_21, self.matrix_4_22, self.matrix_4_23, self.matrix_4_24,
					self.matrix_4_31, self.matrix_4_32, self.matrix_4_33, self.matrix_4_34 ]
		self.matrix4Widgets = [ self.tilde_label_5, self.tilde_label_6, self.matrix4_bracket_label_1, self.matrix4_bracket_label_2, self.matrix4_vertLine_label ]
		self.matrix5Labels = [ self.matrix_5_11, self.matrix_5_12, self.matrix_5_13, self.matrix_5_14,
					self.matrix_5_21, self.matrix_5_22, self.matrix_5_23, self.matrix_5_24,
					self.matrix_5_31, self.matrix_5_32, self.matrix_5_33, self.matrix_5_34 ]
		self.matrix5Widgets = [ self.tilde_label_3, self.matrix5_bracket_label_1, self.matrix5_bracket_label_2, self.matrix5_vertLine_label ]
		self.matrix6Labels = [ self.matrix_6_11, self.matrix_6_12, self.matrix_6_13, self.matrix_6_14,
					self.matrix_6_21, self.matrix_6_22, self.matrix_6_23, self.matrix_6_24,
					self.matrix_6_31, self.matrix_6_32, self.matrix_6_33, self.matrix_6_34 ]
		self.matrix6Widgets = [ self.tilde_label_4, self.matrix6_bracket_label_1, self.matrix6_bracket_label_2, self.matrix6_vertLine_label ]
		self.matrix7Labels = [ self.matrix_7_11, self.matrix_7_12, self.matrix_7_13, self.matrix_7_14,
					self.matrix_7_21, self.matrix_7_22, self.matrix_7_23, self.matrix_7_24,
					self.matrix_7_31, self.matrix_7_32, self.matrix_7_33, self.matrix_7_34 ]
		self.matrix7LabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.matrix7Labels ]
		self.matrix7Widgets = [ self.tilde_label_7, self.tilde_label_8, self.matrix7_bracket_label_1, self.matrix7_bracket_label_2, self.matrix7_vertLine_label ]

		self.resultSystemWidgets = [ self.brace_label_2, self.label_16, self.label_19, self.label_21, self.label_22, self.label_27, self.label_28, self.label_29, self.label_30, self.label_31,
							self.x11_label_3, self.x22_label_3, self.x33_label_3 ]
		self.resultSystemLabels = [ self.result_system_label_11, self.result_system_label_12, self.result_system_label_13,
					self.result_system_label_21, self.result_system_label_22, self.result_system_label_23,
					self.result_system_label_31, self.result_system_label_32, self.result_system_label_33 ]
		self.resultSystemLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.resultSystemLabels ]

		self.resultSystemAnswerLabels = [ self.result_system_answer_label_1, self.result_system_answer_label_2, self.result_system_answer_label_3 ]
		self.resultSystemAnswerLabelsCoordinates = [ (i.pos().x(), i.pos().y()) for i in self.resultSystemAnswerLabels ]

		self.values = [self.z_label, self.z_value_label, self.y_label, self.y_value_label, self.x_label, self.x_value_label]

		self.hide = [self.augmentMatrixWidgets, self.matrixABWidgets, self.matrix1Widgets, self.matrix2Widgets, self.matrix3Widgets, self.resultSystemWidgets, self.values,
				self.matrix4Widgets, self.matrix5Widgets, self.matrix6Widgets, self.matrix7Widgets]

		self.actions = [ self.showABMatrixWidgets, self.showAugmentMatrixWidgets, self.showFirstMatrixWidgets, self.showSecondMatrixWidgets, self.showThirdMatrixWidgets,
				self.showFourthMatrixWidgets, self.showFifthMatrixWidgets, self.showSixthMatrixWidgets, self.showSeventhMatrixWidgets, self.showResultMatrixWidgets,
				self.refreshMatrix7Labels ]

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
		self.matrixList = toUnitShape(self.matrixAB)

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

	def showFourthMatrixWidgets(self):
		for i in range(len(self.matrix4Widgets)):
			self.matrix4Widgets[i].show()
		j = 0
		for i in self.matrixList[3]:
			for k in i:
				self.matrix4Labels[j].setText(str(int(k) if int(k) == k else k))
				j += 1

	def showFifthMatrixWidgets(self):
		for i in range(len(self.matrix5Widgets)):
			self.matrix5Widgets[i].show()
		j = 0
		for i in self.matrixList[4]:
			for k in i:
				self.matrix5Labels[j].setText(str(int(k) if int(k) == k else k))
				j += 1

	def showSixthMatrixWidgets(self):
		for i in range(len(self.matrix6Widgets)):
			self.matrix6Widgets[i].show()
		j = 0
		for i in self.matrixList[5]:
			for k in i:
				self.matrix6Labels[j].setText(str(int(k) if int(k) == k else k))
				j += 1

	def showSeventhMatrixWidgets(self):
		for i in range(len(self.matrix7Widgets)):
			self.matrix7Widgets[i].show()
		j = 0
		for i in self.matrixList[6]:
			for k in i:
				self.matrix7Labels[j].setText(str(int(k) if int(k) == k else k))
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
		self.setSeventhMatrixLabelsCoordinates()

	def setSeventhMatrixLabelsCoordinates(self):
		j = 0
		for i in range(len(self.matrix3Labels)):
			if self.matrix7Labels[i].objectName()[-1] != '4':
				self.matrix7Labels[i].setCoordinates(QtCore.QPoint(*self.resultSystemLabelsCoordinates[j]))
				j += 1
		j = 0
		for i in range(len(self.matrix7Labels)):
			if self.matrix7Labels[i].objectName()[-1] == '4':
				self.matrix7Labels[i].setCoordinates(QtCore.QPoint(*self.resultSystemAnswerLabelsCoordinates[j]))
				j += 1

	def refreshMatrix7Labels(self):
		for i in range(len(self.matrix7Labels)):
			self.matrix7Labels[i].move(*self.matrix7LabelsCoordinates[i])
		j = 0
		k = 0
		for i in range(len(self.matrix7Labels)):
			if self.matrix7Labels[i].objectName()[-1] != '4':
				self.resultSystemLabels[j].setText(self.matrix7Labels[i].text())
				j += 1
			else:
				self.resultSystemAnswerLabels[k].setText(self.matrix7Labels[i].text())
				k += 1

def __main__():
	print('¯\_(ツ)_/¯')
	app = QtWidgets.QApplication([])
	window = MatrixMethod()
	window.show()
	app.exec_()

if __name__ == '__main__':
	__main__()
