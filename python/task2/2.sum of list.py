numbers = input("enter: ")
num = numbers.split(',')
num_list = [int(num_str) for num_str in num]
sum = sum(num_list)
print(sum)