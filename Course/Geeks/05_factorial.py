def fact(num):
	if num == 1:
		return 1
	elif num == 0:
		return 1
	else:
		return num * fact(num-1)

num1 = int(input("Enter the number:"))
res = fact(num1)
print(res)
