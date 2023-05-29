class CommonPasswordChecker:
    """
    This class should contain the code to check
    if the password contains a common word, using the common_words.txt dataset
    """

    # Write your code here

    def __init__(self, password):
        self.password = password
        with open('common_words.txt', 'r') as f:
            self.common_words = set(word.strip() for word in f)

    def check_common(self):
        password_words = set(self.password.split())
        # if any(word in self.common_words for word in password_words):
        #     print("password contains a common word.")
        # else:
        #     print("password does not contain a common word.")