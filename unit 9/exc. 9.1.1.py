# exc. 9.1.1
def are_files_equal(file1, file2):
	f_1 = open(file1, 'r')
	f_2 = open(file2, 'r')
	if f_1.read() == f_2.read():
		return True
	else:
		return False
	f_1.close()
	f_2.close()

def main():
	file1 = "C:\\Users\\user\\Desktop\\vacation.txt"
	file2 = "C:\\Users\\user\\Desktop\\work.txt"
	print(are_files_equal(file1, file2))

if __name__ == '__main__':
	main()

