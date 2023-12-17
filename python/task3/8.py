# 8.Write a Python program to access dictionary key's element by index

print("8.access dictionary key's element by index")
print("  ----------------------------------------")

dict = {}

items = int(input("enter items: "))
for n in range(items):
    key = input("enter key: ")
    value = input("enter value: ")
    dict[key] = value
order = input("enter the order of keys separated:").replace(',',' ').split()
for key in order:
    print(dict[key])