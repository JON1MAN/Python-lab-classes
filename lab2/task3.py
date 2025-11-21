#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
from PIL import Image
import os
import sys

def getFilePath(directoryPath, filePath):
    return os.path.join(directoryPath, filePath)

def isFile(directoryPath, filePath):
    return os.path.isfile(getFilePath(directoryPath, filePath))

def convertFromJpgToPng(directoryPath, filePath):
    im = Image.open(getFilePath(directoryPath, filePath))
    im.save(getFilePath(INPUT_DIRECTORY_PATH, filePath).replace(".jpg", ".png"))

def requireExistingJPGFiles(INPUT_DIRECTORY_PATH):
    count = 0
    for filePath in os.listdir(INPUT_DIRECTORY_PATH):
        if isFile(INPUT_DIRECTORY_PATH, filePath) and filePath.endswith(".jpg"):
            count += 1
    if count == 0:
        raise Exception(
            f"Provided folder: {INPUT_DIRECTORY_PATH}, should contain at least one file with .jpg format, but wasn't")

def goThroughAndConvertToPNG(INPUT_DIRECTORY_PATH):
    requireExistingJPGFiles(INPUT_DIRECTORY_PATH)
    for filePath in os.listdir(INPUT_DIRECTORY_PATH):
        if isFile(INPUT_DIRECTORY_PATH, filePath) and filePath.endswith(".jpg"):
            print(f"converting file: {filePath} to png...")
            convertFromJpgToPng(INPUT_DIRECTORY_PATH, filePath)

if __name__ == "__main__":
    INPUT_DIRECTORY_PATH = ""
    try:
        INPUT_DIRECTORY_PATH = sys.argv[1]
        print(INPUT_DIRECTORY_PATH)
        goThroughAndConvertToPNG(INPUT_DIRECTORY_PATH)
    except:
        INPUT_DIRECTORY_PATH = os.path.abspath(os.path.dirname(__file__))
