# 1. find the missing number in an array of 1-100

array = list(range(1,101))
array.remove(42)
missing = sum(range(1,101)) - sum(array)
print("the missing number is: ",missing)

print("-------------------------------------------------------------------------")

# find duplicate number in an array of 1-100:

import random 

array = list(range(1, 101))
array += random.sample(range(1,101),5)
duplicate = set()
for num in array:
    if array.count(num)>1:
        duplicate.add(num)
print("duplicate numbers are: ",list(duplicate))

print("-------------------------------------------------------------------------")

# 3. compare the two arrays for equal size
array1 = [1,2,3,4,5]
array2 = [6,3,4,5,6]

if len(array1) == len(array2):
    print("both are not same")
else:
    print("both are same")
    
print("-------------------------------------------------------------------------")

# 4. find the largest and  smallest size of array

arra = ("apple","ball","cat")
largest = max(arra)
smallest = min(arra)
print("the largest size: ",largest)
print("the smallest size: ",smallest)

print("-------------------------------------------------------------------------")

# 5. find the second highest number in array

number = [34,65,76,89,23,12]
number.sort()
second_highest = number[-2]
print("the second highest number: ",second_highest)

print("-------------------------------------------------------------------------")

# 6. find the top two maximum numbers in an array

number1 = [34,12,76,89,23,65]
array.sort(reverse=True)
top_two_max = number1[:2]
print("the top two arrays: ",top_two_max)

print("-------------------------------------------------------------------------")

# 7.remove duplicates elements from arrys

array2 = [1,2,2,3,4,4,5,6,1]
unique_element = []

for num in array2:
    if num not in unique_element:
        unique_element.append(num)
print("array after removing duplicates: ",unique_element)

print("-------------------------------------------------------------------------")

# 8. calculate the lenght of array

array1 = [1,2,3,4,5]
length = 0
for _ in array1:
    length += 1
print(length)

print("-------------------------------------------------------------------------")

# 9. insert an element at the end of an array

numn = [1,2,3,4,5,6]

ins = numn.append(7)
print(numn)

print("-------------------------------------------------------------------------")

# 10. insert an element in given elemnet

numm = [1,2,3,4,5,6]
isn = numm.insert(3,2)
print(numm)

print("-------------------------------------------------------------------------")

# 11. delete a given element from the array

array0 = [1,2,3,4,5,6,7]
dele = array0.remove(4)
print(array0)
print("-------------------------------------------------------------------------")

# 12. delete at end of the element

ar = [1,23,45,66]
re = ar.pop()
print(ar)

print("-------------------------------------------------------------------------")

# 13. Reverse in array

arre = [1,2,3,4,5,6]
res = arre.reverse()
print(arre)