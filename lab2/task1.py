#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
import os

DIRECTORY_PATH="/Users/amarchuk/Aibron"

def getFilePath(directoryPath, filePath):
    return os.path.join(directoryPath, filePath)

def isFile(directoryPath, filePath):
    return os.path.isfile(getFilePath(directoryPath, filePath))

def isDirectory(directoryPath, filePath):
    return os.path.isdir(getFilePath(directoryPath, filePath))

def countFilesInDirectory(directoryPath):
    count = 0
    for filePath in os.listdir(directoryPath):
        if (isFile(directoryPath, filePath) or isDirectory(directoryPath, filePath)) and not filePath.startswith("."):
            count += 1
    return count

totalFilesInDirectory = countFilesInDirectory(DIRECTORY_PATH)
print(f"Total files inside {DIRECTORY_PATH}: {totalFilesInDirectory}")