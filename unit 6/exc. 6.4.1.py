# exc. 6.4.1 (Rolling Mission)
def check_valid_input(letter_guessed, old_letter_guessed):
     """
     the function will check if the user typed only one letter
     in english.
     False if:
     1. 2 letters or more
     2. if the "string" contains a symbol
     3. if the letter is already guessed

     :param letter_guessed: input from user
     :type letter_guessed: string
     :param old_letter_guessed: list of the letters already guessed
     :type old_letter_guessed: list
     :param boolean: save the answer (T/F)
     :type boolean: bool
     :return: the result - True or False
     :rtype: bool
     """
     letter_guessed.lower()
     if len(letter_guessed) > 1:
          boolean = False
          print(boolean)
     elif letter_guessed.isalpha() == False and len(letter_guessed) >= 1:
          boolean = False
          print(boolean)
     elif letter_guessed in old_letter_guessed:
          boolean = False
          print(boolean)
     elif letter_guessed.isalpha() == True and len(letter_guessed) == 1:
          boolean = True
          print(boolean)


def main():
     old_letter_guessed = ['a', 'b', 'c']
     letter_guessed = input('Please Enter Your Guess Here: ')
     check_valid_input(letter_guessed, old_letter_guessed)

if __name__ == "__main__":
     main()