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