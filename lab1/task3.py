#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python
import getpass
from enum import Enum


class PasswordType(Enum):
    CONFIRMATION = "confirmed"
    VERIFICATION = "verified"


def validatePassword(originalPassword, passwordToVerify, passwordType: PasswordType):
    if originalPassword != passwordToVerify:
        print(
            f"{passwordType.value} password doesn't match")
        printAccessType(passwordType, False)
        exit()
    else:
        print(
            f"{passwordType.value} password match")
        printAccessType(passwordType, True)

def printAccessType(passwordType: PasswordType, isCorrect):
    if passwordType is passwordType.VERIFICATION and isCorrect:
        print("ACCESS PERMIT")
    elif passwordType is passwordType.VERIFICATION and not isCorrect:
        print("ACCESS DENIED")


original_password = getpass.getpass("===Enter a password===\n")
confirm_password = getpass.getpass("Confirm password:\n")
validatePassword(original_password, confirm_password, PasswordType.CONFIRMATION)

verify_password = getpass.getpass("Verify password:\n")
validatePassword(original_password, verify_password, PasswordType.VERIFICATION)
