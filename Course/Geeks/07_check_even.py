
def even_check (list_1):
	new_list = []
	for i in list_1:
		if (i%2) == 0:
			new_list.append(i)	
		else:
			pass
	return new_list


list_1 =  [1,2,3,4,5,6,7,9,10]
x = even_check(list_1)
print(x)

