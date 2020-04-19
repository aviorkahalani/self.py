# exc. 8.2.2
def take_second(elem):
     return elem[1]

def sort_prices(list_of_tuples):
     print(sorted(list_of_tuples, key = take_second, reverse = True))

def main():
     products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
     sort_prices(products)

if __name__ == '__main__':
     main()