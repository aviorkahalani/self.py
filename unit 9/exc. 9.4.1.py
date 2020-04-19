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
	"""
	text = open(file_path, 'r')
	words = text.read()
	temp_list = []
	# creating a list of words from the text:
	words_list = words.split(' ')
	# by adding all the words that arent in new_list i get rid of double words:
	new_list = []
	for i in words_list:
		if i not in new_list:
			new_list.append(i)
	num_of_unique_words = len(new_list)
	"""
	"""
	#temp_list.append(num_of_unique_words)
	

	# print the word for the the first word:
	# the first way using % operator:
	"""
	if index > len(words_list):
		index = index % len(words_list)
		temp_list.append(words_list[index - 1])
	else:
		temp_list.append(words_list[index - 1])
	"""
	# the second way using While loop:
	if index > len(words_list):
		while index > len(words_list):
			index = index - len(words_list)
		temp_list.append(words_list[index - 1])
	else:
		temp_list.append(words_list[index - 1])

	return tuple(temp_list)
	


def main():
	file_path = r'C:\Users\כהלני\Desktop\self.py\unit 9\words.txt'
	index = int(input('Enter a number: '))
	print(choose_word(file_path, index))

if __name__ == '__main__':
	main()