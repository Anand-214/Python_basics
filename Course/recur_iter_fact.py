"""Functions defined."""
def fact_iter(n):
	fact = 1
	for i in range(n):
		fact = fact * (i+1)
	return fact

def fact_rec(n):
	if n == 1:
		return 1
	else:
		return n * fact_rec(n-1)



"""Main body"""
print("Enter the number:",end="")
n = int(input())
print("Factorial iterative:",fact_iter(n))
print("Factorial recursion:",fact_rec(n))
str1 = "Mira"
for i in range(len(str1)):
	print(str1[i],end=" ")
