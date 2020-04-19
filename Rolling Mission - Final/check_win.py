# exc. 7.3.2 (Rolling Mission)
def check_win(secret_word, old_letters_guessed):
     """
     the function retrun True if the letters of the secret 
     word are in the letters that the user guessed,
     False if otherwise

     :param secret_word: the secret word the user needs to guess
     :param old_letter_guessed: list of letters the user guessed
     :type secret_word: string
     :type old_letters_guessed: list
     :rtype: boolean

     """
     for i in range(0, len(secret_word)):
          if secret_word[i] in old_letters_guessed:
               boolean = True
          else:
               boolean = False
     return boolean

def main():
     secret_word = 'c a t'
     old_letters_guessed = ['c', 'a', 'c', 'i', 's', 'k', 'y']
     print(check_win(secret_word, old_letters_guessed))

if __name__ == '__main__':
     main()