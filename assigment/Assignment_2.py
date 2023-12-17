# while loop
num = int(input("enter a number: "))
i = 1

print("multiple table number")
while i<= 10:
    multiple = num * i
    print(f"{num} * {i} = {multiple}")
    i += 1

print('------------------------------------------------')

# for loop
value = int(input("enter a num : "))
for i in range(1,11):
    multiple = value * i
    print(value ,"x",i,"=", multiple)

print("------------------------------------------------")

# Logical "AND" operator
print(" AND Operator")

x = 10
y = 20

if x >5 and y >5:
    print("both x and y are positive")
else:
    print("both x and y are not positive")

print("-------------------------------------------------")

#Logical " OR " operator
print(" OR Operator")

age = 25
income = 50000

if age >= 18 or income>40000:
    print("he is eligible for loan")
else:
    print("he is not eligible")

print("---------------------------------------------------")

# Logical " NOT " Operator
print(" NOT Operator")

rainy = False

if not rainy:
    print("it's not rainy, you can go outside")
else:
    print("it's rainy, better stay inside")

print("-----------------------------------------------------")

# Relational Operators

print(" RELATIONAL OPERATORS ")
a = int(input("enter a num : "))
b = int(input("enter a num : "))

if a>b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equals to b")
else:
    print("a is less than b")

print("-----------------------------------------------------")

# Creatin logic table using Conditional Statement

print("CONDITIONAL STATEMENT")

list=[1,2,23,45,6,7]
for num in list:
    if num==2:
        print('num is ',num)
    elif num==23:
        print('found number ', num)
else:
    print('number not found')

