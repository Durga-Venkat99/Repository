# 3.write a python program to print even and odd separately in list

print("3.print even and odd using list ")
print("  -----------------------------")

# Read a list of integers from the user, separated by spaces
input_str = input("Enter a list: ")

# Split the input string into a list of strings and convert them to integers
num_list = [int(num_str) for num_str in input_str.replace(',',' ').split()]

# Initialize two empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Separate the even and odd numbers
for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print the even numbers
print("Even numbers:", even_numbers)

# Print the odd numbers
print("Odd numbers:", odd_numbers)
