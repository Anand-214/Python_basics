def Compound_Interest (p,t,r):
	A = p*(1+(r/100))**t
	CI = A-p
	return CI

principle = float(input("Enter the principle:"))
tenure = int(input("Enter the tenure:"))
rate = float(input("Enter the rate:"))
res = Compound_Interest(principle, tenure, rate)
print("{:10.3f}".format(res))
