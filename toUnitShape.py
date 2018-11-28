#coding=utf-8

from copy import deepcopy
from MatrixAlghoritms import addColumn, mulL, addRows, printMatr, swapRows
from MyMatrix import Matrix

def toUnitShape(matrix, col=Matrix([]), col_is_matr=False):
	res = []
	matrix = deepcopy(matrix)
	matrix = addColumn(matrix, col, col_is_matrix=col_is_matr)
	for i in range(len(matrix)):
		matrix[i] = mulL(matrix[i], 1. / matrix[i][i])
	for i in range(len(matrix)):
		for j in range(i + 1, len(matrix)):
			if matrix[i][i] != 0:
				coefficient = matrix[j][i] / matrix[i][i]
			else:
				matrix = swapRows(matrix, i, i + 1)
				continue
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
	t = Matrix([[1, 2, 77, 4], [3, 6, 132, 12], [23, 18, 536, 5]])
	te = toUnitShape(t)
	printMatr(te[-1])