# exc. 5.3.4
my_str = input('Insert Your String Here: ')
my_str = my_str.lower()
def last_early():
     if my_str[-1] in my_str[0:-2]:
          return True
     else:
          return False
print(last_early())