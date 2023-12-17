# 9.Write a python program to count occurrence of given character in string.

print("9.count occurrence of given character in string.")
print(" ----------------------------------------------")

input_string = input("Enter a string: ")
character_to_count = input("Enter the character to count: ")
count = 0
for char in input_string:
    if char == character_to_count:
        count += 1

print(f"The character '{character_to_count}' appears {count} times in the string.")

print("----------------------------------------------------------")

# 2

string = input("enter string: ")
mystring = input("enter mystring: ")
count = string.count(mystring)
print(count)