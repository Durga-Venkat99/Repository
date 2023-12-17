'''
x = ["cat","dog","rat"]
y = ["cat","dog","rat"]
z = ['CAT','DOG','RAT']
print(x == y)
print(x != z)
print(x != y)

a = [10,20,30]
b = [60,70,80]
print(a > b)
print(a < b)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[0])  # Output: [1, 2, 3]
print(nested_list[1][1])  # Output: 5
print(len(nested_list))

for element in nested_list:
    print(element)

n = [1,2,3,4,5,[6,7,8,9,[10,11,12,13],14]]
for element in n:
    print(element)

print(n[5])
print(n[5][2])

for i in nested_list:
    print(nested_list)

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for l in n:
    print(l)

#n = [1,2,3,4,5,[6,7,8,9,[10,11,12,13],14]]
#for element in n:
#    print(element)
print(n[5][4][0])

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in l:
    print(i)
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=" ")
    print()

x = ("salar",10,True,3.0)

t = (4,5,2,1,7,8,9)
print(min(t))
print(max(t))



t =[x*x for x in range(1,6)]
print(t)

t =tuple(x*x for x in range(1,6))
print(t)
'''
'''
l1 = list(eval(input("enter: ")))
print(l1)
'''
'''
def wish(name):
    print("hello",name,"good morning")
wish("sai")
wish("chandu")
'''
'''
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

result = greet("Alice")  # Uses the default greeting
print(result)
'''
'''
# Sample Dictionary
sample_dict = {0: 10, 1: 20}

# Key to check
key_to_check = 2  # You can change this to any key you want to check

# Check if the key exists in the dictionary
if key_to_check in sample_dict:
    print(f"The key {key_to_check} exists in the dictionary.")
else:
    print(f"The key {key_to_check} does not exist in the dictionary.")
'''

# def wish(name = "python"):
#    print("hello",name)
#wish("world")
#wish()
'''
def wish(name = "python",country = "bharat"):
   print("hello",name,country)
wish("world","india")
wish()
'''

'''
# variable length argument(*)
def sum(*n):
    count = 0
    for i in n:
        count = count+i
    print(count)
sum(10,20,30,40)
'''
'''
# local and global variable

a = "global variable"
def function_1():
    print(a)
def function_2():
    a = 'local variable'
    print(a)
function_1()
function_2()
'''
'''
a = 100
def function1():
    a = 999
    print(a)
def function2():
    print(a)
function1()
function2()
'''
'''
positional arguments
variable length arguments
keyword variable length argument
global variable
local variable
'''
"""
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Generate the first 10 numbers in the Fibonacci series
for i in range(10):
  print(fibonacci(i))
""" 
"""
# NESTED REDUCE FUNCTION 
def add(x,y):
    z = 10
    def multiple(x,y):
        print(x*y)
        z = 10
    print(x+y+z)
    multiple(20,30)
add(20,30)
"""


'''
class banking:
    def __init__(self):
        self.pin = None
        self.bal = 0.0
        self.menu()
    def menu(self):
        while True:
            print("1.SET PIN")
            print("2.DEPOSITE")
            print("3.WITH DRAW")
            print("4.CHECK BALANCE")
            print("5.EXIT")
            choice = input("select an option(1/2/3/4/5): ")
            if choice == "1":
                self.set_pin()
            elif choice == "2":
                self.deposite()
            elif choice == "3":
                self.with_draw()
            elif choice == "4":
                self.balance()
            elif choice == "5":
                print("EXIT")
            else:
                print("INVALID PIN OR CHECK ONCE")
    def set_pin(self):
        self.pin = input("enter your pin: ")
        if self.pin:
            print("pin set successfully")
        else:
            print("enter a pin")
    def deposite(self):
        attempt = input("enter your pin: ")
        if attempt == self.pin:
            amount = float(input("Add amount: "))
            if amount > 0:
                self.bal += amount
                print ("your balance is ",amount)
            else:
                print("INVALID AMOUNT")
        else:
            print("enter correct pin")
    def with_draw(self):
        attempt = input("enter your pin: ")
        if attempt == self.pin:
            amount = float(input("enter amount: "))
            if 0 < amount <= self.bal:
                self.bal -= amount
                print("With draw amount $",amount)
            else:
                print("insufficient amount")
        else:
            print("invalid pin")
    def balance(self):
        attempt = input("enter your pin:")
        if attempt == self.pin:
            print("your balance is $",self.bal)
        else:
            print("invalid pin")
if __name__ == "__main__" :
    atm = banking()
    '''
