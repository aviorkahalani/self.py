# exc. 9.1.2
def file_options(file_name, task):
	if task == 'sort':
		edit_file = open(file_name, 'r')
		file_list = edit_file.read().split(' ') 
		print(sorted(file_list))
		edit_file.close()

	elif task == 'rev':
		edit_file = open(file_name, 'r')
		for line in edit_file:
			print(line[::-1])
		edit_file.close()

	elif task == 'last':
		n = int(input('Enter a number: '))
		n = n * (-1)
		file_list = []
		edit_file = open(file_name, 'r')
		for line in edit_file:
			file_list += [line]
		file_list = file_list[n:]
		for line in file_list:
			print(line)
		#print(file_list[n:], sep="\n")

def main():
	file_name = "C:\\Users\\user\\Desktop\\sampleFile.txt"
	task = input('Enter a task: ')
	file_options(file_name, task)

if __name__ == '__main__':
	main()