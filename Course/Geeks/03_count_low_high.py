list1 = [20,9,51,81,50,42,77]
count_low = 0
count_high = 0
for i in range(len(list1)):
	if list1[i] > 50 or (list1[i]%3 == 0):
		count_high += 1
	else:
		count_low += 1
result = [count_low,count_high]
print(result)
