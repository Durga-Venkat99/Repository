# 5.wrte a python program tp delete a given element from the list

print("5.delete a given element from the list")
print(" -------------------------------------")

list_element = [1, 2, 3, 4, 5]
delete_element = list_element.remove(3)
print(list_element)

print()
print("-------------------------------------------------------------------")
print()

my_list = input("enter list: ")

num_list = [int(num_str) for num_str in my_list.replace(',',' ').split()]

print("my_list: ",my_list)

element_delete = int(input("enter the element to delete: "))

if element_delete in num_list:
    num_list.remove(element_delete)
    print("updated list: ",num_list)
else:
    print("not found")
