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