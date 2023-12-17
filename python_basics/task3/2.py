# 2.Write a Python script to check whether a given key already exists in a dictionary.

print("2.script to check whether a given key already exists in a dictionary.")
print("  ------------------------------------------------------------------")

d = {0 : 10,1 : 20}

check = 1

if check in d:
    print("the key ",check,"exists in dictionary")
else:
    print("the key ",check,"doesn't exists in dictionary")