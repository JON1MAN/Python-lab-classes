#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
#2x² − 4x − 6 = 0
import sys

def toNumericParameters(stringArray):
    numericParameters = []
    for x in stringArray:
        try:
            numericParameters.append(float(x))
        except ValueError:
            print(f"Error: '{x}' is not a number.")
            sys.exit(1)
    return numericParameters

userChoice = input("please provide a b c: ")
splittedParameters = userChoice.split()
numericParameters = toNumericParameters(splittedParameters)
a = numericParameters[0]
b = numericParameters[1]
c = numericParameters[2]

def calculateFirstZero(sqrtOfDiscriminant):
    return (-b + sqrtOfDiscriminant) / (2 * a)

def calculateSecondZero(sqrtOfDiscriminant):
    return (-b - sqrtOfDiscriminant) / (2 * a)

def calculateZerosOfFunction(discriminant):
    sqrtOfDiscriminant = discriminant ** 0.5
    return [calculateFirstZero(sqrtOfDiscriminant), calculateSecondZero(sqrtOfDiscriminant)]

def calculateDiscriminant():
    return b * b - 4 * a * c

def solveQuadraticEquation():
    discriminant = float(calculateDiscriminant())
    return calculateZerosOfFunction(discriminant)

print(solveQuadraticEquation())
