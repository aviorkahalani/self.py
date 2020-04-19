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