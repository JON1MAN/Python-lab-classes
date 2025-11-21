#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
GLOBAL_CURRENT_YEAR = 2025
class Human:
    def __init__(self, firstName: str, lastName: str, yearOfBirth: int):
        self.firstName = firstName
        self.lastName = lastName,
        self.yearOfBirth = yearOfBirth

    def __str__(self):
        print ("Hi " + self.firstName + " " + str(self.lastName) + "! You are approximately " + str(self.calculateDeltaFromYearOfBirth()) + " years old \U0001f62e!")

    def calculateDeltaFromYearOfBirth(self):
        return GLOBAL_CURRENT_YEAR - self.yearOfBirth

def birthDateInputWithValidation():
    yearOfBirth = input("Please, enter your date of birth: ")
    while (not yearOfBirth.isnumeric()):
        yearOfBirth = input("Please, enter your date of birth (must to contain only numeric): ")
    return int(yearOfBirth)

firstName = input("Please, enter your first name: ")
lastName = input()
yearOfBirth = birthDateInputWithValidation()

human = Human(firstName, lastName, yearOfBirth)
human.__str__()

