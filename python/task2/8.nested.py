# 8th question
# 8.1-print Write a Python function that takes two lists and returns True if they have at least one common member

f = '8th Question'
print(f.center(50," "))
print(50* "*")

def common_element(f1,f2):
    reult = False
    for x in f1:
        if x in f2:
            result = True
            return result
    return reult

f1 = input("enter_f1: ").replace(',',' ').split()
f1 = [int(x) for x in f1]

f2 = input("enter_f2: ").replace(',',' ').split()
f2 = [int(y) for y in f2]

print(common_element(f1,f2))

print()
print(".....................................................................................")
print()
def common_element(f1,f2):
    for x in f1:
        if x in f2:
            return  True
    return False

f1 = input("enter_f1: ").replace(',',' ').split()
f1 = [int(x) for x in f1]

f2 = input("enter_f2: ").replace(',',' ').split()
f2 = [int(y) for y in f2]

if common_element(f1,f2):
    print("the list having a same element")
else:
    print("their is no same element")

# 8.2 Write a Python program to remove a specified column from a given nested list.

def remove_column(nested_list,n):
    for i in nested_list:
        if n < len(i):
            del i[n]

# read the nested list from the user
nested_list = [ ]
num_rows = int(input("enter the number of rows: "))
num_cols = int(input("enter the number of columns: "))

# Input the nested_list
for m in range(num_rows):
    i = []
    for j in range(num_cols):
        element = input(f"Enter element for row {m+1}, column {j+1}: ")
        i.append(element)
    nested_list.append(i)

# Display the original nested list
print(" Original nested list: ")
for i in nested_list:
    print(i)

# Get the index of the column to remove from the user
column_to_remove = int(input("Enter the index of the column to remove: "))

# Remove the specified column
remove_column(nested_list,column_to_remove)

# Display the updated nested list
print("After removing the specified column:")
for i in nested_list:
    print(i)
print(i)

print()
print(".....................................................................................................")
print()

def remove_column(nested_list, column_index):
    for row in nested_list:
        del row[column_index]

nested_list = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
column_to_remove = 0  

remove_column(nested_list, column_to_remove)

print("After removing 1st column:")
for row in nested_list:
    print(row)