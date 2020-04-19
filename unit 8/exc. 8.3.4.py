# exc. 8.3.4
def inverse_dict(my_dict):
     new_dict = {}
     for key, value in my_dict.items():
          if value in new_dict:
               new_dict[value].append(key)
          else:
               new_dict[value] = [key]
     return new_dict

def main():
     course_dict = {'I': 3, 'love': 3, 'self.py': 2}
     print(inverse_dict(course_dict))


if __name__ == '__main__':
     main()