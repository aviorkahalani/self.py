# exc. 6.1.2
def shift_left(my_list):
     """
     the function "shift_left()" gets a list 
     and return a new list that is shift left/

     :param my_list: the list that the func get
     :type my_list: list
     :return new_list: the shift left list
     :rtype: list
     """
     new_list = [my_list[1], my_list[2], my_list[0]]
     return new_list


def main():
     my_list = ['monkey', 2.0, 1]
     print(shift_left(my_list))

if __name__ == "__main__":
     main()