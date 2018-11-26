#coding=utf-8

from copy import deepcopy
from MatrixAlghoritms import addColumn, mulL, printMatr, addRows
from MyMatrix import Matrix

def toUnitShape(matrix, col=Matrix([]), col_is_matr=False):
	res = []
	matrix = deepcopy(matrix)
	matrix = addColumn(matrix, col, col_is_matrix=col_is_matr)
	for i in range(len(matrix)):
		matrix[i] = mulL(matrix[i], 1. / matrix[i][i])
	for i in range(len(matrix)):
		for j in range(i + 1, len(matrix)):
			coefficient = matrix[j][i] / matrix[i][i]
			coefficient = -coefficient
			matrix[j] = addRows(matrix, i, j, coefficient)
		res.append(deepcopy(matrix))
	for i in range(len(matrix)):
		matrix[i] = mulL(matrix[i], 1 / matrix[i][i])
	res.append(deepcopy(matrix))
	for i in range(len(matrix)):
		for j in range(i):
			coefficient = matrix[j][i] / matrix[i][i]
			coefficient = -coefficient
			matrix[j] = addRows(matrix, i, j, coefficient)
		res.append(deepcopy(matrix))
	return res

if __name__ == '__main__':
	t = Matrix([ [1, 3, 6, 2], [2, 1, -1, 1], [3, -1, -1, 7] ])
	tr = toUnitShape(t)
	for i in range(len(tr)):
		printMatr(tr[i])
		print('')
