# exc. 3.4.2
str = input('Please Enter a String: ')
# 'ddar astronaut. pldase, stop drasing md!'
first_letter = str[0]
str = str[1:]
print((first_letter) + (str.replace('d', 'e')))