# exc 8.4.1 (Rolling Mission)
def print_hangman(num_of_tries):
     HANGMAN_PHOTHOS = {'1': """x-------x""", '2': 
     """
     x-------x
     |
     |
     |
     |
     |""", 
     '3': """
     x-------x
     |       |
     |       0
     |
     |
     |""", 
     '4': """
     x-------x
     |       |
     |       0
     |       |
     |
     |""", 
     '5': """
     x-------x
     |       |
     |       0
     |      /|\\
     |
     |""", 
     '6': """
     x-------x
     |       |
     |       0
     |      /|\\
     |      /
     |""", 
     '7':"""
     x-------x
     |       |
     |       0
     |      /|\\
     |      / \\
     |"""
      }
     if str(num_of_tries) == '1':
          print(HANGMAN_PHOTHOS['1'])
     elif str(num_of_tries) == '2':
          print(HANGMAN_PHOTHOS['2'])
     elif str(num_of_tries) == '3':
          print(HANGMAN_PHOTHOS['3'])
     elif str(num_of_tries) == '4':
          print(HANGMAN_PHOTHOS['4'])
     elif str(num_of_tries) == '5':
          print(HANGMAN_PHOTHOS['5'])
     elif str(num_of_tries) == '6':
          print(HANGMAN_PHOTHOS['6'])
     elif str(num_of_tries) == '7':
          print(HANGMAN_PHOTHOS['7'])
          

def main():
     num_of_tries = 7
     print_hangman(num_of_tries)

if __name__ == '__main__':
     main()
     