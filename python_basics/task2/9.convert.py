# 9.Write a Python program to convert a list of multiple integers into a single integer.

print("9.Write a Python program to convert a list of multiple integers into a single integer")
print("  -----------------------------------------------------------------------------------")

integer_list = input("Enter a list of integers separated by spaces: ").replace(',',' ').split()

result =  ''.join(integer_list)

integer = int(result)
print(integer)