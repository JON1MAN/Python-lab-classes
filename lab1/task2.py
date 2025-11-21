#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
GLOBAL_CURRENT_YEAR = 2025
class Human:
    def __init__(self, firstName: str, lastName: str, yearOfBirth: int):
        self.firstName = firstName
        self.lastName = lastName
        self.yearOfBirth = yearOfBirth

    def __str__(self):
        return f"Hi {self.firstName} {self.lastName}! You are approximately {self.calculateDeltaFromYearOfBirth()} years old \U0001f62e!"

    def calculateDeltaFromYearOfBirth(self):
        return GLOBAL_CURRENT_YEAR - self.yearOfBirth

def birthDateInputWithValidation():
    yearOfBirth = input("Please, enter your date of birth: ")
    while (not yearOfBirth.isnumeric()):
        yearOfBirth = input("Please, enter your date of birth (must to contain only numeric): ")
    return int(yearOfBirth)

firstName = input("Please, enter your first name: ")
lastName = input("Please, enter your last name: ")
yearOfBirth = birthDateInputWithValidation()

human = Human(firstName, lastName, yearOfBirth)

print(human.__str__())