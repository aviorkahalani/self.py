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

