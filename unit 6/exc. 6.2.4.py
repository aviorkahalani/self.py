# exc. 6.2.4
def extend_list_x(list_x, list_y):
     """
     THE FUNCTION GETS 2 LISTS AND ADD LIST_Y TO LIST_X

     :param list_x: the first list
     :type list_x: list
     :param list_y: the second list 
     :type list_y: list
     :return: [list_y (+) list_x]
     :rtype: list
     """
     # THE SOLUTION IS THAT I ADD THE LIST_Y BEFORE THE LIST_X BEGINS
     # HOW?
     # IF I SLICE LIST_X BETWEEN IT EVEN BEGINS THERE IS THE SAPCE FOR 
     # LIST_Y TO ENTER THE LIST.
     list_x[:0] = list_y
     return list_x

def main():
     list_x = [4, 5, 6]
     list_y = [1, 2, 3]
     print(extend_list_x(list_x, list_y))




if __name__ == "__main__":
     main()