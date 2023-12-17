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