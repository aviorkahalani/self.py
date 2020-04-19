# exc. 6.3.2
def longest(my_list):
     """
     THE FUNCTION GETS A LIST OF STRINGS AND RETURN THE LONGEST STRING

     :param my_list: the list the func gets
     :type my_list: list
     :return: the longest string
     :rtype: string
     """
     new_list = sorted(my_list, key=len)
     print(new_list[-1])

def main():
     my_list = ["111", "234", "2000", "goru", "birthday", "09"]
     longest(my_list)

if __name__ == "__main__":
     main()