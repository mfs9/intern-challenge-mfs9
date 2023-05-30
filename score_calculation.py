from variation_checker import VariationChecker
from common_password_checker import CommonPasswordChecker
from password_exceptions import MissingCharacterException
from password_exceptions import InsufficientScoreException


class ScoreCalculation:
    """
    This class contains the code to calculate the score.
    Passwords with score lower than 16 are invalid
    """

    def __init__(self, password: str) -> None:
        self.password = password
        self.checker = VariationChecker(password)
     

        self.common_checker = CommonPasswordChecker(password).check_common()
        self.score = 0

    def check_score_characters(self):
        # Write your code here
        special_chars = "!$%&\()*+-/?@_"

        #Points for alphanumeric chars
        for char in self.password:
            if char.isalnum():
                self.score +=1

        #Points for special chars
        for char in self.password:
            if char in special_chars:
                self.score +=3

        #Common words penalty
        if self.common_checker:
            self.score -=8

        #Char repetition penalty
        for i in range(len(self.password) - 1):
            if self.password[i] == self.password[i+1]:
                self.score -=2

        #Minimum score validation
        if self.score < 16:
            raise InsufficientScoreException(self.score)

        



        return self.score
