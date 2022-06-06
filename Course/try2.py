def max_worked_hrs(inp_list):
	max_hrs = 0
	emp_name = ''
	for name, hr in inp_list:
		if hr > max_hrs:
			max_hrs = hr
			emp_name = name
	return (emp_name,hr)



work_hrs = [("Abbie",1000),("Shaggy",200),("Chassie",300)]
res,hr = max_worked_hrs(work_hrs)
print(f"The employee {res} has worked the longest for {hr}")
a = 10
b = 15
print(sum(a,b))
