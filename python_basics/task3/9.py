# 9. write a program to remove a key from dictionary 

print("9.remove a key from dictionary")
print(" -----------------------------")
my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_remove = 'b'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")
print("Updated Dictionary:", my_dict)