'''
class calculator:
    def __init__(self,x,y):
        self.a = x
        self.b = y
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def multiple(self):
        return self.a*self.b
    def product(self):
        return self.a/self.b
    def square(self):
        return self.a ** self.b
x = int(input("enter x values: "))
y = int(input("enter y values: "))
instance = calculator(x,y)
choice = 1
while True:
    print("0.exit")
    print("1.add")
    print("2.sub")
    print("3.multiple")
    print("4.product")
    print("5.square")
    choice = int(input("enter option(1/2/3/4/5): "))
    if choice == 1:
        print("result of Adding: ",instance.add())
    elif choice == 2:
        print("result of subtract: ",instance.sub())
    elif choice == 3:
        print("result of multipling: ",instance.multiple())
    elif choice == 4:
        print("result of product: ",instance.product())
    elif choice == 5:
        print("result of square: ",instance.square())
    elif choice == 0:
        exit
    else:
        print("SYNTAX ERROR")
        '''
'''
class grandfather():
    def grandpa(self):
        print("grandfather")
class parent(grandfather):
    def father(self):
        print("he is father")
class child(parent):
    def son(self):
        print("he is my grandfather")

child = child()
child.grandpa()
child.father()
child.son()
'''
'''
class employee:
    company = "marolix"
    def __init__(self,name,id):
        self.name = name
        self.id = id
e = employee("venkat",123)
print(e.name,e.company)
'''

'''
class local:
    def method1(self):
        a = 1000
        print(a)
    def method2(self):
        b = 2000
        print(b)
l = local()
l.method1()
l.method2()
'''
'''
# method overloading
def add(x,y):
    print(x+y)

def add(x,y,z):
    print(x+y+z)
add(10,23,30)
'''
'''
# contructor overloading
class poly:
    def __init__(self):
        print("constructor1")
    def __init__(Self):
        print("constrictor2")
    def __init__(self):
        print("constructor3")
p = poly
'''
'''
# overriding 
class p:
    def method1(self):
        print("this is method1")
    def method2(self):
        print("this is method2")
class C(p):
    def method2(self):
        print("this is childclass method2")
c = C()
c.method1()
c.method2()
'''
'''
class p:
    name = "venkat"
    _name = "durga"
    __name = "Saikumar"

    def m1(self):
        print(p.name)
        print(p._name)
        print(p.__name)
obj = p()
obj.m1()
print(obj.name)
print(obj._name)
print(obj._p__name)
'''
'''
class Student:
    def __init__(self, name, roll_number):
        self.__name = name  # Private attribute
        self._roll_number = roll_number  # Protected attribute

    # Public methods to access and modify private and protected attributes
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) >= 2:
            self.__name = name
        else:
            print("Name must be at least 2 characters long.")

    def get_roll_number(self):
        return self._roll_number

    def set_roll_number(self, roll_number):
        if roll_number > 0:
            self._roll_number = roll_number
        else:
            print("Roll number must be a positive integer.")

# Create a Student object
student = Student("Alice", 101)

# Accessing private and protected attributes
print("Name:", student.get_name())
print("Roll Number:", student.get_roll_number())

# Attempting to modify private and protected attributes
student.set_name("Bob")
print("Name:", student.get_name())

student.set_roll_number(102)
print("Roll Number:", student.get_roll_number())

# Demonstrate encapsulation by attempting to set invalid values
student.set_name("A")
student.set_roll_number(-1)
'''