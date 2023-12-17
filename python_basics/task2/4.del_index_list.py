# 4.write a python program to delete element of given index in list

print("4.delete element of given index in list")
print("  -------------------------------------")

element = input("Enter a list of integers separated by spaces: ")

num_list = [int(num_str) for num_str in element.split()]

print("Original list:", num_list)

index_to_delete = int(input("Enter the index to delete: "))

# Check if the index is within the valid range
if 0 <= index_to_delete < len(num_list):
    deleted_element = num_list.pop(index_to_delete)
    print(f"Deleted element: {deleted_element}")
    print(f"Updated list: {num_list}")
else:
    print("Invalid index. Index is out of range.")

print("----------------------------------------------------------------------------------------")
