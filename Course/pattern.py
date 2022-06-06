print("Enter the number of rows",end=":")
rows = int(input())
print("1)Straight\n2)Inverted\nChoose your option",end=":")
var2 = int(input())
if var2 == 1:
	for i in range(1,rows+1):
		for j in range(1,i+1):
			print("*")

