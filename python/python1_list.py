# 1. write a python program to merge two list

list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
print(list1+list2)
list1.extend(list2)

print("---------------------------------------------------------------------------------------------------------")

# 2. write a program to find the sum of list elements

number = [1,2,3,4,5,6]
add = sum(number)
print(add)

print("---------------------------------------------------------------------------------------------------------")

# 3. print even and odd using list

str = [1,2,3,4,5,6]
even = []
odd = []

for num in str:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)

print("---------------------------------------------------------------------------------------------------------")

# 4. program to delete a given index in list

element = [1,2,3,4,5]
element.pop(2)
print(element)

print("---------------------------------------------------------------------------------------------------------")

# 5. program to delete a given element from a list
list_ = [1,2,3,4,5]
dele = list_.remove(5)
print(list_)

print("---------------------------------------------------------------------------------------------------------")

# 6. program to insert given element in a list

lists = ["toy","boy","play"]
inser = lists.insert(2,"see")
print(lists)

print("---------------------------------------------------------------------------------------------------------")

# 7. check the sizes of given two lists are same size

list11 = [1,2,3,4,5,5]
list22 = [12,3,4,5]

if list11 == list22 :
    print("same")
else:
    print("not same")
    
print("---------------------------------------------------------------------------------------------------------")

# 8. remove duplicates from list

list11 = [1,2,3,4,3,2,1]
unique = list(set(list11))
print(unique)

print("---------------------------------------------------------------------------------------------------------")

# remove a specific column from a given nested list

def remove_col(nested_lsit,col_index):
    for row in nested_lsit:
        del row[col_index]
        
nested_lsit = [1,2,3],[4,5,6],[7,8,9]
column_to_remove = 0

remove_col(nested_lsit,column_to_remove)
print("after removing 1st column: ")
for row in nested_lsit:
    print(row)
    
print("---------------------------------------------------------------------------------------------------------")

# 10. python function that takes two lists and return True if they have atleast one common member
def common_element(f1,f2):
    for x in f1:
        if x in f2:
            return True
    return False

f1 = [1,2,3,4]
f2 = [3,4,5,6]

if common_element(f1,f2):
    print("common integer")
else:
    print("not having common element")
    
print("---------------------------------------------------------------------------------------------------------")

# integer_list = [1,2,3,4,5]
# result = ''.join(integer_list)
# integer = int(result)
# print(integer)

print("---------------------------------------------------------------------------------------------------------")

# 11. find the way of maximum of two numbers

a = 2
b = 4
maximum = max(a,b)
print(maximum)

print("---------------------------------------------------------------------------------------------------------")

# 12. find minimum of two numbers

a = 2
b = 4
minimum = min(a,b)
print(minimum)

print("---------------------------------------------------------------------------------------------------------")

# 13. find the largest number of list

list1 = [12,34,56,45,99,32]
print(max(list1))

print("---------------------------------------------------------------------------------------------------------")

# 14. count the unique values in a list

input_list = [1,2,2,5,8,4,4,8]

l1 = []
count = 0
for item in input_list:
    if item not in l1:
        count += 1
        l1.append(item)
print(count)