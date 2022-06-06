
def fibo_iter (num):
	var = 0
	var1 = 1
	var2 = var + var1
	for i in range(num):
		while var2<=num:
			print(var2,end=" ")	
			var1 = var
			var = var2
			var2 = var + var1

def fibo_rec (num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return (fibo_rec(num-1)) + (fibo_rec(num-2))


print("Enter the number:",end="")
num = int(input())
print("Fibonacci iterative:")
print("0",end=" ")
fibo_iter(num)
print("Fibonacci recursive:")
print("0",end=" ")
fibo_rec(num)

	


