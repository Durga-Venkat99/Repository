fruits = ["apple","banana","cherry"]
fruits.insert(3,"watermelon")
print(fruits)


l = input("l : ").replace(',',' ').split()
for x in l:
    print(int(x))
print("original array: ",l)

index = int(input("index: "))
element = int(input("element: "))

l.insert(index,element)
print('update element:',l)

print()

l = input("l : ").replace(',',' ').split()
[int(x) for x in l]
print("original array: ",l)

index = int(input("index: "))
element = int(input("element: "))

l.insert(index,element)
print('update element:',l)