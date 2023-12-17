# 1.write a python program to merge two list

print("1.merge two list")
print("----------------")
list1 = list(eval(input("enter list1: ")))
list2 = list(eval(input("enter list2: ")))
print(list1+list2)
list1.extend(list2)
print("merge list:", list1)

print()
print()

# write a python program to find the sum of list elements.

print("2.find the sum of list elements")
print(" ------------------------------")
numbers = list(eval(input("enter: ")))
sum = sum(numbers)
print(sum)

print()
print()

# 3.write a python program to print even and odd separately in list

print("3.print even and odd using list ")
print("  -----------------------------")

input_str = list(eval(input("Enter a list: ")))

# Initialize two empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Separate the even and odd numbers
for num in input_str:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print the even numbers
print("Even numbers:", even_numbers)

# Print the odd numbers
print("Odd numbers:", odd_numbers)

print()
print()

# 4.write a python program to delete element of given index in list

print("4.delete element of given index in list")
print("  -------------------------------------")

element = [1,2,3,4,5]
element.pop(4)
print(element)

print("------------------------------------------------------------------------------------------------")

element = list(eval(input("Enter a list of integers separated by spaces: ")))


print("Original list:", element)

index_to_delete = int(input("Enter the index to delete: "))

# Check if the index is within the valid range
if 0 <= index_to_delete < len(element):
    deleted_element = element.pop(index_to_delete)
    print(f"Deleted element: {deleted_element}")
    print(f"Updated list: {element}")
else:
    print("Invalid index. Index is out of range.")

print()
print()

# 5.wrte a python program tp delete a given element from the list

print("5.delete a given element from the list")
print(" -------------------------------------")

list_element = [1, 2, 3, 4, 5]
delete_element = list_element.remove(3)
print(list_element)

print()
print("-------------------------------------------------------------------")
print()

my_list = list(eval(input("enter list: ")))

print("my_list: ",my_list)

element_delete = int(input("enter the element to delete: "))

if element_delete in my_list:
    my_list.remove(element_delete)
    print("updated list: ",my_list)
else:
    print("not found")

# 6.write a python program to insert an elemet  at given index location

print("6.insert an elemet at given index location")
print("  ----------------------------------------")

fruits = ["apple","banana","cherry"]
fruits.insert(3,"watermelon")
print(fruits)

print(".............................................")

fruit = ["apple", "banana", "cherry"]
fruit[1:3] = ["watermelon"]
print(fruit)

print(".............................................")

l = [1,2,3,4,5,6]
print("original array: ",l)

index = int(input("index: "))
element = int(input("element: "))

l.insert(index,element)
print('update element:',l)

print('.............................................')

l = list(eval(input("enter l: ")))
print("original array: ",l)

index = int(input("index: "))
element = int(input("element: "))

l.insert(index,element)
print('update element:',l)

print()
print()

# 7.write a python program to check the sizes of given two lists are same

print("7.check the sizes of given two lists are same")
print("  -------------------------------------------")

list1 = input('list1: ')
list2 = input('list2: ')

if len(list1) == len(list2):
    print("the two lists are the same")
else:
    print("the two lists are not same")


print()
print()

# 8th question
# 8.1-print Write a Python function that takes two lists and returns True if they have at least one common member

f = '8th Question'
print(f.center(50," "))
print(50*"*")
print("8.1-print Python function that takes two lists and returns True if they have at least one common member")
print("    --------------------------------------------------------------------------------------------------")

def common_element(f1,f2):
    for x in f1:
        if x in f2:
            return True
    return False

f1 = list(eval(input("enter f1:")))
f2 = list(eval(input("enter f1:")))

if common_element(f1,f2):
    print("The two lists have at least one common integer.")
else:
    print("The two lists do not have a common integer.")

print()
print("8.2- Remove a specified column from a given nested list")
print("     --------------------------------------------------")

def remove_column(nested_list, column_index):
    for row in nested_list:
        del row[column_index]

nested_list = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
column_to_remove = 0  

remove_column(nested_list, column_to_remove)

print("After removing 1st column:")
for row in nested_list:
    print(row)

print()
print()

# 9.Write a Python program to convert a list of multiple integers into a single integer.

print("9.convert a list of multiple integers into a single integer")
print("  ---------------------------------------------------------")

integer_list = list(eval(input("Enter a list of integers separated by spaces: ")))

result =  ''.join(integer_list)

integer = int(result)
print(integer)

print()
print()

#10.Write a Python program to remove duplicates from a list.

print('10.remove duplicates from a list')
print('   -----------------------------')

list_int = list(eval(input("list: ")))
unique_list = list(set(list_int))
print(unique_list)