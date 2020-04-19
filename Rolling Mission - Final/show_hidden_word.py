# exc. 7.3.1 (Rolling Mission)
def show_hidden_word(secret_word, old_letters_guessed):
     """
     the function returns a string that contains underlines and letters
     that show the letters from the list of letters the user guessed
     in their excat location and the other letters the user didnt guess
     as underlines.
     
     :param secret_word: the secret word the user needs to guess
     :param old_letter_guessed: list of letters the user guessed
     :type secret_word: string
     :type old_letters_guessed: list
     :return new_word: new word that contains letters and underlines
     :rtype: string
     """
     
     new_word = ''
     for i in range(0, len(secret_word)):
          if secret_word[i] in old_letters_guessed:
               new_word += secret_word[i] + " "
          elif secret_word[i] not in old_letters_guessed:
               new_word += " _ "
     return new_word

def main():
     secret_word = "mammalas"
     old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
     print(show_hidden_word(secret_word, old_letters_guessed))

if __name__ == "__main__":
     main()