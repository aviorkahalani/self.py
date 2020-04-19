# exc. 2.5.1 (rolling mission)
# display the opening art of the game:
HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/

                     """

# dislpay the max amount of mistakes:
MAX_TRIES = 6

# (sep='\n') = print in another line the 2nd variabale:
print(HANGMAN_ASCII_ART, MAX_TRIES, sep= '\n')
