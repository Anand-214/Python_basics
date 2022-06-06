list = [16,36,49]
for item in list:
    print(int(item**0.5))

list_in_list = [["Harry",2], ["Marry",3], ["Carry", 6], ["Larry", 10]]
dict1 = dict(list_in_list)
for item,quantity in dict1.items():
    print(f'{item} eats {quantity} Pizza.')
