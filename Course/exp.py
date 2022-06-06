list1 = []
print("1.Append\n2.Insert\n3.Pop\n4.reverse\n5.Remove\n")
usr_ip = input("Enter the command number and the parameters: ")
red = list(map(int,usr_ip.split(" ")))
print(red)
if red[0] == '1':
	list1.append(red[1])
	print(list1)
elif red[0] == '2':
	list1.insert(red[2], red[1])
	print(list1)

elif red[0] == '3':
	list1.pop(red[1])
	print(list1)
