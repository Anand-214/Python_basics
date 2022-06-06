def armstrong(str1, n):
	var = 0
	for i in range(n):
		res = int(str1[i])**n
		var = var + res
	return var


str1 = input("Enter the number:")
str2 = int(str1)
n = len(str1)
ret = armstrong(str1,n)
if ret == str2:
	print("Its armstrong number.")
else:
	print("Its not armstrong number.")


