# exc. 7.2.4
def seven_boom(end_number):
     my_list = []
     for i in range(0, end_number + 1):
          s = str(i)
          if '7' in s or i % 7 == 0:
               my_list += ['BOOM']
          else:
               my_list += [i]
     print(my_list)


def main():
     end_number = 17
     seven_boom(end_number)

if __name__ == "__main__":
     main()
