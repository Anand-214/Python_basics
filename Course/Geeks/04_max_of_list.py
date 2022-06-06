length = int(input("Enter the list length:"))
my_list = []
print("Enter the elements")
max_elem = 0
for i in range(length):
	elem = int(input())
	my_list.append(elem)
	if my_list[i] > max_elem:
		max_elem = my_list[i]
print("The user entered list is: ",my_list)
print("Largest element:", max_elem)
