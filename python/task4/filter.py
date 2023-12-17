# 1.python code to get odd abd even number using filter function

v = "Filter Function"
print(v.center(60," "))

print("1.Using filter function get even and odd")
print("  --------------------------------------")

data = [10,2,3,4,56,32,42,21,59]

print([x for x in data if x % 2 == 0])
print([x for x in data if x % 2 != 0])

print()
print("*********************************************************************************************************")
print()

# 2.python code find number divisible using filter function

print("2.using filter function find divisible by number")

my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
result = list(filter(lambda x: (x % 13 == 0), my_list)) 
print(result)