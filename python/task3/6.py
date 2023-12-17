# 6.Write a Python program to sum all the items in a dictionary.

print("6.sum of all the items in a dictionary")
print("  ------------------------------------")

dict = {}

items = int(input("enter items in dictionary: "))

for n in range(items):
    key = input("enter a key: ")
    value = int(input("enter a value: "))
    dict[key] = value

total = 0

for value in dict.values():
    total += value

print("dictionary: ", dict)
print("sum of all dictionary: ",total)