def welcome_page():
	"""
	The function print the welcome screen for the game 
	"""
	print(r"""
	 _    _
	| |  | |
	| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
	|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
	| |  | | (_| | | | | (_| | | | | | | (_| | | | |
	|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
						 __/ |
						|___/
	""")

def choose_word(file_path, index):
	"""
	the function gets a string that represent a file path
	and a number represent index of a word in the file.
	the function return the secret word for the game

	:param file_path: the function gets wth words from this file
	:type file_path: string
	:param index: a number which is the location in the file for the secret word
	:type index: int
	:param words_list: list of words from the file
	:type words_list: list
	:return secret_word: the secret word
	:rtype: string
	"""

	text = open(file_path, 'r')
	words = text.read()
	secret_word = ''
	# creating a list of words from the text:
	words_list = words.split(' ')

	if index > len(words_list):
		while index > len(words_list):
			index = index - len(words_list)
		secret_word = words_list[index - 1]

	else:
		secret_word = words_list[index - 1]

	return secret_word



def dict_hangman(num_of_tries):
	"""
	The function return the "photo" of the hangman.

	:param num_of_tries: the user's number of guessing
	:type num_of_tries: int
	:return: the photo of the hangman
	:rtype: string
	"""
	HANGMAN_PHOTHOS = {
	'1': """   x-------x""",
	'2': 
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
	
	return HANGMAN_PHOTHOS[str(num_of_tries)]



def check_valid_input(letter_guessed, old_letters_guessed):
	"""
	the function will check if the user typed only one letter
	in English.
	False if:
	1. 2 letters or more
	2. if the "string" contains a symbol
	3. if the letter is already guessed

	:param letter_guessed: input from user
	:type letter_guessed: string
	:param old_letters_guessed: list of the letters already guessed
	:type old_letters_guessed: list
	:return valid_input: True or False acoording the following conditions
	:rtype: bool
	"""

	valid_input = True
	
	if len(letter_guessed) != 1:
		valid_input = False

	elif letter_guessed.isalpha() == False:
		valid_input = False

	elif letter_guessed in old_letters_guessed:
		valid_input = False

	return valid_input
	

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""
	the function will check if the user typed only one letter
	in English.
	False and other printing if:
	1. 2 letters or more
	2. if the "string" contains a symbol
	3. if the letter is already guessed
	ALL OF THIS THE FUNCTION CHECK WITH CHECK_VALID_INPUT()

	:param letter_guessed: input from user
	:type letter_guessed: string
	:param old_letters_guessed: list of the letters already guessed
	:type old_letters_guessed: list
	:param seperator: string of the arrow between the letters
	:type seperator: string
	:return valid_input: True or False acoording the following conditions
	:rtype: bool
	"""

	seperator = ' -> '
	letter_guessed.lower()
	valid_input = check_valid_input(letter_guessed, old_letters_guessed)

	if valid_input == False:
		print('X')
		old_letters_guessed = sorted(old_letters_guessed)
		print(seperator.join(old_letters_guessed))

	elif valid_input == True:
		return valid_input

	



def show_hidden_word(secret_word, old_letters_guessed):
	"""
	the function returns a string that contains underlines and letters
	that show the letters from the list of letters the user guessed
	in their exact location and the other letters the user didn't guess
	as underlines.
		 
	:param secret_word: the secret word the user needs to guess
	:param old_letters_guessed: list of letters the user guessed
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




def check_win(secret_word, old_letters_guessed):
	"""
	the function return True if the letters of the secret
	word are in the letters that the user guessed,
	False if otherwise

	:param secret_word: the secret word the user needs to guess
	:param old_letters_guessed: list of letters the user guessed
	:type secret_word: string
	:type old_letters_guessed: list
	:return boolean: True or False
	:rtype: bool
	"""
	for i in range(0, len(secret_word)):
		if secret_word[i] not in old_letters_guessed:
			win = False
			break

		else:
			win = True

	return win


def main():
	# print the welcome page of the game:
	welcome_page()

	# getting the file route and the index to choose a word from the user for the game:
	file_route_from_user = input('Please enter a file path: ')
	index = int(input('Please enter an index for a word: '))
	secret_word = choose_word(file_route_from_user, index)

	# identify the vars for the game:
	MAX_TRIES = 7
	num_of_tries = 1
	old_letters_guessed = []

	# printing the starting state of the game:
	print("\nLet's Start!", '\n')
	print(dict_hangman(num_of_tries), '\n')
	print(show_hidden_word(secret_word, old_letters_guessed))
	print()
	print("You've Got", (MAX_TRIES - num_of_tries), "Guesses, Good Luck!")

	# while loop until the user doesn't have guesses left
	while num_of_tries < MAX_TRIES:
		print()
		letter_guessed = input('Guess a letter: ')
		letter_guessed = letter_guessed.lower()
		try_update_letter_guessed(letter_guessed, old_letters_guessed)

		# if the user types a valid char but the letter doesn't in the secret word, do this:
		if letter_guessed not in secret_word and check_valid_input(letter_guessed, old_letters_guessed) == True:
			if letter_guessed not in old_letters_guessed:
		#if letter_guessed not in secret_word and letter_guessed.isalpha() == True and len(letter_guessed) < 2:
				num_of_tries += 1
				old_letters_guessed.append(letter_guessed)
				#print('\n')
				print(':(')
				print(dict_hangman(num_of_tries))
				print()
				print(show_hidden_word(secret_word, old_letters_guessed))
				if MAX_TRIES - num_of_tries > 0:
					print('\nYou Have', (MAX_TRIES - num_of_tries), 'Guesses Left!\n')

		elif check_valid_input(letter_guessed, old_letters_guessed) == True:
			old_letters_guessed.append(letter_guessed)
			print(show_hidden_word(secret_word, old_letters_guessed))
			
		# if the user wins, print this and break from the while loop and end the game:
		if check_win(secret_word, old_letters_guessed) == True:
			print('WIN!')
			break
		
	# if the user loses - print this and end the game:
	if num_of_tries == MAX_TRIES:
		print()
		print('LOSE!')
		print('GAME OVER!')
		print('The Word Was:', secret_word.upper())


if __name__ == '__main__':
	main()
