
# exc - 1.4.1 (rolling mission)
>>> import random
>>> print("""
...   _    _
...  | |  | |
...  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
...  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
...  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
...  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
...                       __/ |
...                      |___/
... """
... , random.randint(5,10))



# this is what Python prints:
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/
 6
>>>


# exc - 1.4.2 (rolling mission)
print("""picture 1:
     x-------x""")

print("""picture 2:
     x-------x
     |
     |
     |
     |
     |""")

print("""picture 3:
     x-------x
     |       |
     |       0
     |
     |
     |""")

print("""picture 4:
     x-------x
     |       |
     |       0
     |       |
     |
     |""")

print("""picture 5:
     x-------x
     |       |
     |       0
     |      /|\\
     |
     |""")

print("""picture 6:
     x-------x
     |       |
     |       0
     |      /|\\
     |      /
     |""")

print("""picture 7:
     x-------x
     |       |
     |       0
     |      /|\\
     |      / \\
     |""")


# exc. 2.3.3
# input by the user:
num_of_blocks = input("Enter three digits (each digit for one pig): ")

# divide the digits from the original number:
digit_meot = int(num_of_blocks)/100
digit_temp = int(num_of_blocks)/10
digit_asarot = int(digit_temp)%10
digit_acahdot = int(num_of_blocks)%10

# summing all the digits: 
sum_blocks = (digit_meot) + (digit_asarot)+ (digit_acahdot)
# dividing the blocks for each pig: 
every_pig = int(sum_blocks)/3
# finding the modulo: 
every_pig_pre = int(sum_blocks)%3
# boolean - is it divine without modulo?
bl_tnay = not(int(sum_blocks)%3)

# printing the result:
print (int(sum_blocks))
print(int(every_pig))
print (int(every_pig_pre))
print (bool(bl_tnay))

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


# exc. 2.5.2 (rolling mission)
guess_letter = input("Enter your guess here: ")
print(guess_letter)



# exc. 3.4.2
str = input('Please Enter a String: ')
# 'ddar astronaut. pldase, stop drasing md!'
first_letter = str[0]
str = str[1:]
print((first_letter) + (str.replace('d', 'e')))


# exc. 3.4.3
str = input('Please Enter a String: ')
# 'aviory'
str_center = len(str)//2
str_lower = str[:str_center].lower()
str_upper = str[str_center:].upper()
print(str_lower + str_upper)


# exc. 3.5.1 (rolling mission)
guess_letter = input("Enter your guess here: ")
print(guess_letter.lower())

# exc. 3.5.2 (rolling mission)
guess_word = input('Please Enter Your Word: ')
'hangman'
print('_ '*(len(guess_word)))


# exc. 4.2.2
user_word = input('Enter Your Word Here: ')
user_word = user_word.lower()
user_word = user_word.replace(' ', '')
if (user_word[::1] == user_word[::-1]):
     print("OK")
else:
     print("NOT")

# exc. 4.2.3
temp_degree = input('Insert The Temperature You Would Like to Convert: ')
temp = temp_degree[-1]
temp = temp.upper()
degree = temp_degree[:-1]
degree = float(degree)

c = ((5*degree)-160)/9
f = ((9*degree)+160)/5

if temp=="F":
     print(c,"C", sep='')
elif temp=="C":
     print(f,"F", sep='')
else:
     print('invalid input!')


# exc. 4.2.4
import calendar

user_date = input('Enter a Date in this format - dd/mm/yyyy: ')
day = int(user_date[0:2])
month = int(user_date[3:5])
year = int(user_date[6:])
result = calendar.weekday(year, month, day)

if result == 0:
     print('MONDAY')
elif result == 1:
     print('TUESDAY')
elif result == 2:
     print('WEDNESDAY')
elif result == 3:
     print('THURSDAY')
elif result == 4:
     print('FRIDAY')
elif result == 5:
     print('SATURDAY')
elif result == 6:
     print('SUNDAY ')


# exc. 4.3.1 (Rolling Mission)
guess_letter = input("Enter your guess here: ")
if (len(guess_letter) > 1) and (guess_letter.isalpha()):
     print('E1')
elif (guess_letter.isalpha() == False) and (len(guess_letter) > 1) :
     print('E3')
elif guess_letter.isalpha() == False:
     print('E2')
else:
     guess_letter = guess_letter.lower()
     print(guess_letter)


# exc. 5.3.4
my_str = input('Insert Your String Here: ')
my_str = my_str.lower()
def last_early():
     if my_str[-1] in my_str[0:-2]:
          return True
     else:
          return False
