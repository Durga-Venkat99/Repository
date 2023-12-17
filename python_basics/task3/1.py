# 1.Write a Python script to add a key to a dictionary

print("1.add a key to a dictionary")
print("  -------------------------")

d = {0 : 10,1 : 20}

key = int(input("key : "))
value = int(input("value : "))

d[key] = value

print(d)