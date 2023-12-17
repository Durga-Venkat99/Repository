r = "REDUCE FUNCTION"
print(r.center(60,"_"))
'''
#1.Mutiply two elements by using reduce function
print("1.mutiply two elements by using reduce function")
print("  ---------------------------------------------")

from functools import reduce

def multiply(x,y):
    return x*y
numbers = list(eval(input("enter numbers: ")))

result = reduce(multiply,numbers)

print(result)

print()
print(80*"*")
print()

# 2.Using Reduce Function on sum of list and maximum element from list

print("2.Reduce function on two elements")
print("  -------------------------------")
# example-1
import functools

list1 = list(eval(input("enter list: ")))

print("the sum of list is : ",end="")
print(functools.reduce(lambda a,b: a+b,list1))

print("the maximum elements of list is: ",end="")
print(functools.reduce(lambda a,b: a if a>b else b, list1))

print()
# example-2
import functools

input = input("enter list2: ")
list2 = [int(x) for x in input.split(',')]

print("the sum of list is : ",end="")
print(functools.reduce(lambda a,b: a+b,list2))

print("the maximum elements of list is: ",end="")
print(functools.reduce(lambda a,b: a if a>b else b, list2))
'''
print()

# NESTED REDUCE FUNCTION 
print("3.Nested function with Reduce function")
print("  ------------------------------------")

def add(x,y):
    z = 10
    def multiple(x,y):
        print(x*y)
        z = 10
    print(x+y+z)
    multiple(20,30)
add(20,30)

# eaxmple-2:

def add(x, y):
    z = 10
    print(x + y + z)
def multiple(x, y):
        print(x * y)

user_x = int(input("Enter a value for x: "))
user_y = int(input("Enter a value for y: "))

add(user_x, user_y)

user_input_x = int(input("Enter a value for x in multiple(): "))
user_input_y = int(input("Enter a value for y in multiple(): "))

multiple(user_input_x, user_input_y)