print(last_early())


# exc. 5.3.5
def distance(num1, num2, num3):
     ans1 = abs(num2 - num1)
     ans2 = abs(num2 - num3)
     ans3 = abs(num3 - num1)
     ans4 = abs(num3 - num1)

     if ans1 == 1 or ans3 == 1:
          if ans1 >= 2 and ans2 >= 2 or ans3 >= 2 and ans4 >= 2:
               return True
     return False

print(distance(4, 5, 3))


# exc. 5.3.6
def fix_age(age):
     return 0
    
def filter_teens(a = 13, b = 13, c = 13):
     if (a >= 13 and a <= 19 and a != 15 and a != 16):
          a = fix_age(a) 
     if (b >= 13 and b <= 19 and b != 15 and b != 16):
          b = fix_age(b) 
     if (c >= 13 and c <= 19 and c != 15 and c != 16):
          c = fix_age(c) 
     return (a + b + c)

# exc. 5.3.7
def chocolate_maker(small, big, x):
     if (small*lil_choco + big*big_choco is x):
          return True
     if ((small*lil_choco + big*big_choco)) - x >= 1:
          return True
     else:
          return False

lil_choco = 1
big_choco = 5

chocolate_maker(3, 2, 10)

# exc. 5.4.1
num1 = 10
num2 = 2
def func(num1, num2):
     """
     the function will divide two given numbers
     with each others and print the result

     :param num1: the first number
     :type num1: int
     :param num2: the second number
     :type num2: int
     :return: the result of dividing the 2 numbers/
     :rtype: float
     """
     print (num1 / num2)
      
def main():
     func(10, 2)

if __name__ == "__main__":
     main()


# exc. 5.5.1 (Rolling Mission)
def is_valid_input(letter_guessed):
     """
     the function will check if the user typed only one letter
     in english.
     False if:
     1. 2 letters or more/
     2. if the "string" contains a symbol

     :param boolean: save the answer (T/F)
     :type boolean: bool
     :return: the result - True or False
     :rtype: bool
     """
     if len(letter_guessed) > 1:
          boolean = False
          print(boolean)
     elif letter_guessed.isalpha() == False and len(letter_guessed) >= 1:
          boolean = False
          print(boolean)
     elif letter_guessed.isalpha() == True and len(letter_guessed) == 1:
          boolean = True
          print(boolean)

def main():
     letter_guessed = input('Please Enter Your Guess Here: ')
     letter_guessed = letter_guessed.lower()
     is_valid_input(letter_guessed)

if __name__ == "__main__":
     main()


# exc. 6.1.2
def shift_left(my_list):
     """
     the function "shift_left()" gets a list 
     and return a new list that is shift left/

     :param my_list: the list that the func get
     :type my_list: list
     :return new_list: the shift left list
     :rtype: list
     """
     new_list = [my_list[1], my_list[2], my_list[0]]
     return new_list


def main():
     my_list = ['monkey', 2.0, 1]
     print(shift_left(my_list))

if __name__ == "__main__":
     main()



# exc. 6.2.3
def format_list(my_list):
      """
     THE FUNCTION GETS A LIST WITH EVEN LENGTH 
     OF LIST AND RETURN ONLY THE EVEN LIMBS.

     :param seperator: add ", " to the new sring
     :type seperator: sring 
     :param last_limb: take the last limb from the list and add a ' and ' before
     :type last_limb: string
     :return: a new string with the even limbs and the last one 
     :rtype: string 
     """
     seperator = ', '
     seperator = (seperator.join(my_list[0::2]))
     last_limb = str(my_list[-1])
     last_limb = ' and ' + last_limb
     new_list = seperator + last_limb
     return(new_list)


def main():
     my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
     print(format_list(my_list))

if __name__ == "__main__":
     main()


# exc. 6.2.4
def extend_list_x(list_x, list_y):
     """
     THE FUNCTION GETS 2 LISTS AND ADD LIST_Y TO LIST_X

     :param list_x: the first list
     :type list_x: list
     :param list_y: the second list 
     :type list_y: list
     :return: [list_y (+) list_x]
     :rtype: list
     """
     # THE SOLUTION IS THAT I ADD THE LIST_Y BEFORE THE LIST_X BEGINS
     # HOW?
     # IF I SLICE LIST_X BETWEEN IT EVEN BEGINS THERE IS THE SAPCE FOR 
     # LIST_Y TO ENTER THE LIST.
     list_x[:0] = list_y
     return list_x

