#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python

import random
import numpy as np

N = 4

def generateRandomMatrix(start, end):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(random.randint(start, end))
        matrix.append(row)
    return matrix

def buildMinor(matrix, removeRow, removeCol):
    minor = []

    for r in range(len(matrix)):
        if r == removeRow:
            continue

        row = []
        for c in range(len(matrix)):
            if c == removeCol:
                continue
            row.append(matrix[r][c])

        minor.append(row)

    return minor


def isMatrix1x1(matrix):
    return len(matrix) == 1


def isMatrix2x2(matrix):
    return len(matrix) == 2

def computeDeterminant(matrix):
    if isMatrix1x1(matrix):
        return matrix[0][0]

    if isMatrix2x2(matrix):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for col in range(len(matrix)):
        minor = buildMinor(matrix, 0, col)
        sign = (-1) ** col
        det += sign * matrix[0][col] * computeDeterminant(minor)

    return det

def verifyDeterminant(matrix, manualDet):
    numpyMatrix = np.array(matrix)
    numpyDet = round(np.linalg.det(numpyMatrix))

    if numpyDet == manualDet:
        print("Verification passed: manual determinant matches NumPy")
    else:
        print("Verification failed:")
        print("Manual:", manualDet)
        print("NumPy :", numpyDet)

matrix = generateRandomMatrix(0, 10)
det = computeDeterminant(matrix)

verifyDeterminant(matrix, det)

print("\nMatrix:")
for row in matrix:
    print(row)

print("\nDeterminant:", det)

