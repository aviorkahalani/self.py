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
