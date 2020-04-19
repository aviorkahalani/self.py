# exc. 7.2.7
def arrow(my_char, max_length):
     for i in range(1, max_length+1):
         for j in range(1, i+1):
               print(my_char, end = ' ')
         print()
     for i in range(max_length, 1, -1):
         for j in range(1, i):
               print(my_char, end = ' ')
         print() 
          

def main():
     my_char = input('insert a char: ')
     max_length = int(input('insert max length: '))
     arrow(my_char, max_length)


if __name__ == "__main__":
     main()
