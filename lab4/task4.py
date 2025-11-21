#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
import random
import numpy as np

M = 128
N = 128

def verifyMatrixSumViaNumpy(matrixA, matrixB):
    npA = np.array(matrixA)
    npB = np.array(matrixB)
    npSum = npA + npB
    if np.array_equal(npSum, np.array(matrixSum)):
        print("Verification passed: result matches NumPy sum")
    else:
        print("Verification failed: result does NOT match NumPy sum")

def generateMatrix():
    matrix = []
    for i in range(M):
        row = []
        for j in range(N):
            row.append(random.randint(0, 10))
        matrix.append(row)
    return matrix

def sumTwoMatrix(matrixA, matrixB):
    matrixSum = []
    for i in range(M):
        rowSum = []
        for j in range(N):
            rowSum.append(matrixA[i][j] + matrixB[i][j])
        matrixSum.append(rowSum)
    return matrixSum

matrixA = generateMatrix()
matrixB = generateMatrix()
matrixSum = sumTwoMatrix(matrixA, matrixB)
verifyMatrixSumViaNumpy(matrixA, matrixB)