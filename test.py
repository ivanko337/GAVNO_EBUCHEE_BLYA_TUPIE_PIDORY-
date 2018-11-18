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
		self.actionCounter = 0
		self.pushButton.clicked.connect(self.nextAction)
		self.actionsList = [self.showMainDet, self.mainDet, self.showFirstDet, self.det1, self.showSecondDet,  self.det2, self.showThirdDet, self.det3, self.fifthAction]
		self.hideWidgets()
		self.matrix = matrix
		self.matrixB = matrixB

	def hideWidgets(self):
		self.main_det_triangle_label.hide()
		self.main_det_equals_1.hide()
		self.main_det_brice_label_1.hide()
		self.main_det_brice_label_2.hide()
		self.main_det_equals_2.hide()

		self.det1_triangle_label.hide()
		self.det1_index_label.hide()
		self.det1_equals_1_label.hide()
		self.det1_brice_label_1.hide()
		self.det1_brice_label_2.hide()
		self.det1_equals_2_label.hide()

		self.det2_triangle_label.hide()
		self.det2_index_label.hide()
		self.det2_equals_1_label.hide()
		self.det2_brice_label_1.hide()
		self.det2_brice_label_2.hide()
		self.det2_equals_2_label.hide()

		self.det3_triangle_label.hide()
		self.det3_index_label.hide()
		self.det3_equals_1_label.hide()
		self.det3_brice_label_1.hide()
		self.det3_brice_label_2.hide()
		self.det3_equals_2_label.hide()

		self.x1_label.hide()
		self.x2_label.hide()
		self.x3_label.hide()
		self.x1_det1_triangle_label.hide()
		self.x2_det2_triangle_label.hide()
		self.x3_det3_triangle_label.hide()
		self.x1_det_index_label.hide()
		self.x2_det_index_label.hide()
		self.x3_det_index_label.hide()
		self.x1_main_triangle_det_label.hide()
		self.x2_main_triangle_det_label.hide()
		self.x3_main_triangle_det_label.hide()
		self.x1_equals_label.hide()
		self.x2_equals_label.hide()
		self.x3_equals_label.hide()
		self.x1_divide_line_label.hide()
		self.x2_divide_line_label.hide()
		self.x3_divide_line_label.hide()
		self.x1_equals2_label.hide()
		self.x2_equals2_label.hide()
		self.x3_equals2_label.hide()
		self.x1_equals3_label.hide()
		self.x2_equals3_label.hide()
		self.x3_equals3_label.hide()
		self.x1_divide_line2_label.hide()
		self.x2_divide_line2_label.hide()
		self.x3_divide_line2_label.hide()

		self.disableArgumentsLabels()

	def disableArgumentsLabels(self):
		self.argument_label_11_hide.setEnabled(False)

	def nextAction(self):
		if self.actionCounter + 1 == len(self.actionsList): return
		self.actionsList[self.actionCounter]()
		self.actionCounter += 1

	def showMainDet(self):
		self.main_det_triangle_label.show()
		self.main_det_equals_1.show()
		self.main_det_brice_label_1.show()
		self.main_det_brice_label_2.show()
		self.main_det_equals_2.show()

	def showFirstDet(self):
		self.det1_triangle_label.show()
		self.det1_index_label.show()
		self.det1_equals_1_label.show()
		self.det1_brice_label_1.show()
		self.det1_brice_label_2.show()
		self.det1_equals_2_label.show()

		self.answer_label_1.setCoordinates(self.det1_answer_label_1.pos())
		self.answer_label_2.setCoordinates(self.det1_answer_label_2.pos())
		self.answer_label_3.setCoordinates(self.det1_answer_label_3.pos())
		print(self.answer_label_1.x)

		self.det1_argument_12_label.setText(self.argument_label_12.text())
		self.det1_argument_22_label.setText(self.argument_label_22.text())
		self.det1_argument_32_label.setText(self.argument_label_32.text())
		self.det1_argument_13_label.setText(self.argument_label_13.text())
		self.det1_argument_23_label.setText(self.argument_label_23.text())
		self.det1_argument_33_label.setText(self.argument_label_33.text())

	def showSecondDet(self):
		self.det2_triangle_label.show()
		self.det2_index_label.show()
		self.det2_equals_1_label.show()
		self.det2_brice_label_1.show()
		self.det2_brice_label_2.show()
		self.det2_equals_2_label.show()

		self.det2_argument_11_label.setText(self.argument_label_11.text())
		self.det2_argument_21_label.setText(self.argument_label_21.text())
		self.det2_argument_31_label.setText(self.argument_label_31.text())
		self.det2_argument_13_label.setText(self.argument_label_13.text())
		self.det2_argument_23_label.setText(self.argument_label_23.text())
		self.det2_argument_33_label.setText(self.argument_label_33.text())

	def showThirdDet(self):
		self.det3_triangle_label.show()
		self.det3_index_label.show()
		self.det3_equals_1_label.show()
		self.det3_brice_label_1.show()
		self.det3_brice_label_2.show()
		self.det3_equals_2_label.show()

		self.det3_argument_11_label.setText(self.argument_label_11.text())
		self.det3_argument_21_label.setText(self.argument_label_21.text())
		self.det3_argument_31_label.setText(self.argument_label_31.text())
		self.det3_argument_12_label.setText(self.argument_label_12.text())
		self.det3_argument_22_label.setText(self.argument_label_22.text())
		self.det3_argument_32_label.setText(self.argument_label_32.text())

#		self.label_39.setText(self.answer_label_1.text())
#		self.label_41.setText(self.answer_label_2.text())
#		self.label_43.setText(self.answer_label_3.text())

	def fifthAction(self):
		pass

	def mainDet(self):
		mdet = det(self.matrix)
		self.main_det_label.setText(str(mdet))

	def det1(self):
		temp_matrix = swapRowsL(self.matrix, 0, self.matrixB)
		res = det(temp_matrix)
		self.det_1_label.setText(str(round(res)))

	def det2(self):
		temp_matrix = swapRowsL(self.matrix, 1, self.matrixB)
		res = det(temp_matrix)
		self.det_2_label.setText(str(round(res)))

	def det3(self):
		temp_matrix = swapRowsL(self.matrix, 2, self.matrixB)
		res = det(temp_matrix)
		self.det_3_label.setText(str(round(res)))

	def setCoordinates(self):
		self.argument_label_11.setCoordinates(self.main_det_arg_11.pos())
		self.argument_label_12.setCoordinates(self.main_det_arg_12.pos())
		self.argument_label_13.setCoordinates(self.main_det_arg_13.pos())
		self.argument_label_21.setCoordinates(self.main_det_arg_21.pos())
		self.argument_label_22.setCoordinates(self.main_det_arg_22.pos())
		self.argument_label_23.setCoordinates(self.main_det_arg_23.pos())
		self.argument_label_31.setCoordinates(self.main_det_arg_31.pos())
		self.argument_label_32.setCoordinates(self.main_det_arg_32.pos())
		self.argument_label_33.setCoordinates(self.main_det_arg_33.pos())

def __main__():
	app = QtWidgets.QApplication(sys.argv)
	window = Test(Matrix([[5, 1, 2], [4, 3, 6], [12, 23, 18]]), Matrix([77, 132, 536]))
	window.show()
	app.exec_()

if __name__ == '__main__':
	__main__()
