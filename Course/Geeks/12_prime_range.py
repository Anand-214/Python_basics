def prime_range(strt, end):
	prime_list = []
	for i in range(strt,end):
		for j in  range(strt, end):
			if i%j == 0:
				break
			else:
				


strt = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
prime_range(strt, end)


