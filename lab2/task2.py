#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
import os
from importlib.metadata import files

DIRECTORY_PATH="/Users/amarchuk/Aibron"

class bcolors:
    HEADER = '\033[95m'
    DIR = '\033[94m'
    FILE = '\033[92m'
    ENDC = '\033[0m'

def getFilePath(directoryPath, filePath):
    return os.path.join(directoryPath, filePath)

def isFile(directoryPath, filePath):
    return os.path.isfile(getFilePath(directoryPath, filePath))

def isDirectory(directoryPath, filePath):
    return os.path.isdir(getFilePath(directoryPath, filePath))

def getColoredElementName(path, file):
    if(isDirectory(path, file)) :
        return bcolors.DIR + file + bcolors.ENDC
    else:
        return bcolors.FILE + file + bcolors.ENDC

def printFilesFromDir(directoryPath):
    totalElements = 0
    directories = 0
    files = 0
    for root, dirs, files in os.walk(directoryPath, topdown=True):
        path = root.split(os.sep)
        files.sort()
        print("|" + (len(path) - 1) * '---', bcolors.HEADER + os.path.basename(root) + bcolors.ENDC)
        for file in files:
            print("|" + len(path) * '---', getColoredElementName(root, file))

print(f"Files inside {DIRECTORY_PATH}")
printFilesFromDir(DIRECTORY_PATH)
