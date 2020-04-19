# exc. 9.2.3
def who_is_missing(file_name):
	find_the_num = open(file_name, "r")
	numbers = find_the_num.read()
	number_list = [int(x) for x in numbers.split(",")]
	number_list.sort()
	#print(number_list)
	i = number_list[0]
	for num in number_list:
		if i not in number_list:
			found = i
		i += 1
		find_the_num.close()

	new_text = open(r"C:\Users\user\Desktop\found.txt", "w")
	new_text.write(str(found))
	new_text.close()

def main():
	file_name = r"C:\Users\user\Desktop\findMe.txt"
	who_is_missing(file_name)


if __name__ == '__main__':
	main()