def main():
     list_x = [4, 5, 6]
     list_y = [1, 2, 3]
     print(extend_list_x(list_x, list_y))




if __name__ == "__main__":
     main()



# exc. 6.3.1
def are_lists_equal(list1 = [], list2 = [], list3 = []):
     """
     THE FUNCTION GETS 3 LISTS AND RETURN IF 2 OF THEM ARE EQUAL.

     :param list1: first list
     :type list1: list
     :param list2: second list
     :type list2: list
     :param list3: list
     :type list3: list
     :return: True or False
     :rtype: boolean
     """
     list1.sort()
     list2.sort()
     list3.sort()

     if list1 == []:
          list1 = list3
     elif list2 == []:
          list2 = list3

     if list1 == list2:
          return True
     else:
          return False

def main():
     list1 = [0.6, 1, 2, 3]
     list2 = []
     list3 = [9, 0, 5, 10.5]
     print(are_lists_equal(list1, list2, list3))

if __name__ == "__main__":
     main()



# exc. 6.3.2
def longest(my_list):
     """
     THE FUNCTION GETS A LIST OF STRINGS AND RETURN THE LONGEST STRING

     :param my_list: the list the func gets
     :type my_list: list
     :return: the longest string
     :rtype: string
     """
     new_list = sorted(my_list, key=len)
     print(new_list[-1])

def main():
     my_list = ["111", "234", "2000", "goru", "birthday", "09"]
     longest(my_list)

if __name__ == "__main__":
     main()



# exc. 6.4.1 (Rolling Mission)
def check_valid_input(letter_guessed, old_letter_guessed):
     """
     the function will check if the user typed only one letter
     in english.
     False if:
     1. 2 letters or more
     2. if the "string" contains a symbol
     3. if the letter is already guessed

     :param letter_guessed: input from user
     :type letter_guessed: string
     :param old_letter_guessed: list of the letters already guessed
     :type old_letter_guessed: list
     :param boolean: save the answer (T/F)
     :type boolean: bool
     :return: the result - True or False
     :rtype: bool
     """
     letter_guessed.lower()
     if len(letter_guessed) > 1:
          boolean = False
          print(boolean)
     elif letter_guessed.isalpha() == False and len(letter_guessed) >= 1:
          boolean = False
          print(boolean)
     elif letter_guessed in old_letter_guessed:
          boolean = False
          print(boolean)
     elif letter_guessed.isalpha() == True and len(letter_guessed) == 1:
          boolean = True
          print(boolean)


def main():
     old_letter_guessed = ['a', 'b', 'c']
     letter_guessed = input('Please Enter Your Guess Here: ')
     check_valid_input(letter_guessed, old_letter_guessed)

if __name__ == "__main__":
     main()



# exc. 6.4.2 (Rolling Mission)
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
     """
     the function will check if the user typed only one letter
     in english.
     False and other printing if:
     1. 2 letters or more
     2. if the "string" contains a symbol
     3. if the letter is already guessed

     :param letter_guessed: input from user
     :type letter_guessed: string
     :param old_letter_guessed: list of the letters already guessed
     :type old_letter_guessed: list
     :param boolean: save the answer (T/F)
     :type boolean: bool
     :return: the result - True or False
     :rtype: bool    
     """
     seperator = ' -> '
     if len(letter_guessed) > 1:
          print('X')
          print(seperator.join(old_letters_guessed))
          print('False')
     elif letter_guessed.isalpha() == False and len(letter_guessed) >= 1:
          print('X')
          print(seperator.join(old_letters_guessed))
          print('False')
     elif letter_guessed.lower() in old_letters_guessed:
          print('X')
          print(seperator.join(old_letters_guessed))
          print('False')
     elif letter_guessed.isalpha() == True and len(letter_guessed) == 1:
          print('True')
          old_letters_guessed.append(letter_guessed)
          print("Old Letters: ", old_letters_guessed)


def main():
     old_letters_guessed = ['a', 'p', 'c', 'f']
     #try_update_letter_guessed('A', old_letters_guessed)
     #try_update_letter_guessed('s', old_letters_guessed)
     #try_update_letter_guessed('$', old_letters_guessed)
     try_update_letter_guessed('d', old_letters_guessed)


if __name__ == "__main__":
     main()



# exc. 7.1.4
def squared_numbers(start, stop):
     while start <= stop:
          print(start**2)
          start += 1


def main():
     start = -3 
     stop = 3
     squared_numbers(start, stop)

if __name__ == "__main__":
     main()



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



