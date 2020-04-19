# exc. 9.4.1 (Rolling Mission)
def choose_word(file_path, index):
	"""
	the function gets a string that represent a file route
	and a number represent index of a word in the file.
	the function return a tuple of:
	1) number of different words in the file
	2) a word given by the index
	"""

	# for the rolling mission i need to delete this section:
	text = open(file_path, 'r')
	words = text.read()
	choosen_word = ''
	# creating a list of words from the text:
	words_list = words.split(' ')
		
	if index > len(words_list):
		while index > len(words_list):
			index = index - len(words_list)
		choosen_word = words_list[index - 1]
	else:
		choosen_word = words_list[index - 1]
	
	return choosen_word
	


def main():
	file_path = r'C:\Users\כהלני\Desktop\self.py\unit 9\words.txt'
	index = int(input('Enter a number: '))
	print(choose_word(file_path, index))

if __name__ == '__main__':
	main()