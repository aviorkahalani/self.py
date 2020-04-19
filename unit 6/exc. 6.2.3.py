# exc. 6.2.3
def format_list(my_list):
      """
     THE FUNCTION GETS A LIST WITH EVEN LENGTH 
     OF LIST AND RETURN ONLY THE EVEN LIMBS.

     :param seperator: add ", " to the new sring
     :type seperator: sring 
     :param last_limb: take the last limb from the list and add a ' and ' before
     :type last_limb: string
     :return: a new string with the even limbs and the last one 
     :rtype: string 
     """
     seperator = ', '
     seperator = (seperator.join(my_list[0::2]))
     last_limb = str(my_list[-1])
     last_limb = ' and ' + last_limb
     new_list = seperator + last_limb
     return(new_list)


def main():
     my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
     print(format_list(my_list))

if __name__ == "__main__":
     main()