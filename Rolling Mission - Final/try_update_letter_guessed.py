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
          return boolean
     elif letter_guessed.isalpha() == False and len(letter_guessed) >= 1:
          boolean = False
          return boolean
     elif letter_guessed in old_letter_guessed:
          boolean = False
          return boolean
     elif letter_guessed.isalpha() == True and len(letter_guessed) == 1:
          boolean = True
          return boolean

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
     """
     the function will check if the user typed only one letter
     in english.
     False and other printing if:
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
     check_valid_input(letter_guessed, old_letters_guessed)
     seperator = ' -> '
     if check_valid_input(letter_guessed, old_letters_guessed) == False:
          print('X')
          print(seperator.join(old_letters_guessed))
          print('False')

     elif check_valid_input(letter_guessed, old_letters_guessed) == True:
          print('True')
          old_letters_guessed.append(letter_guessed)
          print("Old Letters: ", old_letters_guessed)



def main():
     old_letters_guessed = ['a', 'p', 'c', 'f']
     try_update_letter_guessed('ab', old_letters_guessed)


if __name__ == "__main__":
     main()