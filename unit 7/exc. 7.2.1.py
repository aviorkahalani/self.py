# exc. 7.2.1
def is_greater(my_list, n):
     for num in my_list:
          if num > n:
               print(num)



def main():
     my_list = [1, 30, 25, 60, 27, 28]
     n = 28 
     is_greater(my_list, n)


if __name__ == "__main__":
     main()



def numbers_letters_count(my_str):
     my_list = []
     length_of_string = 0
     num_of_digits = 0
     for num in my_str:
          length_of_string += 1
          if num.isdigit() == True:
               num_of_digits += 1
     my_list = [num_of_digits, length_of_string - 3]
     print(my_list)


def main():
     my_str = 'Python 3.6.3'
     numbers_letters_count(my_str)

if __name__ == "__main__":
     main()

