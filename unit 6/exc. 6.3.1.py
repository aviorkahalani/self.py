# exc. 6.3.1
def are_lists_equal(list1 = [], list2 = [], list3 = []):
     """
     THE FUNCTION GETS 3 LISTS AND RETURN IF 2 OF THEM ARE EQUAL.

     :param list1: first list
     :type list1: list
     :param list2: second list
     :type list2: list
     :param list3: list
     :type list3: list
     :return: True or False
     :rtype: boolean
     """
     list1.sort()
     list2.sort()
     list3.sort()

     if list1 == []:
          list1 = list3
     elif list2 == []:
          list2 = list3

     if list1 == list2:
          return True
     else:
          return False

def main():
     list1 = [0.6, 1, 2, 3]
     list2 = []
     list3 = [9, 0, 5, 10.5]
     print(are_lists_equal(list1, list2, list3))

if __name__ == "__main__":
     main()
