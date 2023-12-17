# 8.Write a python program to Remove Repeated Character from String.

print("8.Remove Repeated Character from String.")
print(" --------------------------------------")

character = input("enter: ")
unique_charc = ""

for char in character:
    if char not in unique_charc:
        unique_charc += char
print(unique_charc)

# unique_charc = "establise the emporer"
