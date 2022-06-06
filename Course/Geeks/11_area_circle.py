def area_circle(rad):
	pi = 3.142
	return pi * (rad**2)


rad = int(input("Enter the radius:"))
res = area_circle(rad)
print("%.5f"%(res))

