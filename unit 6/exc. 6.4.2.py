# exc. 6.4.2 (Rolling Mission)
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
     seperator = ' -> '
     if len(letter_guessed) > 1:
          print('X')
          print(seperator.join(old_letters_guessed))
          print('False')
     elif letter_guessed.isalpha() == False and len(letter_guessed) >= 1:
          print('X')
          print(seperator.join(old_letters_guessed))
          print('False')
     elif letter_guessed.lower() in old_letters_guessed:
          print('X')
          print(seperator.join(old_letters_guessed))
          print('False')
     elif letter_guessed.isalpha() == True and len(letter_guessed) == 1:
          print('True')
          old_letters_guessed.append(letter_guessed)
          print("Old Letters: ", old_letters_guessed)


def main():
     old_letters_guessed = ['a', 'p', 'c', 'f']
     #try_update_letter_guessed('A', old_letters_guessed)
     #try_update_letter_guessed('s', old_letters_guessed)
     #try_update_letter_guessed('$', old_letters_guessed)
     try_update_letter_guessed('$', old_letters_guessed)


if __name__ == "__main__":
     main()