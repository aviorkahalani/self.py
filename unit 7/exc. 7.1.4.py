# exc. 7.1.4
def squared_numbers(start, stop):
     while start <= stop:
          print(start**2)
          start += 1


def main():
     start = -3 
     stop = 3
     squared_numbers(start, stop)

if __name__ == "__main__":
     main()