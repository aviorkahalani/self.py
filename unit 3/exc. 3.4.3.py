# exc. 3.4.3
str = input('Please Enter a String: ')
# 'aviory'
str_center = len(str)//2
str_lower = str[:str_center].lower()
str_upper = str[str_center:].upper()
print(str_lower + str_upper)