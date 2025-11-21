#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python

a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

dotProduct = 0
for i in range(len(a)):
    dotProduct += a[i] * b[i]

print("Dot product:", dotProduct)