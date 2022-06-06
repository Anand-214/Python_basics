from functools import reduce
def first_4th_caps(inp):
	rand_list = []
	for i in range(len(inp)):
		if i==0 or i==3:
			rand_list.append(inp[i].upper())
		else:
			rand_list.append(inp[i])
	return ''.join(rand_list)

def small_caps(name):
	new_name = []                #store everything in a blank list
	for i in range(len(name)):   #here i will be integers 0 1 2 3 
		if i%2 == 0:
			new_name.append(name[i].upper())
		else:
			new_name.append(name[i].lower())
	return ''.join(new_name)

res = small_caps(input("Enter the name:"))
print(res)

res2 = first_4th_caps(input("Enter the name:"))
print(res2)

			
