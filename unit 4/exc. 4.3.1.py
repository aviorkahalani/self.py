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
