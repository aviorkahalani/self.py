# exc. 4.2.2
user_word = input('Enter Your Word Here: ')
user_word = user_word.lower()
user_word = user_word.replace(' ', '')
if (user_word[::1] == user_word[::-1]):
     print("OK")
else:
     print("NOT")