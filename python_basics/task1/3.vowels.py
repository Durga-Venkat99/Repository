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