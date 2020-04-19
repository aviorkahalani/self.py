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
