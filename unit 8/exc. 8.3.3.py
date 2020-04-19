# exc. 8.3.3
def count_chars(my_str):
     my_dict = {}
     for i in my_str:
          if i in my_dict:
               my_dict[i] += 1
          else:
               my_dict[i] = 1
     print(my_dict)

def main():
     magic_str = 'abra cadabra'
     count_chars(magic_str)

if __name__ == '__main__':
     main()
