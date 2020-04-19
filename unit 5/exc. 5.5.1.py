# exc. 5.5.1 (Rolling Mission)
def is_valid_input(letter_guessed):
     """
     the function will check if the user typed only one letter
     in english.
     False if:
     1. 2 letters or more/
     2. if the "string" contains a symbol

     :param boolean: save the answer (T/F)
     :type boolean: bool
     :return: the result - True or False
     :rtype: bool
     """
     if len(letter_guessed) > 1:
          boolean = False
          print(boolean)
     elif letter_guessed.isalpha() == False and len(letter_guessed) >= 1:
          boolean = False
          print(boolean)
     elif letter_guessed.isalpha() == True and len(letter_guessed) == 1:
          boolean = True
          print(boolean)

def main():
     letter_guessed = input('Please Enter Your Guess Here: ')
     letter_guessed = letter_guessed.lower()
     is_valid_input(letter_guessed)

if __name__ == "__main__":
     main()