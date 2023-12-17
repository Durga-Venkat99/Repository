print('10.remove duplicates from a list')
print('   -----------------------------')

list_int = input("list: ").replace(',',' ').split()
unique_list = list(set(list_int))
print(unique_list)