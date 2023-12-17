# write a python program to remove a given character from string

print("1. A given character remove from string")
print("   ------------------------------------")
string = input("enter : ")
char = input("remove: ")
new_str = string.replace(char,"")
print(new_str)