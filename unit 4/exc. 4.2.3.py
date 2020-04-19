# exc. 4.2.3
temp_degree = input('Insert The Temperature You Would Like to Convert: ')
temp = temp_degree[-1]
temp = temp.upper()
degree = temp_degree[:-1]
degree = float(degree)

c = ((5*degree)-160)/9
f = ((9*degree)+160)/5

if temp=="F":
     print(c,"C", sep='')
elif temp=="C":
     print(f,"F", sep='')
else:
     print('invalid input!')