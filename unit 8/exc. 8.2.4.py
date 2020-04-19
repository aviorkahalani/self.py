# exc. 8.2.4
def sort_anagrams(list_of_strings):
     i = 0
     new_list = [list_of_strings[i]]
     for word in list_of_strings[1:]:
          if sorted(list_of_strings[0]) == sorted(word):
               new_list.append(word)
               """
          for j in list_of_strings:
               if sorted(i) == sorted(j):
                    new_list.append([i])
                    """
     print(new_list)


def main():
     list_of_strings = ['deltas', 'retainers', 'desalt',
     'pants', 'slated', 'generating', 
     'ternaries', 'smelters', 'termless', 
     'salted', 'staled', 'greatening', 
     'lasted', 'resmelts']
     sort_anagrams(list_of_strings)


if __name__ == '__main__':
     main()

