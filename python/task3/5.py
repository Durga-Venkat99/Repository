# 5.Write a Python program to create a dictionary from a string

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