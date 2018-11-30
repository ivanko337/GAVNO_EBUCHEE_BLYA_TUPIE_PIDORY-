#coding=utf-8

from copy import deepcopy
from MatrixAlghoritms import addColumn, mulL, addRows, printMatr, swapRows
from MyMatrix import Matrix

def matrixEquals(m1, m2):
	if len(m1) != len(m2):
		return False
	for i in range(len(m1)):
		for j in range(len(m1[i])):
			if m1[i][j] != m2[i][j]:
				return False
	return True

def toUnitShape(matrix, col=Matrix([]), col_is_matr=False):
	res = []
	matrix = deepcopy(matrix)
	matrix = addColumn(matrix, col, col_is_matrix=col_is_matr)
	for i in range(len(matrix)):
		if int(matrix[i][i]) != 0:
			matrix[i] = mulL(matrix[i], 1. / matrix[i][i])
		printMatr(matrix)
		print('')
	print('')
	for i in range(len(matrix)):
		for j in range(i + 1, len(matrix)):
			if float(matrix[i][i]) != 0:
				coefficient = float(matrix[j][i]) / float(matrix[i][i])
			else:
				if i + 1 != len(matrix):
					matrix = swapRows(matrix, i, i + 1)
				continue
			coefficient = -coefficient
			matrix[j] = addRows(matrix, i, j, coefficient)
		printMatr(matrix)
		print('')
		res.append(deepcopy(matrix))
	for i in range(len(matrix)):
		if int(matrix[i][i]) != 0:
			coefficient = 1. / float(matrix[i][i])
			matrix[i] = mulL(matrix[i], coefficient)
		else:
			if i + 1 != len(matrix):
				matrix = swapRows(matrix, i, i + 1)
	res.append(deepcopy(matrix))
	for i in range(len(matrix)):
		for j in range(i):
			if float(matrix[i][i]) != 0:
				coefficient = float(matrix[j][i]) / float(matrix[i][i])
			else:
				if i + 1 != len(matrix):
					matrix = swapRows(matrix, i, i + 1)
				continue
			coefficient = -coefficient
			matrix[j] = addRows(matrix, i, j, coefficient)
		res.append(deepcopy(matrix))
	return res