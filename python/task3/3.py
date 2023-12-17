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
