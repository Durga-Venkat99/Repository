# 1.write a python program to convert string into upper case by using lambda function
s = "LAMBDA FUNCTION"
print(s.center(50," "))
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

