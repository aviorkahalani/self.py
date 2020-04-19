# exc. 2.3.3
# input by the user:
num_of_blocks = input("Enter three digits (each digit for one pig): ")

# divide the digits from the original number:
digit_meot = int(num_of_blocks)/100
digit_temp = int(num_of_blocks)/10
digit_asarot = int(digit_temp)%10
digit_acahdot = int(num_of_blocks)%10

# summing all the digits: 
sum_blocks = (digit_meot) + (digit_asarot)+ (digit_acahdot)
# dividing the blocks for each pig: 
every_pig = int(sum_blocks)/3
# finding the modulo: 
every_pig_pre = int(sum_blocks)%3
# boolean - is it divine without modulo?
bl_tnay = not(int(sum_blocks)%3)

# printing the result:
print (int(sum_blocks))
print(int(every_pig))
print (int(every_pig_pre))
print (bool(bl_tnay))