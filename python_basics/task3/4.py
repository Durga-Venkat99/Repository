# 4.write a Python script to print a dictionary with keys as numbers between 1 and 15(both included) and the values are the square of the keys

print("4.the dictionary with keys and square the key")
print(" --------------------------------------------")

dict = {}

for num in range(1,16):
    dict[num] = num ** 2
print(dict)