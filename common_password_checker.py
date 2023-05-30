class CommonPasswordChecker:
    """
    This class should contain the code to check
    if the password contains a common word, using the common_words.txt dataset
    """

    # Write your code here



    def __init__(self, password):
        #saves the password as an class instance atribute
        
        self.password = password
        with open('common_words.txt', 'r') as f:
            self.common_words = set(word.strip() for word in f)

    #checks for common words
    def check_common(self):
        for word in self.common_words:
            if word in self.password:
                return True
        return False