# exc. 7.2.4
def seven_boom(end_number):
     my_list = []
     for i in range(0, end_number + 1):
          s = str(i)
          if '7' in s or i % 7 == 0:
               my_list += ['BOOM']
          else:
               my_list += [i]
     print(my_list)


def main():
     end_number = 17
     seven_boom(end_number)

if __name__ == "__main__":
     main()



# exc. 7.2.5
def sequence_del(my_str):
     new_string = ""
     prev_char = None
     for letter in my_str:
          if letter != prev_char:
              new_string += letter
              prev_char = letter
     print(new_string)

def main():
     my_str = 'Heeyyy   yyouuuu!!!'
     sequence_del(my_str)

if __name__ == "__main__":
     main()



# exc. 7.2.6
def activities_for_costumer(user_string):
     user_digit = int(input('PLEASE ENTER YOUR DIGIT: '))
     if user_digit != 9:
          if user_digit == 1:
               user_list = user_string.split()
               print(user_list)
               main()
          elif user_digit == 2:
               user_list = user_string.split(',')
               print(len(user_list))
               main()
          elif user_digit == 3:
               check_product = input('Check a Product: ')
               boolean = False
               if check_product in user_string:
                    boolean = True
               print(boolean)
               main()
          elif user_digit == 4:
               check_count = input('Which Product to check: ')
               user_list = user_string.split(',')
               count = 0
               for i in user_list:
                    if i == check_count:
                         count += 1 
               print(count)
               main()
          elif user_digit == 5:
               user_list = user_string.split(',')
               remove_product = input('which Product to Remove: ')
               user_list.remove(remove_product)
               print(user_list)
               main()
          elif user_digit == 6:
               user_list = user_string.split(',')
               add_product = input('Which Product to Add: ')
               user_list.append(add_product)
               print(user_list)
               main()
          elif user_digit == 7:
               user_list = user_string.split(',')
               new_list = []
               for i in user_list:
                    if len(i) < 3 or i.isalpha() == False:
                         print(i)
               main()
          elif user_digit == 8:
               user_list = user_string.split(',')
               new_user_list = []
               for product in user_list:
                    if product not in new_user_list:
                         new_user_list.append(product)
               print(new_user_list)
               main()
     else:
          print('Thank You! See You Next Time...')
               


def main():
     user_string = "Milk,Cottage,Tomatoes,Milk"
     #user_digit = int(input('PLEASE ENTER YOUR DIGIT: '))
     activities_for_costumer(user_string)

if __name__ == "__main__":
     main()



# exc. 7.2.7
def arrow(my_char, max_length):
     for i in range(1, max_length+1):
         for j in range(1, i+1):
               print(my_char, end = ' ')
         print()
     for i in range(max_length, 1, -1):
         for j in range(1, i):
               print(my_char, end = ' ')
         print() 
          

def main():
     my_char = input('insert a char: ')
     max_length = int(input('insert max length: '))
     arrow(my_char, max_length)


if __name__ == "__main__":
     main()


# exc. 7.3.1 (Rolling Mission)
def show_hidden_word(secret_word, old_letters_guessed):
     new_word = ''
     for i in range(0, len(secret_word)):
          if secret_word[i] in old_letters_guessed:
               new_word += secret_word[i] + " "
          elif secret_word[i] not in old_letters_guessed:
               new_word += " _ "
     return new_word

def main():
     secret_word = "mammalas"
     old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
     print(show_hidden_word(secret_word, old_letters_guessed))

if __name__ == "__main__":
     main()


# exc. 7.3.2 (Rolling Mission)
def check_win(secret_word, old_letters_guessed):
     for i in range(0, len(secret_word)):
          if secret_word[i] in old_letters_guessed:
               boolean = True
          else:
               boolean = False
          return boolean

def main():
     secret_word = 'friends'
     old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
     print(check_win(secret_word, old_letters_guessed))

if __name__ == '__main__':
     main()

# exc. 8.2.1
data = ('self', 'py', 1.543)
format_string = 'Hello'
print(format_string + ' %s.%s learner, you have only %.1f units left before you master the course!' %(data))


# exc. 8.2.2
def take_second(elem):
     return elem[1]

def sort_prices(list_of_tuples):
     print(sorted(list_of_tuples, key = take_second, reverse = True))

def main():
     products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
     sort_prices(products)

if __name__ == '__main__':
     main()


