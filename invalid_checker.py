from password_exceptions import InvalidCharacterException


class InvalidChecker:
    """
    This class should contain the code to check
    if the password contains any invalid characters
    """

    def __init__(self, password: str) -> None:
        special_chars = "!$%&\()*+-/?@_"
        if not any(char in special_chars for char in password):
            raise InvalidCharacterException
