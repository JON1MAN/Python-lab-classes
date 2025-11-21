#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
# Każdego dnia staram się uczyć programowania i rozwijać swoje umiejętności, oraz nigdy nie poddawać się mimo trudności.
userChoice = input("enter text: ")

wordsMap = {
    "i": "oraz",
    "oraz": "i",
    "nigdy": "prawie nigdy",
    "dlaczego": "czemu respectively",
}

text = userChoice.lower()
splittedText = text.split()
updatedText = []
for word in splittedText:
    if word in wordsMap.keys():
        word = wordsMap[word]
    updatedText.append(word)
updatedText = " ".join(updatedText)
print(updatedText)
