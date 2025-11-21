#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python

import random
import numpy as np

M = 8
N = 8

def generateMatrix(start, end):
    matrix = []
    for i in range(M):
        row = []
        for j in range(N):
            row.append(random.randint(start, end))
        matrix.append(row)
    return matrix

def multiplyMatrix(matrixA, matrixB):
    result = generateMatrix(0, 0)
    for i in range(M):
        for j in range(N):
            s = 0
            for k in range(N):
                s += matrixA[i][k] * matrixB[k][j]
            result[i][j] = s
    return result

def verifyMatrixMultiplication(result, matrixA, matrixB):
    npA = np.array(matrixA)
    npB = np.array(matrixB)
    npResult = npA @ npB

    if np.array_equal(npResult, np.array(result)):
        print("Verification passed: manual multiplication matches NumPy result")
    else:
        print("Verification failed: results do NOT match")

matrixA = generateMatrix(0, 10)
matrixB = generateMatrix(0, 10)
multiplyResult = multiplyMatrix(matrixA, matrixB)
verifyMatrixMultiplication(multiplyResult, matrixA, matrixB)
