def fact_rec(n):
	"""Function to calaculate factorial of number using recursion"""
	if n == 1:
		return 1
	else:
		return n * fact_rec(n-1)
def fact_iter(n):
	"""Function to calaculate factorial of number using iterative method"""
	fac = 1
	for i in range(n):
	    fac = fac * (i+1)
	return fac

def loop_string(str1):
	for i in range(len(str1)):
		print(str1[i])

print("Enter the number",end=":")
n = int(input())
print("Factorial of number using recursion:",fact_rec(n))
print("Factorial of number using iterative:",fact_iter(n))
print("The character by character string is:")
loop_string("Anand")
'''for i in range(1,10):
    print(i)
'''



