# exc. 8.2.3
def mult_tuple(tuple1, tuple2):
     new_list = []
     for i in range(0, len(tuple1)):
          for j in range(0, len(tuple2)):
               new_list.append((tuple1[i], tuple2[j]))
     for i in range(0, len(tuple2)):
          for j in range(0, len(tuple1)):
               new_list.append((tuple2[i], tuple1[j]))
     print(tuple(new_list))


def main():
     tuple1 = (1, 2, 3)
     tuple2 = (4, 5, 6)
     mult_tuple(tuple1, tuple2)


if __name__ == '__main__':
     main()

