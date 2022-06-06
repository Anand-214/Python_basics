thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

my_list = ["apple", "mi", "Samsung", "one+"]
new_list = [x for x in my_list if "a" in x]
print(new_list)
