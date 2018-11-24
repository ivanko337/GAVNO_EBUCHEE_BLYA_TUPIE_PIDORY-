#coding=utf-8

from copy import deepcopy
from MatrixAlghoritms import printMatr, addRows, mulL
from MyMatrix import Matrix
from numpy import around

def round(matrix):
	matrix = deepcopy(matrix)
	for i in range(len(matrix)):
		matrix[i] = around(matrix[i], 2)
	return matrix

def normalizeZeros(matrix):
	matrix = deepcopy(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 0:
				matrix[i][j] = 0.0
	return matrix

def toTriangleShape(matr):
	res = []
	matr = deepcopy(matr)
	if matr[0][0] == 0:
		matr = swapRows(matr, 0, -1)
	for i in range(len(matr)):
		for j in range(i + 1, len(matr)):
			coefficient = float(matr[j][i]) / float(matr[i][i])
			coefficient = -coefficient
			print('i: {}, coefficient: {}'.format(i, coefficient))
			print('{} {}'.format(matr[i], matr[j]))
			matr[j] = addRows(matr, i, j, coefficient)
			print('{} {}'.format(matr[i], matr[j]))
		if i != 2:
			res.append(normalizeZeros(matr))
		printMatr(matr)
		print('')
	for i in range(len(matr)):
		if matr[i][i] != 0:
			matr[i] = mulL(matr[i], 1. / matr[i][i])
	res.append(normalizeZeros(matr))
	for i in range(len(res)):
		res[i] = around(res[i], 2)
	return res
