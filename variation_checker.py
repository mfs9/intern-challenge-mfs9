import re
import string
from password_exceptions import MissingCharacterException

class VariationChecker:
    """
    This class should contain the code to check if there's a minimum of:
     - One numerical digit
     - One special character
     - One uppercase letter
     - One lowercase letter
     If not, the password is invalid
    """

    def __init__(self, password):
        self.password = password
        self.is_valid()

    def is_valid(self):
        # Checking for a numerical digit
        if not any(char.isdigit() for char in self.password):
            raise MissingCharacterException('numerical digit')
        # Checking for a special character
        special_characters = string.punctuation
        if not any(char in special_characters for char in self.password):
            raise MissingCharacterException('special character')
        # Checking for an uppercase letter
        if not any(char.isupper() for char in self.password):
            raise MissingCharacterException('uppercase letter')
        # Checking for a lowercase letter
        if not any(char.islower() for char in self.password):
            raise MissingCharacterException('lowercase letter')
