class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def m1(self):
        print("name - ",self.name)
        print("age - ",self.age)
class student(person):
    def __init__(self,name,age,rollno,attendence):
        super().__init__(name,age)
        self.rollno = rollno
        self.attendence = attendence
    def m2(self):
        super().m1()
        print("rollno - ",self.rollno)
        print("attendence - ",self.attendence,"%")
s1 = student("ram",24,991,80)
s1.m2()

print(80*"-")

class parent:
    a = 10
    def __init__(self):
        self.b = 20
class child(parent):
    def m1(self):
        print(self.b)
        print(super().a)
c = child()
c.m1()

print(80*"-")

class p:
    def __init__(self):
        print("this is constructor")
    def m1(self):
        print("this is instance method")
    @classmethod
    def m2(cls):
        print("this is class method")
    @staticmethod
    def m3():
        print("this is static method")
class c(p):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m4(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c = c()
c.m4()

print(80*"-")

# inside the instance method
class p:
    def __init__(self):
        print("this is parent constructor")
    def m1(self):
        print("this is parent instance method")
    @classmethod
    def m2(cls):
        print("this is clss method")
    @staticmethod
    def m3():
        print("this is static method")
class C(p):
    @classmethod
    def m4(cls):
        super().m2()
        super().m3()
    
c = C()
c.m4()

class p:
    def __init__(self):
        print("this is parent constructor")
    def m1(self):
        print("this is parent classmethod")
    @classmethod
    def m2(cls):
        print("this is parent classmethod")
    @staticmethod
    def m3():
        print("this is static method")
class C(p):
    @classmethod
    def m4(cls):
        super(C,cls).m1(cls)

c = C()
c.m4()

# inside of staticmethod
class p:
    def __init__(self):
        print("this is parent constructor")
    def m1(self):
        print("this is parent instance method")
    @classmethod
    def m3(cls):
        print("this is class method")
    @staticmethod
    def m4():
        print("this is static method")

class E(p):
    @staticmethod
    def m4():
        super(E,E).m3()

    @staticmethod
    def m5():
        super(E,E).m3()

c = E()
c.m4()

class A:
    def m1(self):
        print("m1() method from A class")
class B(A):
    def m1(self):
        print("m1() method from B class")

class C(B):
    def m1(self):
        print("m1() method from C Class")
class D(C):
    def m1(self):
        print("m1() method from D class")
class E(D):
    def m1(self):
        super(C, self).m1()
e = E()
e.m1()