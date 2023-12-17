# 7.write a python program to check the sizes of given two lists are same

print("7.check the sizes of given two lists are same")
print("  -------------------------------------------")

list1 = input('list1: ')
list2 = input('list2: ')

if len(list1) == len(list2):
    print("the two lists are the same")
else:
    print("the two lists are not same")

print("......................................................................")

list1 = input('list1: ').replace(',',' ').split()
list1 = [int(x) for x in list1]

list2 = input('list2: ').replace(',',' ').split()
list2 = [int(x) for x in list2]

if len(list1) == len(list2):
    print("the two lists are the same")
else:
    print("the two lists are not same")

# question1 : here when we giving the same word three times in one list1 and list2 different word three its gave not same.