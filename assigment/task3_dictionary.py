# 1.Write a Python script to add a key to a dictionary

print("1.add a key to a dictionary")
print("  -------------------------")

d = {0 : 10,1 : 20}

key = int(input("key : "))
value = int(input("value : "))

d[key] = value

print(d)

print()
print()

# 2.Write a Python script to check whether a given key already exists in a dictionary.

print("2.script to check whether a given key already exists in a dictionary.")
print("  ------------------------------------------------------------------")

d = {0 : 10,1 : 20}

check = 1

if check in d:
    print("the key ",check,"exists in dictionary")
else:
    print("the key ",check,"doesn't exists in dictionary")

print()
print()

# 3.Write a Python program to iterate over dictionaries using for loops

print("3.iterate over dictionaries using for loops")
print(" ------------------------------------------")
 
loop = {'a': 1, 'b': 2, 'c': 3}

for key in loop:
    print(key)

print("--------------------------------------------------------------")

loop = {'a': 1, 'b': 2, 'c': 3}

for value in loop.values():
    print(value)

print("--------------------------------------------------------------")

loop = {'a': 1, 'b': 2, 'c': 3}

for items in loop.items():
    print(items)

print('-------------------------------------------------------------')

loop = {'a': 1, 'b': 2, 'c': 3}

for key, value in loop.items():
    print(f'Key: {key}, Value: {value}')

print()
print()

# 4.write a Python script to print a dictionary with keys as numbers between 1 and 15(both included) and the values are the square of the keys

print("4.the dictionary with keys and square the key")
print(" --------------------------------------------")

dict = {}

for num in range(1,16):
    dict[num] = num ** 2
print(dict)

print()
print()

# 5.Write a Python program to create a dictionary from a string # 5.Write a Python program to create a dictionary from a string

print("5.Track the count of the letters from the string")
print("  ----------------------------------------------")

letter = input("letter: ")

dict = {}

for char in letter:
    if char.isalpha():
        char = char.lower()

        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
print(dict)

print()
print()

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

print()
print()

# 7.Write a Python program to combine two dictionary by adding values for common keys

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
print()

# 8.Write a Python program to access dictionary key's element by index

print("8.access dictionary key's element by index")
print("  ----------------------------------------")

dict = {}

items = int(input("enter items: "))
for n in range(items):
    key = input("enter key: ")
    value = input("enter value: ")
    dict[key] = value
order = input("enter the order of keys separated:").replace(',',' ').split()
for key in order:
    print(dict[key])

print()
print()

# 9. write a program to remove a key from dictionary 

print("9.remove a key from dictionary")
print(" -----------------------------")
my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_remove = 'b'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")
print("Updated Dictionary:", my_dict)

print()
print()

# 10.Write a Python script to merge two Python dictionaries

print("10.merge two python dictionaries")
print("  ------------------------------")

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6}

dict1.update(dict2)

print("Merged Dictionary:", dict1)
