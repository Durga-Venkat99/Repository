# Recursive function to find power of a number
t = "RECURSION FUNCTION"
print(t.center(60," "))
print("1.Recursion function to find power of a number")
print("  --------------------------------------------")

def power(n,p):
    if p == 0:
        return 1
    return (n*power(n, p-1))
if __name__ == '__main__':
    n = 7
    p = 2

    print(power(n,p))

print()
print("*********************************************************************************")
print()

# 2.Using recursion function to get sum of digits

print("2.recursion on sum of digits")
print("   -------------------------")
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_of_digits(remaining_digits)

result = sum_of_digits(12345)  # Calculates the sum of digits in 12345, which is 1+2+3+4+5 = 15
print(result)

print()
print("******************************************************************************************")
print()

# 3.write a python program to find sum of a nested list using recursion

print("3.Sum of nested list using recursion")
print("  ----------------------------------")

def nested_list(n):
    total = 0
    for j in range(len(n)):
        if type(n[j]) == list:
            total += nested_list(n[j])
        else:
            total += n[j]
    return total
print(nested_list([[1,2,3],[6,7],8]))

print()
print("******************************************************************************************")

s = "LAMBDA FUNCTION"
print(s.center(60," "))
# 1.write a python program to convert string into upper case by using lambda function

print("1.convert string into upper case by using lambda function")
print("  -------------------------------------------------------")

string = "marolix technologies"
upper = lambda string:string.upper()
print(upper(string))

print()
print("********************************************************************************************")
print()

# 2.write python program to print cube using lambda function 

print("2.cube using lambda function")
print("  --------------------------")

def cube(y):
	return y*y*y

lambda_cube = lambda y: y*y*y

print("Using lambda function, cube:", lambda_cube(5))

print()
print("****************************************************************************************************")
print()

# 3.Example of lambda function using if-else

print("3.using lambda function on ifelse")
print("  -------------------------------")
Max = lambda a, b : a if(a > b) else b

print(Max(1, 2))


print()
print()
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

print()
print()

# 1.Adding two functions by using map functions

m = "MAP FUNCTION"
print(m.center(60,"_"))
print()
print("ADDING TWO ELEMENTS USING MAP FUNCTION")
n1 = list(eval(input("enter:")))
n2 = list(eval(input("enter:")))

results = map(lambda x,y : x+y, n1,n2)
print(list(results))

print()
print(60*"*")
print()

# 2.Using map function on list of string
print("2.list of string map function")
print("  ---------------------------")

user_input = input("Enter a string: ")
result = list(map(list, user_input.split(",")))
print(result)

print()
print(60*"*")
print()

# 3.Double the even numbers by using  map function

print("3.Double the even number using map function")
print("  -----------------------------------------")

def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num

numbers = list(eval(input("enter numbers: "))) # Split and convert to integers

result = list(map(double_even, numbers))
print(result)

print()
print(100*"*")
print()

r = "REDUCE FUNCTION"
print(r.center(60,"_"))
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