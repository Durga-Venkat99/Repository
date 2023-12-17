print("1.merge two list")
print("----------------")
list1 = input("enter list1: ")
list2 = input("enter list2: ")
list1 = [int(x) for x in list1.split(',')]
list2 = [int(x) for x in list2.split(',')]
print(list1+list2)
list1.extend(list2)
print("merge list:", list1)