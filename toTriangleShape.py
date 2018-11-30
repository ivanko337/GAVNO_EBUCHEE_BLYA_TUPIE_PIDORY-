#coding=utf-8

from copy import deepcopy
from MatrixAlghoritms import addRows, mulL, swapRows
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
			if float(matr[i][i]) != 0:
				coefficient = float(matr[j][i]) / float(matr[i][i])
			else:
				matr = swapRows(matr, i, i + 1)
				continue
			coefficient = -coefficient
			matr[j] = addRows(matr, i, j, coefficient)
		if i != 2:
			res.append(normalizeZeros(matr))
	for i in range(len(matr)):
		if matr[i][i] != 0:
			matr[i] = mulL(matr[i], 1. / matr[i][i])
	res.append(normalizeZeros(matr))
	return res
