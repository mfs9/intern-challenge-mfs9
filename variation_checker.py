import re
import string


class VariationChecker:
    """
    This class should contain the code to check if there's a minimum of:
     - One numerical digit
     - One special character
     - One uppercase letter
     - One lowercase letter
     If not, the password is invalid
    """

    # Write your code here

    def __init__(self, password):
        self.password = password

    def is_valid(self):
        #Checando por um valor numerico
        if not any(char.isdigit() for char in self.password):
            print("Password must contain one numerical digit.")
            return False
        #Checando por um caractere especial
        special_characters = string.punctuation
        if not any(char in special_characters for char in self.password):
            print("Password must contain one special character.")
            return False
        #Checar por letra maiuscula
        if not any(char.isupper() for char in self.password):
            print("Password must contain one uppercase letter")
            return False
        #Checar por letra minuscula
        if not any(char.islower() for char in self.password):
            print("Password must contain one lowercase letter.")
            return False
        
        #Caso passe por todas as checagens
        return True