# exc. 8.2.3
def mult_tuple(tuple1, tuple2):
     new_list = []
     for i in range(0, len(tuple1)):
          for j in range(0, len(tuple2)):
               new_list.append((tuple1[i], tuple2[j]))
     for i in range(0, len(tuple2)):
          for j in range(0, len(tuple1)):
               new_list.append((tuple2[i], tuple1[j]))
     print(tuple(new_list))


def main():
     tuple1 = (1, 2, 3)
     tuple2 = (4, 5, 6)
     mult_tuple(tuple1, tuple2)


if __name__ == '__main__':
     main()



# exc. 8.2.4
def sort_anagrams(list_of_strings):
     i = 0
     new_list = [list_of_strings[i]]
     for word in list_of_strings[1:]:
          if sorted(list_of_strings[0]) == sorted(word):
               new_list.append(word)
               """
          for j in list_of_strings:
               if sorted(i) == sorted(j):
                    new_list.append([i])
                    """
     print(new_list)


def main():
     list_of_strings = ['deltas', 'retainers', 'desalt',
     'pants', 'slated', 'generating', 
     'ternaries', 'smelters', 'termless', 
     'salted', 'staled', 'greatening', 
     'lasted', 'resmelts']
     sort_anagrams(list_of_strings)


if __name__ == '__main__':
     main()


# exc. 8.3.2
def dict_options(my_dict, user_digit):
     if user_digit == '1':
          print("HER LAST NAME: ", my_dict["last_name"])
          main()

     if user_digit == '2':
          print("BORN ON MONTH: ", my_dict["birth_date"][3:5])
          main()

     if user_digit == '3':
          mone = 0
          for i in my_dict["hobbies"]:
               mone += 1
          print('NUMBER OF HOBBIES: ', mone)
          main()

     if user_digit == '4':
          print(my_dict["hobbies"][-1])
          main()

     if user_digit == '5':
          my_dict["hobbies"].append('Cooking')
          print(my_dict["hobbies"])
          main()

     if user_digit == '6':
          my_dict["birth_date"] = (27, 3, 1970)
          print(my_dict["birth_date"])
          main()

     if user_digit == '7':
          my_dict["age"] = 49
          print("MARIAH CAREY IS", my_dict["age"], "YEARS OLD")
          main()


def main():
     my_dict = {"first_name": "Mariah", "last_name": "Carey",
               "birth_date": "27.03.1970", 
               "hobbies": ['Sing', 'Compose', 'Act']}
     user_digit = input('INSERT A DIGIT: ')
     dict_options(my_dict, user_digit)

if __name__ == '__main__':
     main()


# exc. 8.3.3
def count_chars(my_str):
     my_dict = {}
     for i in my_str:
          if i in my_dict:
               my_dict[i] += 1
          else:
               my_dict[i] = 1
     print(my_dict)

def main():
     magic_str = 'abra cadabra'
     count_chars(magic_str)

if __name__ == '__main__':
     main()


# exc. 8.3.4
def inverse_dict(my_dict):
     new_dict = {}
     for key, value in my_dict.items():
          if value in new_dict:
               new_dict[value].append(key)
          else:
               new_dict[value] = [key]
     return new_dict

def main():
     course_dict = {'I': 3, 'love': 3, 'self.py': 2}
     print(inverse_dict(course_dict))


if __name__ == '__main__':
     main()



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


# exc. 9.3.2
def my_mp3_playlist(file_path):
     BIG_LIST = []
     songs_list = []
     songs_text = open(file_path, 'r')
     songs_data = [line.split(';') for line in songs_text.readlines()]
     # find the longest song:
     length_of_songs = []
     for longer in range(0, len(songs_data)):
          length = songs_data[longer][2]
          length = length.replace(":", "")
          length_of_songs.append(length)
     longest = max(length_of_songs)
     index = length_of_songs.index(longest)
     #print('The longest song is: ', songs_data[index][0])
     BIG_LIST.append(songs_data[index][0])
     # number of songs:
     number = len(songs_data)
     #print('Number of songs: ', number)
     BIG_LIST.append(number)
     # find the most frequent:
     count_list = []
     for band in range(0, len(songs_data)):
          name_of_band = songs_data[band][1]
          count_list.append(name_of_band)
     counter = 0
     num = count_list[0]

     for y in count_list:
          curr_frequency = count_list.count(y)
          if curr_frequency > counter:
               counter = curr_frequency
               num = y
     #print('The most frequent band is: ', num)
     BIG_LIST.append(num)
     print(tuple(BIG_LIST))


def main():
     file_path = r'C:\Users\user\Desktop\songs.txt'
     my_mp3_playlist(file_path)


if __name__ == '__main__':
     main()