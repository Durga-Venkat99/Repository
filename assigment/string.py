# membership operator using in and not in 
# 1. " IN " operator

Name = (" 1.IN OPERATOR ")
print(Name)
print("------------------------------------")
list = ["1","2","3","4","5"]
listed = "2"
if listed in list:
    print(listed, "is inlist")
else:
    print("not in the list")

print()

# 2. " NOT-IN " operator
Name = (" 2.NOT-IN OPERATOR ")
print(Name)
print("------------------------------------")
tuple = ("x","y","z","u","v")
num = 2
if num in tuple:
    print(num,"is in tuple")
else:
    print("not in the tuple")

print()

# 3. Membership operator with Dictionaries
print("3.Dictionaries ")
print("------------------------------------")
dict = {
    "name" : "venkat",
    "age"  : 25,
    "gender": "male"
}
check = "name"
if check in dict:
    print(check,"in dict")
else:
    print(check ,"not in dict")

dict = {
    "name" : "venkat",
    "age"  : 25,
    "gender": "male"
}
check = "phone number"
if check in dict:
    print(check,"in dict")
else:
    print(check ,"not in dict")

print()

# Finding a substring by using index
print("4.Finding a substring by using index")
print("--------------------------------------")

str = "hello to every one"
string = "to"
result = str.index(string)
print("the index of the substring is found:",result)

result1 = str.index(" ")
print("the index where the substring is found:",result1)

str = "hello to every one nice to meet you"
str2 = " "
result2 = str.index(str2, 7, 9)
print("the index where substring is found:",result2)

print()

# string method using rindex()
print("5.rindex Method ")
print("-----------------------------------------")
string = "this is a great place to learn python "
print(string.rindex("learn"))
print(string.rindex('is'))
print(string.rindex('python', 0, 37))              # here 0-37 letters are counting in a string including spaces

print()

# string method using Find()
print("6.Finding the substring using Find")
print("-----------------------------------------")
str = "easy to learn python"
str1 = "learn"
result = str.find(str1)
print("the index of the substring is found:",result)

str2 = "python"
result1 = str.find(str2, 4)
print("the index of the substring is found:",result1)

print()

# rFind Method
print(" 7.rFind Method ")
print("-----------------------------------------")
str1 = "this is string"
str2 = "is"
found = str1.rfind(str2)
print("this index of substring :",found)

found = str1.rfind("hello")
print("this index of substring :",found)

found = str1.rfind("is", 2, 5)
print("this index of substring :",found)

print()

# Joins Method
print("8.Joins Method ")
print("-----------------------------------")
ab = "-"
char = ("a","b","c")
print(ab.join(char))

sets = {'3','5','3','2','5','4'}
charc = "/"
res = charc.join(sets)
print(res)

print()

# Replace method
print("9.Replace Method")
print("-----------------------------------")
name = "welcnme tn marnlix"
str = name.replace("n","o")
print("name :",str)

# Split method
print("10.split Method")
print("------------------------------------")
words = "ab,bc,cd,da,db,ac"
print(words.split(","))
print(words.split(",",2))

print()

# 11.Using comparison operators to compare strings
print(" 11.Using comparison operators to compare strings")
print("--------------------------------------------------")
string1 = "apple"
string2 = "banana"
if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

if string1 != string2:
    print("The strings are not equal.")
else:
    print("The strings are equal.")

if string1 < string2:
    print("string1 comes before string2.")
else:
    print("string1 does not come before string2.")

if string1 > string2:
    print("string1 comes after string2.")
else:
    print("string1 does not come after string2.")

print()

# 12. capitalize method
print("12.capitalize method")
print("--------------------------------------------")
a = "capitalize method"
print(a.capitalize())

b = "welcome to marolix"
print(b.capitalize())

print()

# 13.center method
print("13.center method")
print("---------------------------------------------")
name = "venkat"
output = name.center(20,".")
print(output)

print(name.center(20," "))                   # here reading a space to make a center

# 13.count method
print("13.count method")
print("---------------------------------------------")
word = ("hello,this is venkat")
sub_count = "is"
print("the word of is count: ",word.count(sub_count))

words = ("the cost of amount is ten and what is ?")
sub_words = "ten"
output = words.count(sub_words)
print("the words of ten count: ",output)

words = ("the cost of amount is ten and what is ?")
sub_words = " "
output = words.count(sub_words)
print("the space are count as: ",output)

print()

# 14. decode() method
print("14.Decode method")
print("---------------------------------------------")

str = ("hey this is python course")
str_encoded = str.encode()
print("the encode is : ",str_encoded)
str_decoded = str_encoded.decode()
print("the decode is :",str_decoded)

print()

#15.Endswith method
print("15. Endswith Method")
print("---------------------------------------------")

img = ("picture of coloring.")
sub_img = "ring."
result = img.endswith(sub_img)
print("the result is:",result)

img = ("picture of coloring.")
sub_img = "ring."
result = img.endswith(sub_img, 15,20)
print("the result is:",result)

img = ("picture of coloring.")
sub_img = "ring."
result = img.endswith(sub_img, 20)
print("the result is:",result)

print()

#16. isAlpha method
print("16.is-Alpha")
print("---------------------------------------------")

vs = ('Welcome')
print("the 'vs' is : ",vs.isalpha())

ss = ("python")
result = ss.isalpha()
print("the 'ss' is : ",result)

str = ("welcome ")
result=str.isalpha()
print("the str is: ", result)

print()

# 16.numeric and digits methods
print("16.numeric and digits methods")
print("----------------------------------------------")
str = "Welcome2023"
result=str.isnumeric()
print("the str is: ", result)

str = ("2023")
result=str.isnumeric()
print("the number is: ", result)

str = ("\00B3E")
result=str.isnumeric()
print("the character is: ", result)

print()

# 17.Title method
print("17.Title method")
print("---------------------------------------------")

str = "Home"
result=str.istitle()
print("Is the input string is: ", result)

str = "Hello world"
result=str.istitle()
print("Is the input string is: ", result)

str = "Hello World"
result=str.istitle()
print("Is the input string is: ", result)

# 18.swapcase method

print("18.swapcase method")

str = "hello world"
print(str.swapcase())

str = "Hello World"
print(str.swapcase())

str = "HELLO WORLD"
print(str.swapcase())