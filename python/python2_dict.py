# 1. python script on a key to a dictionary

d = {0:10,1:20}

key = 2
value = 30

d[key] = value
print(d)

print("-----------------------------------------------------------------------------------------------------------------")

# 2. python script to check given key already exists in a dictionary

d = {0:10,1:20}
check = 1
if check in d:
    print("yes,it already exists")
else:
    print("it doesn't exists")
    
print("-----------------------------------------------------------------------------------------------------------------")

# 3. iterator over dictionary using for loops

loop = {'a':1,'b': 2,'c':3}

for key in loop:
    print(key)
    
print("---------------------------------------------------------------------")

for value in loop.values():
    print(value)
    
print("---------------------------------------------------------------------")

for key,value in loop.items():
    print(f"key:{key},value:{value}")

print("-----------------------------------------------------------------------------------------------------------------")

# 4. print a dictionary with keys as number between 1 and 15 and values are the square of the keys
dict = {}

for num in range(1,16):
    dict[num] = num**2
print(dict)

print("-----------------------------------------------------------------------------------------------------------------")

# 5. track the coount of letters from the string

letters = "marolix technology"

dict1 = {}

for char in letters:
    if char.isalpha():
        char = char.lower()
        
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1
print(dict1)