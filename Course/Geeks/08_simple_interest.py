def SI_calculator(p,n,r):
	return float((p*n*r)/100)

principle = float(input("Enter the principle:"))
tenure = int(input("Enter the tenure:"))
rate = float(input("Enter the rate:"))
res = SI_calculator(principle, tenure, rate)
print(res)
