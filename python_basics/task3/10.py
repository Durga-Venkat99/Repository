# 10.Write a Python script to merge two Python dictionaries

print("10.merge two python dictionaries")
print("  ------------------------------")

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5, 'e': 6}

dict1.update(dict2)

print("Merged Dictionary:", dict1)