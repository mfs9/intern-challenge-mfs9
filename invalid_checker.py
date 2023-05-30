from password_exceptions import InvalidCharacterException
from password_exceptions import MissingCharacterException


class InvalidChecker:
    """
    This class should contain the code to check
    if the password contains any invalid characters
    """

    def __init__(self, password: str) -> None:
        self.password = password
        self.special_chars = "!$%&\()*+-/?@_" 
        self.check_validity()

    def check_validity(self):
        # Checking if there's any invalid character
        for char in self.password:
            if char not in self.special_chars and not char.isalnum():
                raise InvalidCharacterException()

        # Checking if there's at least one special character
        if not any(char in self.special_chars for char in self.password):
            raise MissingCharacterException("special character")