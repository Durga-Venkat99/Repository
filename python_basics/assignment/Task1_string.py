# write a python program to remove a given character from string

print("1. A given character remove from string")
print("   ------------------------------------")
string = input("enter : ")
char = input("remove: ")
new_str = string.replace(char,"")
print(new_str)

print()
print()

# Write a program to check String is Palindrome or not.
print("2.palindrome or not")
print("  -----------------")

word = input("name : ")
word_lower = word.lower()
reverse = word_lower[::-1]

if word == reverse:
    print("it's a palindrome")
else:
    print("it's not a palindrome")

print()
print()

# 3.Write a python program to check given character is vowel or consonant
print("3.Write a python program to check given character is vowel or consonant")
print(" ----------------------------------------------------------------------")

char = input("Enter a  character: ")
char_lower = char.lower()       # Convert the character to lowercase for case-insensitive comparison
is_aplpha = char_lower.isalpha()

if char_lower in 'aeiou':
    print(f"the character '{char}' is a vowel")
else:
    print(f"the character '{char}' is a constant")

print()
print()

# 4.Write a python program to replace string space with given character in Python.
print("4.Write a python program to replace string space with given character in Python.")
print(" ------------------------------------------------------------------------------")

name = input("enter : ")
change = input("enter the replacement name: ")
replace = input("enter the replace: ")
new_name = name.replace(change,replace)
print("result : ",new_name)

print()
print()

# 5.Write a python program to count alphabets, digits, and special characters in the string.
print("5.Write a python program to count alphabets, digits, and special characters in the string.")
print(" ----------------------------------------------------------------------------------------")
alphabet = input("alpha : ")
alpha = alphabet
digit = input("digit: ")
number = digit
specialcharacters = input("spl_char: ")
char = specialcharacters
print(alphabet.count(alpha))
print(digit.count(number))
print(specialcharacters.count(char))

print()
print("________________________________________________________________")
print()
ads = input("string: ")
alphabet = 0
digits = 0
spl_character = 0

for char in ads:
    if char.isalpha():
        alphabet += 1
    elif char.isdigit():
        digits += 1
    else:
        spl_character += 1

print("the alphabet of count time is",alphabet)
print("the digit of the count is: ",digits)
print("the special character of the count is :",spl_character)

print()
print()

# 6.write a program to remove spaces from string
print("6.remove spaces from string")
print("   ------------------------------------")
string = input("enter : ")
char = input("remove: ")
new_str = string.replace(char,"")
print(new_str)

print()
print()

# 7.Write a python program to find sum of integers in the string
print("7.find sum of integers in the string")
print(" -----------------------------------")

str1 = int(input("str1 : "))
str2 = int(input("str2 : "))

print("sum of string :",str1+str2)
print("sum of string :",str1*str1)
print("sum of string :",str1%str2)

print()
print()

# 8.Write a python program to Remove Repeated Character from String.

print("8.Remove Repeated Character from String.")
print(" --------------------------------------")

character = input("enter: ")
unique_charc = ""

for char in character:
    if char not in unique_charc:
        unique_charc += char
print(unique_charc)

# unique_charc = "establise the emporer"

print()
print()

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

print()
print()

# 10.Write a python program to check string is anagrams or not in Python.

print("10.check string is anagrams or not in Python.")
print(" -------------------------------------------")

str1 = input("the anagram of str1: ")
str2 = input("the anagram of str2: ")

if str1 != str2:
    print("the strings are anagrams")
else:
    print("the strings are not anagrams")

    if str1 == str2:
        print("the strings are anagrams")
    else:
        print("the strings are not anagrams")

# good = bad, listen = silent, mute =umute
