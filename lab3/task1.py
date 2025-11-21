#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
#Każdego dnia staram się uczyć programowania i rozwijać swoje umiejętności, oraz nigdy nie poddawać się mimo trudności.
#/Users/amarchuk/Documents/GitHub/python_lab_classes/lab3/test.txt
from pathlib import Path
userChoice = input("enter: txt or direct: ")

wordsToRemove = {
    "się",
    "i",
    "oraz",
    "nigdy",
    "dlaczego",
}

def removeWords(text):
    text = text.lower()
    splittedText = text.split()
    words = []
    for word in splittedText:
        if word not in wordsToRemove:
            words.append(word)
    words = " ".join(words)
    return words

if userChoice == "txt":
    filePath = input("enter path: ")
    filePaths = [Path(p) for p in filePath.split(", ")]
    for file in filePaths:
        f = open(file, "r+")
        txt = f.read()
        updatedText = removeWords(txt)
        with open(f"new_{updatedText[0]}.txt", "w") as newFile:
            newFile.write(updatedText)
        f.close()
elif userChoice == "direct":
    txt = input("enter txt: ")
    updatedText = removeWords(txt)
    print(updatedText)