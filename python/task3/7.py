# 7.Write a Python program to combine two dictionary by adding values for common keys
'''
print("7.combine two dictionary by adding values for common keys")
print("  -------------------------------------------------------")

from collections import Counter
d1 = {}
item1 = int(input("number items: "))
for n in range(item1):
    key = input("enter key: ")
    value = int(input("enter the value: "))
    d1[key] = int(value)

d2 = {}
item2 = int(input("number items: "))
for n in range(item2):
    key = input("enter key: ")
    value = int(input("enter the value: "))
    d2[key] = int(value)

result = Counter(d1) + Counter(d2)

print(result)

print()
print(80*"-")
print()
'''
dict0 = {}
item1 = int(input("enter items: "))
for n in range(item1):
    key = input("enter key: ")
    value = input("enter value: ")
    dict0[key] = value

dict1 = {}
item2 = int(input("enter items: "))
for n in range(item2):
    key = input("enter key: ")
    value = input("enter value: ")
    dict1[key] = value

for key in dict0:
    if key in dict1:
        dict1[key] = dict1[key] + dict0[key]
    else:
        pass
print(dict1)