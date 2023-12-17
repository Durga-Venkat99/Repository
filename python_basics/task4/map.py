# 1.Adding two functions by using map functions

m = "MAP FUNCTION"
print(m.center(60,"_"))

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

numbers = list(eval(input("enter: ")))

result = list(map(double_even, numbers))
print(result)