class calculator():
    def __init__(self,x,y):
        self.a = x
        self.b = y
    def add(self):
        return self.a + self.b
    def multiple(self):
        return self.a * self.b
    def product(self):
        return self.a / self.b
    def subtract(self):
        return self.a - self.b
    def square(self):
        return self.a ** self.b
x = int(input("number of X value: "))
y = int(input("number of Y value: "))
instance = calculator(x,y)
choice = 1
print(x,y)
while choice != 0:
    print("0.Exit")
    print("1.addition")
    print("2.subtraction")
    print("3.division")
    print("4.multiplication")
    print("5.square")
    choice = int(input("enter choice: "))
    if choice == 1:
        print("the addition is: ",instance.add())
    elif choice == 2:
        print("the subtraction is: ",instance.subtract())
    elif choice == 3:
        print("the division: ",instance.product())
    elif choice == 4:
        print("the multiplication: ",instance.multiple())
    elif choice == 5:
        print("the squaring on number: ",instance.square())
    elif choice == 0:
        print("EXIT")
    else:
        print("invalid ERROR")
print()